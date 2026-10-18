# Corpus Xavante (CorXav)

Corpus textual e linguístico da língua xavante (A’uwẽ), voltado à documentação, pesquisa linguística e produção de recursos digitais, com revisão e tradução em colaboração com falantes.

**Autores:** Fabrício Ferraz Gerardi · Luas Toribio · Yvan Roksandic.

## Versão 0.2.0 — ampliação do corpus (18 de outubro de 2026)

A versão 0.2.0 amplia o acervo de trabalho com **sete narrativas tradicionais** (1.007 unidades de alinhamento preliminares), além dos materiais anteriormente incorporados de *Meu Mundo* e *A’uwe na Rowatsu’u*. As unidades das narrativas correspondem a segmentos de transcrição/glosa, **não necessariamente a sentenças**. Os textos, traduções e alinhamentos ainda exigem conferência e revisão linguística.

### Novidades

- Sete narrativas tradicionais incorporadas ao conjunto de dados do leitor.
- Leitura contínua dos contos em paralelo xavante–português.
- Consulta lexical por clique nas palavras xavante, busca de formas e ocorrências em contexto.
- Editor permanente **local**, com edição dos segmentos em xavante e português e salvamento no arquivo de trabalho.
- Busca e substituição no fluxo de revisão local; preservação de cópias de segurança.
- Rascunhos TSV e CoNLL-U preparados para anotação posterior; **não constituem um treebank UD validado**.
- Normalização inicial de `ò → o` e `è → e` no texto xavante das narrativas, com preservação das fontes originais.

Consulte [CHANGELOG.md](CHANGELOG.md) para o histórico de versões.

## Organização e acesso

- **Leitor:** `docs/leitura/index.html`; dados de leitura em `docs/leitura/dados.json`.
- **Editor local permanente:** `tools/editor_local/editor_corxav.html` e `tools/editor_local/servidor_corxav.py`.
- **Editor inicial:** `editor/index.html`, com importação/exportação e armazenamento no navegador.
- **Metadados e materiais de pesquisa:** `metadata/`, `sources/`, `texts/`, `translations/`, `annotations/` e `ud/`, conforme disponíveis no repositório.

### Executar o editor permanente

Requer Python 3.9 ou superior. Na raiz do repositório:

```bash
python3 tools/editor_local/servidor_corxav.py
```

O serviço local utiliza a porta 8765. Se ela já estiver ocupada, encerre o servidor anterior antes de iniciar este. Abra no navegador:

- Editor: `http://127.0.0.1:8765/editor/`
- Leitor: `http://127.0.0.1:8765/leitura/`

O editor altera o arquivo de trabalho `docs/leitura/dados.json` **no computador onde o serviço está sendo executado**. Faça cópias de segurança e revise as alterações antes de incorporá-las ao repositório. O GitHub Pages é estático e **não oferece salvamento no servidor**.

## Fontes, transcrição e anotação

Os materiais incluem *Meu Mundo*, *A’uwe na Rowatsu’u* I e II e sete narrativas tradicionais. As narrativas foram extraídas de material interlinear e estão disponíveis como segmentos de trabalho; a glosa portuguesa não deve ser confundida com tradução livre validada.

As camadas de transcrição, normalização ortográfica, tradução, segmentação, glosa, morfologia e dependências sintáticas são independentes. A inclusão de textos **não depende** de análise CoNLL-U. A sincronização automática entre revisões do editor e arquivos CoNLL-U ainda não está implementada.

Revisões devem preservar identificadores, proveniência, referência bibliográfica, ortografia de origem, participantes, data e estado de validação.

## Página pública e repositório

- Página do projeto: https://languagestructure.github.io/Corpus_Xavante/
- Código e versões: https://github.com/LanguageStructure/Corpus_Xavante
- Histórico de alterações: [CHANGELOG.md](CHANGELOG.md)

## Citação e DOI

Gerardi, Fabrício Ferraz; Toribio, Luas; Roksandic, Yvan. 2026. *Corpus Xavante (CorXav)*. Versão 0.2.0. Repositório de pesquisa.

**DOI da versão 0.1:** https://doi.org/10.5281/zenodo.23244728

**DOI da versão 0.2.0:** https://doi.org/10.5281/zenodo.23457736

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23457736.svg)](https://doi.org/10.5281/zenodo.23457736)

## Licenciamento e responsabilidades

A distribuição de textos e materiais deve respeitar autoria, direitos e autorizações pertinentes. A autorização de publicação das sete narrativas foi confirmada para esta etapa do projeto; isso não implica automaticamente licença aberta irrestrita para todo o acervo. Licenças de software e condições de reutilização dos dados devem ser definidas separadamente.

A versão 0.2.0 é uma **versão de desenvolvimento**. Os materiais permanecem sujeitos a correções e validação linguística.
