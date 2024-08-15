# About
This folder is meant to be used to store examples files from each NFDI consortium in either JSON-LD or TTL that are 
conform to [CDIF](https://cross-domain-interoperability-framework.github.io/cdifbook/). The content of these files should be a knowledge graph that contains the necessary
domain-independent metadata of a dataset (e.g. author, date, ...) as well as domain-specific metadata (e.g. used 
observation method/tools, ...).

In our [14-08-2024 call](https://docs.google.com/document/d/14z6kuAdVaiflWUtjqk3LKt-hqg_DeaRCpLY7TFo1PoU), we 
discussed the  [Discovery Profile](https://cross-domain-interoperability-framework.github.
io/cdifbook/metadata/discovery.html) and the [Data Integration Profile](https://cross-domain-interoperability-framework.github.io/cdifbook/data_integration/dataintegrationintro.html) and 
although the former is a necessary prerequisite, it is the latter we are interested in testing here with examples. 

# File naming conventions
Please use the following file naming convention:

```
[ConsortiumAcronym]_CDIF_ex_[integer].[ttl/jsonld] 
example: NFDI4Chem_CDIF_ex_1.ttl
```