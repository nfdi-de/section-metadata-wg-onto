# Mapping Tools

The goal of this document is to highlight recommended mapping tools. A mapping
tool is a reusable workflow that can be used to predict, review, curate, or
reason over semantic mappings.

The goal of this document isn't highlight mapping formats like SSSOM, JSKOS,
etc. nor software that simply implements object models and I/O for the formats.

## Biomappings

Biomappings (https://github.com/biopragmatics/biomappings) is an open source
project that has a few parts:

1. A simple Python-based workflow for generating lexical mappings between
   ontologies, controlled vocabularies, and any other resource that mints
   identifiers
2. A web-based curation tool for manually reviewing predicted mappings
3. A workflow for publishing all generated + curated mappings in SSSOM, with
   detailed provenance information

### Artifacts

Mappings that are curated in the Biomappings project are stored in SSSOM under
version control in the GitHub repository. They can be accessed through this
PURL: https://w3id.org/biopragmatics/biomappings/sssom/biomappings.sssom.tsv

### Training Material

1. [Improving ontology interoperability with Biomappings (video; 1 hour)](https://www.youtube.com/watch?v=_gAdGShZReo&pp=ygULYmlvbWFwcGluZ3M%3D)
2. [How To Curate Biomappings (video; 5 minutes)](https://www.youtube.com/watch?v=shZ4OpRInF0&pp=ygULYmlvbWFwcGluZ3M%3D)
3. [Curating Semantic Mappings with Biomappings (OBook)](https://oboacademy.github.io/obook/tutorial/biomappings)

### Publications

- https://doi.org/10.1093/bioinformatics/btad130

## Semantic Reasoning Assembler and Mapper (SeMRA)

The Semantic Mapping Reasoner and Assembler (SeMRA;
https://github.com/biopragmatics/semra) is an open source Python package that
provides:

1. An object model for semantic mappings (based on SSSOM)
2. Functionality for assembling and reasoning over semantic mappings at scale
3. A provenance model for automatically generated mappings
4. A confidence model granular at the curator-level, mapping set-level, and
   community feedback-level

### Artifacts

SeMRA was used to assemble a large-scale database of raw semantic mappings from
hundreds of ontologies and databases in SSSOM:
https://doi.org/10.5281/zenodo.11082038. This is periodically refreshed and can
be rebuilt locally with `semra build`.

Domain-specific mapping assemblies listed
[here](https://semra.readthedocs.io/en/latest/artifacts.html)

### Training Material

- [documentation and tutorials](https://semra.readthedocs.io)

### Publications

- https://doi.org/10.1093/bioinformatics/btaf542
