<a id="_5l7hdhn1spdj"></a>2024\-01\-23 \- WG Ontology Mapping & Harmonisation

**Date & Time**: 2024\-01\-23 \- 11\-12 CET

**Meeting Link:**

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88)

**Ressources:**

- Link to GDrive workspace:
  [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH)
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)
- [Overview \- WG Ontology Harmonization & Mapping Meetings](https://docs.google.com/document/d/14z6kuAdVaiflWUtjqk3LKt-hqg_DeaRCpLY7TFo1PoU/edit)

**Main Topic:**

# <a id="_4in35gwl6myp"></a>Participants

**Name**

**NFDI project affiliation\(s\)**

Philip Str�mert

NFDI4Chem, N\.A\.

Hendrik Borgelt

NFDI4Cat, N\.A\.

Josh Moore

NFDI4BIOIMAGE, N\.A\.

Cord Wiljes

NFDI\-GS

Jakob Vo�

NFDI4Objects, N\.A\.

Konrad F�rstner

NFDI4Microbiota, N\.A\.

Naouel Karam

NFDI4Biodiversity

Noemi Betancort

KonsortSWD, N\.A\.

Etienne Posthumus

NFDI4Culture, N\.A\.

Heike Fliegl

N\.A\.

Sandra Z�nkert

Base4NFDI

Susanne Kunis

NFDI4BIOIMAGE

Florian Thiery

NFDI4Objects

# <a id="_3cakx2qk2ogo"></a>Agenda

**discussed aspect of main topic**

**prepared or present by **

Base4NFDI Knowledge Graph Infrastructure proposal

Konrad F�rstner

Ontology Engineering / Evaluation / Best Practices

Cord Wiljes

# <a id="_71znd1hi3viy"></a>Notes

- new member Sandra \(Base4NFDI\) section liaison officer, to support the WG of
  the sections
- Base4NFDI Knowledge Graph Infrastructure proposal
  - preparing the second version of the proposal
  - KGs are seen as the playground where the data integration of multiple
    disciplines happens
    - Q: how can our WG contribute to have a mapping between the entities used
      in such a KG database
      - Q \(Naouel\): in how far is the base4nfdi TS meant to be integrated
      - Q \(Jacob\): Is it correct, that the KG infrastructure WG will not
        actually host/serve KGs?
        - Yes, rather provide guidance on how to build a KG database and build a
          registry for all NFDI KGs and only provide one SPARQL endpoint for
          doing federated KG searches
        - Q \(Etienne\): but how is this possible without a central index
          containing all KGs
      - Jacob: Wants some kind of dashboard to see which KG uses which ontology
      - Etienne: how do you deal with LPG and RDF KG differences?
        - not yet thought out fully, but there is the plan to be able to combine
          these at the query level
  - Konrad will send a link to the proposal and comments will be open between
    Feb 5 \- 8
- Ontology Engineering / Evaluation / Best Practices - what is missing so far is
  the overall topic of ontology engineering - how can we do mapping when some of
  the ontologies we are supposed to map are of �poor� quality - Jacob: a subset
  of ontology engineering is relevant for our WG - challenging topic, difficult
  to approach - WG Ontology Mapping: Evaluation of Ontologies important for
  matching, goal is not to extend existing ontologies\. Framework for evaluation
  for ontologies would be helpful - using ROBOT - Foops Score or O�Fair�E
  score? - @etienne will ask if he can share a great presentation about how to
  evaluate ontologies in MatWerk  
  See: _E\. Norouzi, J\. Waitelonis, H\. Sack_: Landscape Analysis of Ontologies
  in Materials Science and Engineering\. In Proc\. of EUROMAT 2023 \->
  [Euromat2023_MSE_ontology_Evaluation](https://docs.google.com/presentation/d/13IAy48dNIe1iK7K1An9dnqX0kpwWHeq0XYBzUhUeZ0k/edit?usp=sharing) -
  s\. rules in OBO foundry to ensure quality  
  Best practices would be good - TS plans to offer high quality - SHACL for
  quality check - Actual data is necessary to advance - s\. FAIRness assessment
  of ontologies - How are ontologies selected? - Biodiversity has explicit
  criteria / process for governance - Cat started with competency questions -
  How to advance? Work with list of ontologies used by the consortia, see
  spreadsheet

ToDo�s from a privat Discussion after the Meeting between Philip and Hendrik
Borgelt:

1. We need to communicate inside of the WG what differentiates us from the TS
   and what work do we need to do for the TS\.

From my point of view
\([hendrik borgelt](mailto:hendrikborgelt@googlemail.com)\) we are a
subcontracting \(zuarbeitende; sorry i think there is no real good translation\)
Working Group which does preparatory work for the Terminology Service\. For
Example we define which Criteria that make out a �good� and �harmonized�
Ontologie, such that a TS might build up a service which checks whether these
criteria are fulfilled\.

I also think that we are a working group that is allowed to propose criteria
that might not be verifiable right now, but that lead to �better� and
�harmonized� Ontologies\. Whether we separate these criterias for �Top\-Level�
domains as given via the grouping in the NFDI \(Engineering, Humanities,
a\.s\.o\.\) we need to discuss\( and i think we are allowed to discuss whether
we are able to harmonize Ontologies �as of now� for all of NFDI\)\.

1. We started a discussion whether we want to collect criteria for a Dashboard
   which determines �how harmonized� the current Ontologies are\. We can not
   force and should not force any Ontology to change, however, I think we should
   at least collect a list of criterias that tell newcomers and even �oldies�
   how to change in order to be more compatible with other Ontologies,
   especially those deemed good and useful in the NFDI\. We are a precursor to a
   standardization organization for ontologies to be used in research data
   management, so we should already be looking at what criteria the ontologies
   we develop should meet\.
