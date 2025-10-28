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
| terminology              | either an ontology, thesaurus or controlled vocabulary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                              |
| TLO / Top-Level Ontology | In information science, an upper ontology (also known as a top-level ontology, upper model, or foundation ontology) is an ontology that consists of very general terms (such as "object", "property", "relation") that are common across all domains. An important function of an upper ontology is to support broad semantic interoperability among a large number of domain-specific ontologies by providing a common starting point for the formulation of definitions. Terms in the domain ontology are ranked under the terms in the upper ontology, e.g., the upper ontology classes are superclasses or supersets of all the classes in the domain ontologies. | https://en.wikipedia.org/wiki/Upper_ontology |
| MLO / mid-level ontology |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                              |
| domain-level ontology    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                              |
| thesaurus                | thesaurus (pl.: thesauri or thesauruses), sometimes called a synonym dictionary or dictionary of synonyms, is a reference work which arranges words by their meanings (or in simpler terms, a book where one can find different words with similar meanings to other words), sometimes as a hierarchy of broader and narrower terms, sometimes simply as lists of synonyms and antonyms.                                                                                                                                                                                                                                                                              | https://en.wikipedia.org/wiki/Thesaurus      |

## NFDI Terminology Principles

**Editor Note:** The idea is to have something similar to the
[OBO Foundry Principles](https://obofoundry.org/principles/) here that should be
guidance to all terminology development projects within the NFDI as common best
practices. Hence, adding these OBO Foundry principles verbatim is just a
temporary placeholder. And it is expected to be discussed which ones we can
reuse verbatim and which ones we need to adjust for our NFDI context.

1. **Open** - The ontology MUST be openly available to be used by all without
   any constraint other than (a) its origin must be acknowledged and (b) it is
   not to be altered and subsequently redistributed in altered form under the
   original name or with the same identifiers.
2. **Common Format** - The ontology is made available in a common formal
   language in an accepted concrete syntax.
3. **URI/Identifier Space** - Each ontology MUST have a unique IRI in the form
   of an OBO Foundry permanent URL (PURL).
4. **Versioning** - The ontology provider has documented procedures for
   versioning the ontology, and different versions of ontology are marked,
   stored, and officially released.
5. **Scope** - The scope of an ontology is the extent of the domain or subject
   matter it intends to cover. The ontology must have a clearly specified scope
   and content that adheres to that scope.
6. **Textual Definitions** - The ontology has textual definitions for the
   majority of its classes and for top level terms in particular.
7. **Relations** - Relations should be reused from the BFO2020 or Relations
   Ontology (RO).
   - @StroemPhi: Might be changed to only BFO2020, if we can agree to a BFO2020
     only setup when the NFDIcore will serve as common TLO/MLO backbone.
     Currently, I doubt this to be feasable, as my ontologies are expected to be
     fully OBO compatible modules. But once we have a BFO 2020-RO bridge and
     conversion pipeline this should be possible. SeeAlso:
     https://github.com/obi-ontology/obi/issues/1880
8. **Documentation** - The owners of the ontology should strive to provide as
   much documentation as possible.
9. **Documented Plurality of Users** - The ontology developers should document
   that the ontology is used by multiple independent people or organizations.
10. **Commitment To Collaboration** - OBO Foundry ontology development, in
    common with many other standards-oriented scientific activities, should be
    carried out in a collaborative fashion.7
11. **Locus of Authority** - There should be a person who is responsible for
    communications between the community and the ontology developers, for
    communicating with the Foundry on all Foundry-related matters, for mediating
    discussions involving maintenance in the light of scientific advance, and
    for ensuring that all user feedback is addressed.
12. **Naming Conventions** - The names (primary labels) for elements (classes,
    properties, etc.) in an ontology must be intelligible to scientists and
    amenable to natural language processing. Primary labels should be unique
    among OBO Library ontologies.
13. **Notification of Changes** - Ontologies SHOULD announce major changes to
    relevant stakeholders and collaborators ahead of release.
14. **Maintenance** - The ontology needs to reflect changes in scientific
    consensus to remain accurate over time.
15. **Term Stability** - The definition of a term MUST always denote the same
    thing(s)–known as “referent(s)”–in reality. If a proposed change to the
    definition would substantially change its referents, then a new term with
    new IRI and definition MUST instead be created.
16. **Responsiveness** - Ontology developers MUST offer channels for community
    participation and SHOULD be responsive to requests.

## Term Reuse

A general best practise in terminology development is to not reinvent the wheel
and rather reuse already existing terminologies whenever possible. There already
exists a multitude for different purposes, e.g. simple controlled vocabularies
(often in from of SKOS Thesauri) to elaborate OWL Ontologies. Hence, one should
use terminology look-up services and registries to research and evaluate such
existing terminologies before and while developing a new terminology.

### Top-Level Ontology Reuse

- needed as a common foundation when developing OWL ontologies

#### Currently used TLOs in NFDI:

- [BFO v2.0 classes only version](https://terminology.tib.eu/ts/ontologies/bfo) -
  used in: NFDI4Chem, ...
  - standard TLO in the OBO Foundry along with the Relation Ontology (RO)
- [BFO 2020](https://github.com/BFO-ontology/BFO-2020) - used in:
  [NFDIcore Ontology](https://ise-fizkarlsruhe.github.io/nfdicore/)
- [CIDOC CRM 7.1.3](https://cidoc-crm.org/Version/version-7.1.3) - used in
  NFDI4Objects

### Mid-Level Ontology Term Reuse

### Other terminologies

## Terminology Hosting & Indexing

- addresses Principle 1-6 & 8-11
- a terminology developed within NFDI
  - MUST
    - be indexed in the TS4NFDI
    -
  - SHOULD
    - adhere to a minimal metadata standard
      - see MOD

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
