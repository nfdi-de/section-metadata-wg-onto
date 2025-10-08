<a id="_5l7hdhn1spdj"></a>2023\-03\-28 \- WG Ontology Mapping & Harmonisation

**Date & Time**: 2023\-03\-28 \- 11:00 \- 12:00 CET

**Meeting Link:**

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88)

**Ressources:**

- Link to GDrive workspace:
  [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH)
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)

**Main Topic:**

- CIDOC\-CRM
- i\-adopt ontology
- WG outreach \- 1st Conference on Research Data Infrastructure
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=1839424810)

# <a id="_4in35gwl6myp"></a>Participants

- Jakob Vo�\(NFDI4Objects\)
- Philip Str�mert \(NFDI4Chem/TIB\)
- Hendrik Borgelt \(NFDI4Cat\)
- Naouel Karam \(NFDI4Biodiv\)
- Alexander Wolodkin \(NFDI4Earth, SGN\)
- Dorothea Iglezakis \(NFDI4Ing, MaRDI\)
- Amir Laadhar \(NFDI\-MatWerk\)
- Noemi Betancort \(KonsortSWD, Uni Bremen\)
- Alexander Behr \(NFDI4Cat\)
- Luca Ghiringhelli \(FAIRmat, HU Berlin\)
- Tillmann Fischer \(IPB, NFDI4Chem\)

# <a id="_3cakx2qk2ogo"></a>Agenda

**discussed aspect of main topic**

**prepared or present by **

short intro to CIDOC\-CRM

Jakob Vo�

1st Conference on Research Data Infrastructure

Philip Str�mert

i\-adopt ontology

Philip Str�mert

# <a id="_71znd1hi3viy"></a>Notes

## <a id="_lok4cw79ya3c"></a>CIDOC\-CRM

- Introduction Slides at
  [https://doi\.org/10\.5281/zenodo\.7777399](https://doi.org/10.5281/zenodo.7777399)
- Full specification in HTML at
  [https://cidoc\-crm\.org/html/cidoc_crm_v7\.1\.2_with_translations\.html](https://cidoc-crm.org/html/cidoc_crm_v7.1.2_with_translations.html)
- has a long history dating back to the mid nineties
  - predates standards like: Dublin Core, XML and RDF
  - but has encodings in RDF and XML
- Aims to model data from museums: originates in the museum communities to
  describe their artefacts and data about artefacts to be shared
- domain\-specific extension for scientific observations
  - [https://www\.cidoc\-crm\.org/collaborations](https://www.cidoc-crm.org/collaborations)
    list the extensions
- In practical use usually some DB specific schema fields are mapped/aligned to
  CIDOC\-CRM classes
- use case:
  [LIDO](https://cidoc.mini.icom.museum/working-groups/lido/lido-overview/about-lido/what-is-lido/)
  \-> allowing harvesting of museum objects/catalogs
- CRMact \(model for activity plan\) looks similar to what other ontologies
  model for i\.e\. in natural or life sciences
- modeling patterns: CIDOC\-CRM is event based, meaning that certain classes are
  defined according to whether they are being an event
- open questions
  - Are there any mappings between CIDOC\-CRM and other TLOs?
    - we need to ask the CIDOC IG
  - Possible use cases for NFDI?
    - already used in NFDI4Culture and NFDI4Objects\. Activities wrt to mappings
      already ongoing?
- interoperability aspect \- often institutions use it to broadly map their
  internal schemas
  - this means a direct translation/transformation between data from one source
    to another is often not possible, and a more specific mapping has to be done
    to do direct data
- chat comment by Noemi Betancort:  
  here examples of the use of CIDOC\-CRM in Wikibase instances
  [https://link\.springer\.com/chapter/10\.1007/978\-3\-031\-15743\-1_49](https://link.springer.com/chapter/10.1007/978-3-031-15743-1_49)
  or
  [https://swib\.org/swib21/slides/05\-03\-gayo\.pdf](https://swib.org/swib21/slides/05-03-gayo.pdf)
  \(i have heard about the use of CIDOC\-CRM for modelling Wikibase Instances,
  but I dont know more details\) \- sorry, I was searching for this information
  before and I found it now that we changed the topic

## <a id="_wlu1gsbrixt5"></a>1st Conference on Research Data Infrastructure

- [https://www\.nfdi\.de/cordi\-2023\-call\-for\-papers/](https://www.nfdi.de/cordi-2023-call-for-papers/)
  - Extended Abstracts with up to 1\.000 words due: April 21, 2023
  - **Harmonising RDM**: This track is about \(meta\-\)data, terminologies and
    provenance and how research data management can be harmonised on a broad
    basis across organisations and disciplines\.
- might be a good outlet to present our WG, its goals and such?

## <a id="_rnehgcfdhxq2"></a>i\-adopt ontology

- was presented at RDA 20th Plenary Meeting \- Gothenburg \(Hybrid\)
- [https://i\-adopt\.github\.io/index\.html](https://i-adopt.github.io/index.html)
- [https://github\.com/i\-adopt](https://github.com/i-adopt)
- List of compiled terminologies:
  [https://i\-adopt\.github\.io/terminologies/list/all](https://i-adopt.github.io/terminologies/list/all)
- Does anyone use this, or is involved in it?
  - Naouel Karam: NFDI4Biodiversity is involved, to describe complex variables\.
  - Structure observable properties on a very broad level, connects to other
    ontologies on a the more detail level \(for properties, units, constraints
    for instance\)
- How can we make use of this?
- Similarity with DDI\-CDI \(Data Documentation Initiative, Cross Domain
  Integration\) for representing variables \(at a conceptual and instantiated
  level\) in datasets with the possibility to use external ontologies:
  - [https://ddialliance\.org/Specification/ddi\-cdi](https://ddialliance.org/Specification/ddi-cdi)
  - The Role of DDI\-CDI in EOSC
    [https://www\.fairsfair\.eu/news/role\-ddi\-cdi\-eosc\-possible\-uses\-and\-applications](https://www.fairsfair.eu/news/role-ddi-cdi-eosc-possible-uses-and-applications)
    \-> here the recording describing the role of this specification at he EOSC
    [https://codata\.org/initiatives/decadal\-programme2/ddi\-cross\-domain\-integration/ddi\-cdi\-and\-eosc/](https://codata.org/initiatives/decadal-programme2/ddi-cross-domain-integration/ddi-cdi-and-eosc/)
  - more information and useful webinars, like Data Processing and Provenance in
    DDI\-CDI
    [https://codata\.org/initiatives/decadal\-programme2/ddi\-cross\-domain\-integration/](https://codata.org/initiatives/decadal-programme2/ddi-cross-domain-integration/)

<a id="_29tb5w1tte9o"></a>## [Used Ontologies @
NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit"
\l "gid=1839424810)

- Does our TLO mapping draft make sense / is it useful?
- What other resources are there that have already made mappings between TLOs?
  - from the OntoCommons project
    - [OntoC_D2\.4_final\.pdf](https://drive.google.com/file/d/1kuLR4ViG-RVt57kVKCl73UVS0wHnLj_s/view?usp=share_link)
      � Common Logic mapping between DOLCE & BFO
    - [From Causation \(and Parthood\) to Time the Case of EMMO\.pdf](https://drive.google.com/file/d/1AGT_6Duf4m8q-9e59CrSn-1TxESaC2wO/view?usp=share_link)
      - partial Common Logic mapping between EMMO and DOLCE
