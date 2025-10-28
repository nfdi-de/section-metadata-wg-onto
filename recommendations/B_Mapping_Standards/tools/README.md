# Mapping Tools

The goal of this document is to highlight recommended mapping tools. A mapping
tool is a reusable workflow that can be used to predict, review, curate, or
reason over semantic mappings.

The goal of this document isn't highlight mapping formats like SSSOM, JSKOS,
etc. nor software that simply implements object models and I/O for the formats.

| Name                                                        | Description                                                    |
|-------------------------------------------------------------|----------------------------------------------------------------|
| [SSSOM Curator](sssom-curator.md)                           | Lexical prediction of semantic mappings and curation interface |
| [Semantic Mapping Reasoner and Assembler (SeMRA)](semra.md) | Reasoning-based prediction of semantic mappings                |
## Recommendations if You're Developing a Mapping Tool

GitHub Epic: https://github.com/nfdi-de/section-metadata-wg-onto/issues/64

1. Try and avoid being project specific or domain specific, i.e., don't add NFDI in the name or "bio"- in the name, to
   avoid alienating people from other communities or domains
