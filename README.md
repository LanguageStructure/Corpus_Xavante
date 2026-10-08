# Corpus Xavante (CorXav)

Corpus textual e linguístico da língua xavante (A'uwẽ), desenvolvido para documentação, pesquisa linguística e produção de recursos digitais.

**Autores:** Fabrício Ferraz Gerardi · Luas Toribio · Yvan Roksandic

## Objetivos

O CorXav reúne textos com proveniência documentada e permite acrescentar traduções, segmentação, análises morfológicas e anotações sintáticas progressivamente. Diferentemente do [Corpus Bororo](https://github.com/LanguageStructure/Bororo-Corpus), **a inclusão de textos não depende de anotação CoNLL-U**.

## Princípios

- Preservar o texto original e registrar sua fonte, versão, ortografia e condições de uso.
- Atribuir identificadores persistentes a documentos e segmentos.
- Manter separadas as camadas de texto, tradução, segmentação, glosas e análise UD.
- Registrar o estado de revisão de cada camada; não apresentar anotações automáticas como validadas.
- Respeitar autoria indígena, consentimento e restrições de acesso determinadas pelos detentores dos materiais.
- Publicar apenas materiais cuja divulgação esteja autorizada.

## Organização

```text
Corpus_Xavante/
├── README.md
├── metadata/
│   └── README.md
├── sources/
│   └── README.md
├── texts/
│   └── README.md
├── translations/
│   └── README.md
├── annotations/
│   └── README.md
└── ud/
    └── README.md
```

## Fluxo de trabalho

1. Identificar a fonte, os participantes, os direitos e a autorização de uso.
2. Registrar o documento original sem alterar seu conteúdo.
3. Preparar texto digital e segmentação com identificadores estáveis.
4. Alinhar traduções quando disponíveis.
5. Adicionar análises linguísticas em arquivos separados, com indicação de autoria e revisão.
6. Exportar subconjuntos adequados para CoNLL-U / Universal Dependencies, sem exigir que todo o corpus esteja anotado.

## Estado do projeto

**Fase inicial (2026).** A infraestrutura está em preparação; não há estatísticas ou cobertura de anotação publicadas nesta versão.

## Citação e licença

Citação provisória: Gerardi, Fabrício Ferraz; Toribio, Luas; Roksandic, Yvan. *Corpus Xavante (CorXav)*. Repositório de pesquisa, 2026.

A licença de código e as condições de distribuição dos dados serão definidas separadamente, conforme a proveniência e as autorizações específicas. A presença de um arquivo no repositório não implica permissão para redistribuição irrestrita.

## Contato e contribuições

Contribuições de textos e correções devem incluir a fonte e a situação de autorização. Discussões metodológicas podem ser abertas nas Issues do repositório.
