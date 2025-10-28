# Mapping Tools

The goal of this folder is to highlight mapping tools, i.e., concrete
implementations of reusable workflows that can be used to predict, review,
curate, or reason over semantic mappings.

The goal of this folder isn't to highlight mapping formats like SSSOM, JSKOS,
etc. nor software that simply implements object models and I/O for the formats.

| Name                                                        | Description                                                    |
| ----------------------------------------------------------- | -------------------------------------------------------------- |
| [SSSOM Curator](sssom-curator.md)                           | Lexical prediction of semantic mappings and curation interface |
| [Semantic Mapping Reasoner and Assembler (SeMRA)](semra.md) | Reasoning-based prediction of semantic mappings                |

## Contributing

You should make a new markdown file in this folder named by the tool/workflow.
Make the name lowercase with dashes instead of spaces.

Please include the following:

1. The full name and acronym (if appropriate) for the software
2. A high-level description of what the tool does and why
3. A link to its source code, freely available container, or freely available
   executable
4. Links to documentation and training materials
5. Links to publications about or using the workflow

Importantly, each of these should explicitly say how is the tool useful in the
main objective work for making sure the terminologies used throughout NFDI can
be linked, harmonized, mapped. How does this promote interoperability (in the
context of harmonizing our used terminologies) within NFDI.

## Recommendations if You're Developing a Mapping Tool

GitHub Epic: https://github.com/nfdi-de/section-metadata-wg-onto/issues/64

1. Try and avoid being project specific or domain specific, i.e., don't add NFDI
   in the name or "bio"- in the name, to avoid alienating people from other
   communities or domains
