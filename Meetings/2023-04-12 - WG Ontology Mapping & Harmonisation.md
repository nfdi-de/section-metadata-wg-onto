<a id="_5l7hdhn1spdj"></a>2023\-04\-12 \- WG Ontology Mapping & Harmonisation

**Date & Time**: 2023\-04\-12 \- 11:00\-12:00 CET

**Meeting Link:**

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88)

**Ressources:**

- Link to GDrive workspace:
  [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH)
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)

**Main Topic:**

- I\-ADOPT ontology used in NFDI4Biodiversity\.
  [Link to Slides](https://drive.google.com/file/d/1-6aSZ23tb9IBsmt3_yVNEGBGnAUPCcaE/view?usp=share_link)
- Why Mappings Matter and how to make them FAIR � A FAIR\-IMPACT Workshop
  **Online**, **13 April 2023 **
  - [https://fair\-impact\.eu/events/fairimpact\-events/why\-mappings\-matter\-and\-how\-make\-them\-fair](https://fair-impact.eu/events/fairimpact-events/why-mappings-matter-and-how-make-them-fair)
- 2nd SSSOM workshop \(hybrid\) \- **23\.4\.2023**
  - Time: 2:30 pm Italy \(CET\), 1:30 pm BST, 8:30 am EDT, 5:30 am PDT \(3 hours
    total\)
  - register via:
    [https://docs\.google\.com/forms/d/e/1FAIpQLSclpK6G4gE3YaQtn1vHqxyFCUFIZkIvN8oF_mcA5pwkxW\-Bvw/viewform](https://docs.google.com/forms/d/e/1FAIpQLSclpK6G4gE3YaQtn1vHqxyFCUFIZkIvN8oF_mcA5pwkxW-Bvw/viewform)
  - announced via OBO\-list:
    [https://groups\.google\.com/g/obo\-discuss/c/QG9x6N9oziQ?pli=1](https://groups.google.com/g/obo-discuss/c/QG9x6N9oziQ?pli=1)
  - The four use cases we will discuss are:
- Complex mappings \(Tiffany Callahan, Nicolas Matentzoglu\)
- Literal mappings \(James McLaughlin\)
- Value Set / Answer Set / Concept Set mappings \(Chris Roeder\)
- Schema mappings \(Yann Le Franc, Chris Mungall\)
- [CORDI 2023 \- Finding a common ground for NFDI terminologies](https://docs.google.com/document/d/1Y8BiM8czU9RMfFQY6v5HKXMNI9IKmQaFsA3FdXTW_5k)
  ???
- preparing a few slides for the next Section\-Metadata

# <a id="_4in35gwl6myp"></a>Participants

- Arnost Stanzel,
- Christian Stemmer,
- Holger Israel,
- Hendrik Borgelt,
- Matthias L�be,
- Raimi Solorzano,
- David Linke \(NFDI4Cat\)
- Philip Str�mert \(NFDI4Chem, TIB\)
- Luca Ghiringhelli,
- Noemi Betancort,
- Naouel Karam \(NFDI4Biodiv\)

# <a id="_3cakx2qk2ogo"></a>Agenda

**discussed aspect of main topic**

**prepared or present by **

I\-Adopt ontology use in NFDI4Biodiversity

Naouel Karam

# <a id="_71znd1hi3viy"></a>Notes

I\-Adopt

- used to semantify what has been studied/looked at in an observation
  - can be used as
    [schema:variableMeasured](https://schema.org/variableMeasured) value
    - not yet implemented by NFDI4Biodiversity
- I\-Adopt has a terminology registry that uses tabs to filter/list the entities
  defined in the ontology, to help the users find the right external ontology
  term:
  [https://i\-adopt\.github\.io/terminologies/list/all/](https://i-adopt.github.io/terminologies/list/all/)
- in NFDI4Biodiversity they have a semi\-automatic annotation using schema\.org
  and I\-Adopt
  - not yet automated wrt which type of I\-Adopt entities are the
    [schema:PropertyValue](https://schema.org/PropertyValue)s provided
    automatically under the
    [schema:variableMeasured](https://schema.org/variableMeasured) node
- I\-Adopt is kind of a meta\-model in that the instances of its very few
  classes can and should be classes from other ontologies
- research data annotated with this framework \(TBox\) will only say what
  research variables where uses, in other words what was observed/studied, not
  what are the results of this study/observation
  - if multiple variables are within such an ABox of a data set, we cannot know
    their interdependence \(as in which was measured/observed first\), as there
    are no predicates for this in I\-Adopt
- this framework should be endorsed by our WG as it is low level enough to be
  implemented in all consortia
  - seeAlso
    [InteroperAble Descriptions of Observable Property Terminologies \(I\-ADOPT\) WG Outputs and Recommendations](https://zenodo.org/record/6520132#.YnOhMJNBybQ)
    - �Variable as used in I\-ADOPT is used as a synonym for Observable
      Property\. It is the description of something observed or derived�
  - no need for any top level ontology etc\.
  - every research data is based on the variables of a study/investigation
  - it�s a first step to filter the mass of research data based on the study
    variables
  - interoperability depends on using well known/established
    vocabularies/ontologies for instantiating the I\-Adopt classes
    - We still need mappings between ontology terms to integrate I\-Adopt based
      knowledge graphs \(ABoxes\) from different domains\. \(e\.g\. one
      consortium uses PATO to instantiate physical qualities and another one
      might use Wikidata terms for that, so we need a mapping between these to
      allow a query over a combined NFDI I\-Adopt based graph\)
- Question: What are the differences to the
  [ISA framework](https://isa-tools.org/) approach and are there any mappings
  between ISA framework and I\-Adopt?
