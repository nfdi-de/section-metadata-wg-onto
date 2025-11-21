# Cross-Domain Interoperability Framework (CDIF)

This document gives some background on the CDIF Framework.

## CDIF

The framework is based on a set of five core profiles that address the most
important functions for cross-domain FAIR implementation.

- https://cross-domain-interoperability-framework.github.io/cdifbook/introduction.html

## CDIF Profiles

The framework is based on a set of five core profiles that address the most
important functions for cross-domain FAIR implementation.

Discovery (patterns for metadata content, serialization and publication)

Data access (documentation of access conditions and permitted use)

Controlled vocabularies (practices for the publication of controlled
vocabularies and semantic artefacts)

Data integration (documentation of the structural and semantic aspects of data
to make it integration-ready)

Universals (description of _universal_ elements – time, geography, and units of
measurement).

## Old Notes

This folder is meant to be used to store examples files from each NFDI
consortium in either JSON-LD or TTL that are conform to
[CDIF](https://cross-domain-interoperability-framework.github.io/cdifbook/). The
content of these files should be a knowledge graph that contains the necessary
domain-independent metadata of a dataset (e.g. author, date, ...) as well as
domain-specific metadata (e.g. used observation method/tools, ...).

In our
[2024-08-14 call](https://docs.google.com/document/d/14z6kuAdVaiflWUtjqk3LKt-hqg_DeaRCpLY7TFo1PoU),
we discussed the
[Discovery Profile](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/discovery.html)
and the
[Data Integration Profile](https://cross-domain-interoperability-framework.github.io/cdifbook/data_integration/dataintegrationintro.html)
and although the former is a necessary prerequisite, it is the latter we are
interested in testing here with examples.

### File naming conventions

Please use the following file naming convention:

```
[ConsortiumAcronym]_CDIF_ex_[integer].[ttl/jsonld]
example: NFDI4Chem_CDIF_ex_1.ttl
```
