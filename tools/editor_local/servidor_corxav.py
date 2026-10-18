#!/usr/bin/env python3
"""Servidor local de leitura e edição CorXav; não publicar na internet."""
import argparse
import json
import os
import shutil
import tempfile
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

HERE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo', type=Path, default=Path.home() / 'Documents/Corpus_Xavante/repositorio/Corpus_Xavante')
    parser.add_argument('--port', type=int, default=8765)
    args = parser.parse_args()
    repo = args.repo.expanduser().resolve()
    datafile = repo / 'docs/leitura/dados.json'
    if not datafile.is_file():
        raise SystemExit('Arquivo não encontrado: ' + str(datafile))
    editor = HERE / 'editor_corxav.html'
    if not editor.is_file():
        raise SystemExit('Editor HTML não encontrado ao lado do servidor.')

    class Handler(SimpleHTTPRequestHandler):
        def __init__(self, *a, **kw):
            super().__init__(*a, directory=str(repo / 'docs'), **kw)

        def send_json(self, code, obj):
            b = json.dumps(obj, ensure_ascii=False).encode('utf-8')
            self.send_response(code)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(b)))
            self.send_header('Cache-Control', 'no-store')
            self.end_headers()
            self.wfile.write(b)

        def do_GET(self):
            path = urlsplit(self.path).path
            if path in ('/', '/editor', '/editor/'):
                b = editor.read_bytes()
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', str(len(b)))
                self.send_header('Cache-Control', 'no-store')
                self.end_headers()
                self.wfile.write(b)
            elif path == '/api/textos':
                try:
                    self.send_json(200, json.loads(datafile.read_text(encoding='utf-8'))['textos'])
                except (OSError, ValueError, KeyError) as exc:
                    self.send_json(500, {'erro': str(exc)})
            else:
                super().do_GET()

        def do_POST(self):
            if urlsplit(self.path).path != '/api/salvar':
                self.send_json(404, {'erro': 'Rota inexistente'})
                return
            try:
                length = int(self.headers.get('Content-Length', '0'))
                if not 0 < length <= 2_000_000:
                    raise ValueError('Tamanho de solicitação inválido')
                payload = json.loads(self.rfile.read(length).decode('utf-8'))
                edits = payload.get('alteracoes')
                if not isinstance(edits, list) or not edits:
                    raise ValueError('Nenhuma alteração recebida')
                if len(edits) > 2000:
                    raise ValueError('Alterações demais')
                doc = json.loads(datafile.read_text(encoding='utf-8'))
                textos = doc.get('textos')
                if not isinstance(textos, list):
                    raise ValueError('Formato de dados inválido')
                # Identificação por posição + id: permite IDs repetidos sem trocar registros.
                indices = set()
                for item in edits:
                    i = item.get('indice')
                    if type(i) is not int or not 0 <= i < len(textos) or i in indices:
                        raise ValueError('Índice inválido ou duplicado')
                    indices.add(i)
                    original = textos[i]
                    if original.get('id') != item.get('id') or original.get('obra') != item.get('obra'):
                        raise ValueError('O corpus foi alterado desde a abertura. Recarregue o editor.')
                    for key in ('xav', 'por'):
                        if not isinstance(item.get(key), str):
                            raise ValueError('Campo de texto inválido')
                    if (original.get('xav', '') != item.get('anterior_xav') or
                            original.get('por', '') != item.get('anterior_por')):
                        raise ValueError('Há alterações externas. Recarregue o editor antes de salvar.')
                for item in edits:
                    t = textos[item['indice']]
                    t['xav'] = item['xav']
                    t['por'] = item['por']
                backup = datafile.with_name('dados.json.backup-editor-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
                shutil.copy2(datafile, backup)
                fd, tmpname = tempfile.mkstemp(prefix='.corxav-', suffix='.json', dir=str(datafile.parent))
                try:
                    with os.fdopen(fd, 'w', encoding='utf-8') as f:
                        json.dump(doc, f, ensure_ascii=False, indent=2)
                        f.write('\n')
                        f.flush()
                        os.fsync(f.fileno())
                    os.replace(tmpname, datafile)
                finally:
                    if os.path.exists(tmpname):
                        os.unlink(tmpname)
                self.send_json(200, {'ok': True, 'salvas': len(edits), 'backup': backup.name})
            except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as exc:
                self.send_json(409, {'erro': str(exc)})

    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    print('Editor: http://127.0.0.1:%d/editor/' % args.port)
    print('Leitor: http://127.0.0.1:%d/leitura/' % args.port)
    print('Dados: ', datafile)
    print('Acesso limitado a este computador. Para parar: Control+C')
    server.serve_forever()


if __name__ == '__main__':
    main()
