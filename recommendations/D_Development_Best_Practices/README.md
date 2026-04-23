# Objective D - NFDI’s Best Practices for Terminology Development and Publishing

GitHub Epic: https://github.com/nfdi-de/section-metadata-wg-onto/issues/31

## Target audience

The present recommendation is mainly addressed to developers of terminologies,
such as OWL ontologies or SKOS thesauri, within NFDI. However, its wording is
also aimed to be intelligible for domain experts, who are collaborating with
these developers.

## Existing resources

- https://obofoundry.org/principles/
- https://oboacademy.github.io/obook/
- https://cthoyt.com/2020/05/12/building-an-ontology.html
- http://www.ontologydesignpatterns.org/
- Seppälä, S., Ruttenberg, A., & Smith, B. (2017). Guidelines for writing
  definitions in ontologies. Ciência Da Informação, 46(1). retrieved via
  https://philpapers.org/archive/SEPGFW.pdf
- Chris Mungall. (2019) OntoTip: Write simple, concise, clear, operational
  textual definitions.
  https://douroucouli.wordpress.com/2019/07/08/ontotip-write-simple-concise-clear-operational-textual-definitions/
- Arp, R., Smith, B., & Spear, A. D. (2015). Building Ontologies with Basic
  Formal Ontology. The MIT Press. ISBN:9780262527811

## Glossary

**Editor Note:** We might want to outsource this glossary to a different
page/doc, as I imagine this to come in handy also in other docs we'll write,
e.g.
https://github.com/nfdi-de/section-metadata-wg-onto/pull/28/commits/38410712b3c82a9bbe9b9ad5a5c172b8bcc20504

| Term                     | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | further reading/sources                      |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| terminology              | either an ontology, thesaurus, or controlled vocabulary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                              |
| top-level ontology (TLO) | In information science, an upper ontology (also known as a top-level ontology, upper model, or foundation ontology) is an ontology that consists of very general terms (such as "object", "property", "relation") that are common across all domains. An important function of an upper ontology is to support broad semantic interoperability among a large number of domain-specific ontologies by providing a common starting point for the formulation of definitions. Terms in the domain ontology are ranked under the terms in the upper ontology, e.g., the upper ontology classes are superclasses or supersets of all the classes in the domain ontologies. | https://en.wikipedia.org/wiki/Upper_ontology |
| mid-level ontology (MLO) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                              |
| domain-level ontology    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                              |
| thesaurus                | thesaurus (pl.: thesauri or thesauruses), sometimes called a synonym dictionary or dictionary of synonyms, is a reference work which arranges words by their meanings (or in simpler terms, a book where one can find different words with similar meanings to other words), sometimes as a hierarchy of broader and narrower terms, sometimes simply as lists of synonyms and antonyms.                                                                                                                                                                                                                                                                              | https://en.wikipedia.org/wiki/Thesaurus      |

## NFDI Terminology Principles

