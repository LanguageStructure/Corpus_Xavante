# Corpus Xavante (CorXav)

Corpus textual e linguístico da língua xavante (A'uwẽ), voltado à documentação, à pesquisa linguística e à produção de recursos digitais, com revisão e tradução em colaboração com falantes.

**Autores do projeto:** Fabrício Ferraz Gerardi · Luas Toribio · Yvan Roksandic.

## Versão 0.1 — versão inicial de trabalho

Esta versão documenta a estrutura inicial do corpus e o fluxo de edição. **Não representa uma edição linguística validada nem a publicação irrestrita dos textos.** A disponibilização pública de cada documento depende da verificação de autoria, direitos e autorização de uso.

## Materiais e fluxo de trabalho

- **Meu Mundo:** conjunto de textos trabalhados em paralelo, com campos em xavante e português.
- **A'uwe na Rowatsu'u 1** (Jerônimo Tsawê, 2005, 2ª edição experimental): fonte monolíngue em preparação para revisão do xavante e tradução com falante nativo. O texto extraído automaticamente exige conferência com o original.
- **A'uwe na Rowatsu'u 2** (Jerônimo Tsawê, 2005, 2ª edição experimental, Editora UCDB): fonte catalogada para extração, revisão e tradução progressivas. Os dois volumes constam em `metadata/rowatsuu-catalog.json`.
- **Editor local:** duas colunas editáveis. O campo português pode começar vazio, com placeholder visual; textos parcialmente traduzidos podem ser salvos. O original deve ser preservado separadamente da versão corrigida.
- **Busca e revisão:** ocorrências devem ser inspecionáveis antes de substituições, com backups das edições.

A inclusão de documentos **não depende** de análise CoNLL-U. Traduções, segmentação, glosas, morfologia e análise UD são camadas incrementais e independentes.

## Estrutura do repositório

```text
Corpus_Xavante/
├── README.md
├── docs/                  # página informativa, sem textos restritos
├── metadata/
├── sources/
├── texts/
├── translations/
├── annotations/
└── ud/
```

Os diretórios `data/` e `data/parallel/`, quando presentes em instalações de trabalho, podem conter arquivos de edição; sua presença não implica autorização para publicação.

## Princípios de documentação

1. Registrar proveniência, referência bibliográfica, autoria, ortografia, versão e condições de acesso.
2. Preservar fontes e extrações originais, distinguindo-as de correções humanas.
3. Permitir revisão do xavante e tradução portuguesa progressivas, inclusive com campos vazios.
4. Registrar revisores, datas e estado de validação, sem apresentar resultados automáticos como revisados.
5. Manter separadas as camadas textual, tradutória e linguística.
6. Respeitar decisões dos autores e das comunidades quanto ao acesso e à redistribuição.

## Página do projeto

**Site público (GitHub Pages):** https://languagestructure.github.io/Corpus_Xavante/

O site é publicado a partir de `docs/index.html` e apresenta o projeto **sem reproduzir o conteúdo dos livros ou os dados de trabalho**.

## Citação

Gerardi, Fabrício Ferraz; Toribio, Luas; Roksandic, Yvan. 2026. *Corpus Xavante (CorXav)*. Versão 0.1. Repositório de pesquisa.

**DOI da versão 0.1:** [10.5281/zenodo.23244728](https://doi.org/10.5281/zenodo.23244728).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23244728.svg)](https://doi.org/10.5281/zenodo.23244728)

## Licenciamento e acesso

Licenças de software e condições de distribuição dos dados devem ser tratadas separadamente. A versão 0.1 não atribui licença aberta aos textos por omissão. Não publique os materiais de origem ou suas transcrições antes de verificar os direitos e as autorizações pertinentes.

## Contribuições

Correções, traduções e anotações devem registrar a fonte, os participantes, a revisão e as condições de divulgação.
