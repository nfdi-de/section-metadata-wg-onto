# Objective C - NFDI-wide Collaboration on Use Cases

GitHub Epic: https://github.com/nfdi-de/section-metadata-wg-onto/issues/30

## Information about NFDICore ontology

- Github: [NFDICore ontology](https://github.com/ISE-FIZKarlsruhe/nfdicore)
- Documentation: https://ise-fizkarlsruhe.github.io/nfdicore/
- Discussions related to NFDICore should be done here:
  https://github.com/ISE-FIZKarlsruhe/nfdicore/discussions

## Available SPARQL endpoints

- [NFDI4Culture](https://nfdi4culture.de/sparql) (NFDICore ontology is used)
- [NFDI4Chem](https://search.nfdi4chem.de/sparql)
- [NFDI-MatWerk](https://nfdi.fiz-karlsruhe.de/matwerk/shmarql/) (NFDICore
  ontology is used)
- [NFDI4DataScience](https://nfdi.fiz-karlsruhe.de/4ds/sparql) (NFDICore
  ontology is used) here also a
  [SHMARQL endpoint](https://nfdi.fiz-karlsruhe.de/4ds/shmarql) is available
- [NFDI4Memory](https://nfdi.fiz-karlsruhe.de/4memory/shmarql/) provided using
  SHMARQL (NFDICore ontology is used)
- [NFDI4Bioimage](https://kg.nfdi4bioimage.de/#/) NFDICore ontology is used
- [NFDI4Earth](https://sparql.knowledgehub.nfdi4earth.de/)
- NFDI4Energy, see https://openenergyplatform.org/
- [MaRDI](https://query.portal.mardi4nfdi.de/)
- [NFDI4Microbiota](https://nfdi4microbiota.de/services/sparql_query/)
- [NFDI4Objects](https://graph.nfdi4objects.net/sparql)
- NFDI4Cat to be added
- FAIRMAT to be added
- NFDI4Ing to be added (https://ingest.nfdi4ing.de/api/v1/sparql)
- [GESIS KG](https://data.gesis.org/gesiskg/sparql) (NFDICore ontology is used)
- [ORKG](https://orkg.org/triplestore)
- [Chemotion KG](https://ditrare.ise.fiz-karlsruhe.de/chemotion-kg/shmarql/)
  provided using shmarql (NFDICore ontology is used)
- [Platform MaterialDigital - PMD KG](https://pmdkg.ise.fiz-karlsruhe.de/sparql)
- [KGI4NFDI Knowledge Graph Registry](https://kgi.services.base4nfdi.de/kg_registry/)
- to be completed ...

## Available Knowledge Graphs

The KGI4NFDI base service has a registry at
https://github.com/KGI4NFDI/kgi4nfdi_registry_data. Ideally all KGs used within
NFDI should be registered there.

## Use Case [1]: Bridging NFDI4Culture / NFDI4Chem Knowledge Graphs

See the
[blog post](https://cthoyt.com/2025/10/07/bridging-culture-and-chemistry.html)
by @cthoyt that has been inspired by an invited
[talk](https://zenodo.org/records/17127336) by Torsten Schrade (NFDI4Culture) at
the NFDI4Chem consortium's 6th meeting in Mainz.

What we can do by bridging the 4Chem knowledge graph and 4culture knowledge
graph? We can connect datasets in Chemotion electronic laboratory notebooks
(ELNs) that annotate the instrument used for generation with depictions of those
instruments in cultural heritage objects like paintings.

In sum the data journey described in the blog post does not work, but it depicts
where improvement is necessary, which might form the foundation for further
joint activities.

### Summary of useful links provided in the blog post:

- [Bioregistry](https://bioregistry.io/) is very helpful for resolving needed
  prefixes
- [PyOBO](https://github.com/biopragmatics/pyobo) is a library of reusable
  tooling to support ingesting new resources across domains in an ontology-like
  shape. It has been used in the present example to ingest
  [Iconclass](https://iconclass.org/) data, which appeared to be challenging.
- [Simple Standard for Sharing Ontological Mappings (SSSOM)](https://mapping-commons.github.io/sssom/)
  is a community standard for storing semantic mappings and giving access to
  standardized tooling for accessing, querying, and applying them.
- [Ubergraph](https://github.com/INCATools/ubergraph) is an RDF triplestore and
  public SPARQL query endpoint, which includes a novel approach to precomputing
  OWL inferences. Thus, it can be used for integrating OBO ontologies into a
  unified semantic graph, see: https://zenodo.org/records/7249759 for more
  information.