0. **No isolation** – The terminology must be developed in such a way that it
   will integrate itself nicely within the larger landscape of other
   terminologies already used in the field or in related fields.
   - In particular, if a field has already established guidelines or principles
     for the development or maintenance of terminologies, a new terminology
     developed within the context of NFDI would be expected to follow them.
   - One field that does already have established principles for terminology
     development is the biological and biomedical field, where most projects
     follow the [OBO Foundry Principles](https://obofoundry.org/principles/). In
     fact the following guidelines below are, for the most part, directly
     inspired from the OBO Foundry Principles.
   - In the absence of established guidelines in a given field, a good place to
     start would be to look at existing ontologies in the field. The NFDI
     collections in the
     [Semantic Farm](https://semantic.farm/collection/?ror=05qj6w324) can be
     used to explore those.
1. **Open** - The terminology must be openly available to be used by all without
   any constraint other than (a) its origin must be acknowledged and (b) it is
   not to be altered and subsequently redistributed in altered form under the
   original name or with the same identifiers.
   - OBO Foundry principle #1
2. **Common Format** - The terminology must be available in a common formal
   language in an accepted concrete syntax.
   - OBO Foundry principle #2
3. **URI/Identifier Space** - Each terminology must have a unique IRI that
   identifies it. All entities defined within the terminology (not including
   entities imported from other terminologies) must have a unique IRI within a
   single namespace, which is ideally derived from the terminology’s own IRI.
   The terminology IRI must resolve to a machine-readable version of the
   terminology (in a format suitable according to Principle 2).
   - Derived from OBO Foundry principle #3, without the additional OBO-specific
     requirement that all IRIs must be under the
     `http://purl.obolibrary.org/obo/` namespace.
   - It is furthermore recommended that IRIs be minted according to a consistent
     policy, which should be documented. The
     [McMurry et al. (2017)](https://doi.org/10.1371/journal.pbio.2001414) paper
     is a good starting point to devise such a consistent policy.
4. **Versioning** - The terminology provider has documented procedures for
   versioning the terminology, and different versions of the terminology are
   marked, stored, and officially released.
   - OBO Foundry principle #4
5. **Scope** - The scope of a terminology is the extent of the domain or subject
   matter it intends to cover. The terminology must have a clearly specified
   scope and content that adheres to that scope.
   - OBO Foundry principle #5
6. **Textual Definitions** - The terminology has textual definitions for the
   majority of its classes and for top level terms in particular.
   - OBO Foundry principle #6. Of note, the implementation guidelines of the
     foundry stipulate that the definitions must be provided as
     [IAO:0000115](http://purl.obolibrary.org/obo/IAO_0000115) annotations; that
     particular requirement may be ignored for ontologies that are not expected
     to fit within the set of OBO ontologies. However, the point stands that a
     commonly agreed upon annotation property should be used to provide the
     definitions – if not IAO:0000115, then maybe
     [skos:definition](http://www.w3.org/2004/02/skos/core#definition).
   - It is furthermore recommended that definitions be annotated with source
     informations.
7. **Consistent use of relations and annotations** – The terminology should use
   relations (object properties) ideally coming from a single unified source,
   that is commonly used by other terminologies of the field. Likewise for
   annotation properties.
   - This is derived from OBO Foundry Principle #7, which mandates the use of
     relation from OBO’s Relation Ontology (RO), but RO might not be suitable
     for all terminologies outside of OBO.
8. **Documentation** - The owners of the terminology should strive to provide as
   much documentation as possible.
   - OBO Foundry principle #8
9. **Commitment To Collaboration** - Terminology development, in common with
   many other standards-oriented scientific activities, should be carried out in
   a collaborative fashion.
   - OBO Foundry principle #10
10. **Locus of Authority** - There should be a person or group of persons who is
    responsible for communications between the community and the ontology
    developers, for mediating discussions involving maintenance of the ontology
    in the light of scientific advance, and for ensuring that all user feedback
    is addressed.
    - Derived from OBO Foundry principle #11, without requiring that there
      should always be _one person_ (instead of a _group_) acting as the locus
      of authority, and without the OBO-specific requirement that this person
      should be in charge of all communications with the foundry.
11. **Naming Conventions** - The names (primary labels) for elements (classes,
    properties, etc.) in a terminology must be intelligible to scientists and
    amenable to natural language processing. Primary labels should be unique
    within the terminology.
    - Derived from OBO Foundry principle #12, without the OBO-specific
      requirement that primary labels should be unique among all OBO ontologies.
    - As for definitions, a commonly agreed upon annotation property should be
      consistently used to provide the labels. Common properties for that
      purpose are [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) and
      [skos:prefLabel](http://www.w3.org/2004/02/skos/core#prefLabel).
12. **Notification of Changes** - Terminologies should announce major changes to
    relevant stakeholders and collaborators ahead of release.
    - OBO Foundry principle #13
13. **Maintenance** - The terminology needs to reflect changes in scientific
    consensus to remain accurate over time.
    - OBO Foundry principle #16
14. **Term Stability** - The definition of a term must always denote the same
    thing(s)–known as “referent(s)”–in reality. If a proposed change to the
    definition would substantially change its referents, then a new term with
    new IRI and definition must instead be created.
    - OBO Foundry principle #19
15. **Responsiveness** - Terminology developers must offer channels for
    community participation and SHOULD be responsive to requests.
    - OBO Foundry principle #20

## Term Reuse

A general best practise in terminology development is to not reinvent the wheel
and rather reuse already existing terminologies whenever possible. There already
exists a multitude for different purposes, e.g. simple controlled vocabularies
(often in from of SKOS Thesauri) to elaborate OWL Ontologies. Hence, one should
use terminology look-up services and registries to research and evaluate such
existing terminologies before and while developing a new terminology.

### Top-Level Ontology (TLO) Reuse

- needed as a common foundation when developing OWL ontologies

#### Currently used Top-Level Ontologies (TLOs) in NFDI:

- [BFO v2.0 classes only version](https://terminology.tib.eu/ts/ontologies/bfo) -
  used in: NFDI4Chem, ...
  - standard TLO in the OBO Foundry along with the Relation Ontology (RO)
- [BFO 2020](https://github.com/BFO-ontology/BFO-2020) - used in:
  [NFDIcore Ontology](https://ise-fizkarlsruhe.github.io/nfdicore/)
- [CIDOC CRM 7.1.3](https://cidoc-crm.org/Version/version-7.1.3) - used in
  NFDI4Objects

### Mid-Level Ontology (MLO) Term Reuse

### Other terminologies

- [LIDO](https://cidoc.mini.icom.museum/working-groups/lido/lido-overview/about-lido/what-is-lido/) -
  used in NFDI4Objects and NFDI4Culture

## Terminology Hosting and Indexing

- addresses Principle 1-6 & 8-11
- a terminology developed within NFDI
  - MUST
    - be indexed in Semantic Farm
    - be indexed in the TS4NFDI
  - SHOULD
    - adhere to a minimal metadata standard
      - see Metadata for Ontology Description (MOD)

See [Semantic Farm and BARTOC](semantic-farm-and-bartoc.md) for discussion of
recommendations for indexing

## Tooling

### Ontology Development Kit (ODK)

- https://github.com/INCATools/ontology-development-kit
- tutorials & how-tos in the OBOOK
  - https://oboacademy.github.io/obook/howto/odk-setup/
  - https://oboacademy.github.io/obook/howto/odk-update/
  - https://oboacademy.github.io/obook/howto/odk-create-repo/
  - https://oboacademy.github.io/obook/howto/odk-migrate-to-odk/
- NFDI consortia already using ODK: NFDIcore, Matwerk, 4Culture, 4Memory,
  4DataScience, 4Chem
- PROs
- CONs

### WIDOCO

### ROBOT

### PROTÈGÈ

### WIKIBASE

## Quality Assurance

- [OntoClean](https://doi.org/10.1007/978-3-540-24750-0_8)
- [PoolParty](https://help.poolparty.biz/en/user-guide-for-knowledge-engineers/advanced-features/quality-management-in-poolparty.html)
  (Consistency Checker for SKOS)
- [qSKOS](https://github.com/cmader/qSKOS)
- [SKOSify](https://github.com/NatLibFi/Skosify)
