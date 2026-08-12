# Ontology Mapping Service (OXO)

The European Bioinformatics Institute (EBI) published the Ontology Mapping
Service (OXO) in [2019](https://doi.org/10.1016/j.drudis.2019.05.020) as an
interactive browser of mappings extracted from ontologies listed in the EBI's
Ontology Lookup Service (OLS). At the time of publication, this was limited to
[OBO Foundry ontologies](https://obofoundry.org/), which mostly used imprecise
`oboInOwl:hasDbXref` mappings.

The successor project OXO2 ([homepage](https://wwwdev.ebi.ac.uk/oxo2/);
[GitHub](https://github.com/EBISPOT/OXO2);
[preprint](https://arxiv.org/abs/2506.04286)) is built using the
[Simple Standard for Sharing Ontological Mappings (SSSOM)](https://mapping-commons.github.io/sssom/)
as a data model. It includes additional semantic mappings beyond OBO Foundry
ontologies such as those listed in the
[Mapping Commons Registry](https://mapping-commons.github.io). It additionally
generates inferred semantic mappings partially based on the inference rules
developed for the
[Semantic Mapping Assembler and Reasoner (SeMRA)](../tools/semra.md) that were
later codified in the
[SSSOM specification](https://mapping-commons.github.io/sssom/dev/chaining-rules/).

OXO2 is a static resource - it doesn't have mechanisms for adding new mappings
nor reviewing existing mappings. It's also not a user/developer-facing tool for
making new inferences. It has search capability based on term label or
identifier and filtering based on source/target ontology, mapping set, or
predicate type. It displays mappings in a tabular way, but does not have
graph-based visualization nor exploration.

OXO2 is primarily maintained by
[Henriette Harmse](https://github.com/henrietteharmse) with nearly all recent
commits assisted by Anthropic's Claude.
