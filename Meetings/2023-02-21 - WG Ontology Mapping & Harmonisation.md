<a id="_5l7hdhn1spdj"></a>2023\-02\-21 \- WG Ontology Mapping & Harmonisation

__Date & Time__: 2023\-02\-21 \- 11\-12 CET

 

__Meeting Link:__

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88)

__Ressources:__

- [https://terminplaner\.dfn\.de/spN7DKSZVdgpsjsQ](https://terminplaner.dfn.de/spN7DKSZVdgpsjsQ)
- Link to GDrive workspace: [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH) 
- List of Meetings and general information: [https://docs\.google\.com/document/d/14z6kuAdVaiflWUtjqk3LKt\-hqg\_DeaRCpLY7TFo1PoU/edit](https://docs.google.com/document/d/14z6kuAdVaiflWUtjqk3LKt-hqg_DeaRCpLY7TFo1PoU/edit) 
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)

__Main Topic:__ Evaluate & Discuss [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)

# <a id="_4in35gwl6myp"></a>Participants

- Philip Strömert \(NFDI4Chem\)

# <a id="_3cakx2qk2ogo"></a>Agenda

- get an overview of what each consortium is working with 
- identify the differences, synergies & pain points needed to be discussed, e\.g\.: 
	- number of consortia using the same top & mid level ontologies
	- differences between disciplines \(e\.g\. humanities & natural sciences\)
- addresses the specific tasks from [WG Charter \- 3\. Work Plan](https://docs.google.com/document/d/1GUh7K0Sy8tyrKZ4-BEizb-9Qa0tt3uzE/edit#heading=h.9mqm7qmjqjz)
	- Evaluate existing domain\-agnostic vocabularies
	- Evaluate existing upper\-level ontologies
- Which are the upper/top\-level ontologies of the ontologies we use?
- Which of the ontologies we use are developed by a consortium?

prepared by: 

- all participating consortia are asked to fill out their tab within this worksheet
- it would be great if someone could make a short analysis of the ontologies listed in there \(e\.g\. \# of consortia using BFO as TLO, \# of consortia using OBO\(RO, IAO, OBI\) / Wikibase / DCat / ProvO, …\)

__discussed aspect of main topic__

__prepared or present by __

We need to clearly indicate which ontologies are developed as part of the NFDI\.

# <a id="_71znd1hi3viy"></a>Notes

## <a id="_xdfcjrjekv9s"></a>domain\-agnostic vocabularies

- OBO framework
	- [OBO Relations Ontology](https://terminology.tib.eu/ts/ontologies/ro)
		- all domain agnostic relations used in OBO
	- [PATO \- the Phenotype And Trait Ontology](https://terminology.tib.eu/ts/ontologies/pato)
		- physical qualities/attributes, like temperature, mass, length etc
	- [Information Artifact Ontology \(IAO\)](https://terminology.tib.eu/ts/ontologies/iao)
		- information objects that are not physical \(e\.g\. the content of a data set\)
	- [Ontology for Biomedical Investigations](https://terminology.tib.eu/ts/ontologies/obi)
		- although rooted in biology, it contains many very general concepts, such as planned process or device, patterns for modeling data from measurements and predictions
	- [Scientific Evidence and Provenance Information Ontology \(SEPIO\)](https://terminology.tib.eu/ts/ontologies/sepio)
	- [Units of measurement ontology](https://terminology.tib.eu/ts/ontologies/uo)
		- SI and other scientifically needed units
- [Experimental Factor Ontology \(EFO\)](https://terminology.tib.eu/ts/ontologies/efo)
- [Bioinformatics operations, data types, formats, identifiers and topics \(EDAM\)](https://terminology.tib.eu/ts/ontologies/edam)
- [Ontology of units of Measure \(OM\)](https://terminology.tib.eu/ts/ontologies/om)
- QUDT/OM
- [Sensor, Observation, Sample, and Actuator \(SOSA\) Ontology](https://terminology.tib.eu/ts/ontologies/sosa)
- [The Extensible Observation Ontology \(OBOE\)](https://terminology.tib.eu/ts/ontologies/oboe)

## <a id="_7hcosgl3nfrf"></a>upper\-level ontologies

- [Descriptive Ontology for Linguistic and Cognitive Engineering Dns Ultralite \(DUL\)](https://terminology.tib.eu/ts/ontologies/dolce)
	- information objects:[http://www\.ontologydesignpatterns\.org/ont/dul/IOLite\.owl](http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl)
	- Systems: [http://www\.ontologydesignpatterns\.org/ont/dul/SystemsLite\.owl](http://www.ontologydesignpatterns.org/ont/dul/SystemsLite.owl)
	- Plans: [http://www\.ontologydesignpatterns\.org/ont/dul/PlansLite\.owl](http://www.ontologydesignpatterns.org/ont/dul/PlansLite.owl)
	- Lexical and semiotic domains: [http://www\.ontologydesignpatterns\.org/ont/lmm/LMM\_L2\.owl](http://www.ontologydesignpatterns.org/ont/lmm/LMM_L2.owl)
	- DOLCE\-Zero: [http://www\.ontologydesignpatterns\.org/ont/d0\.owl](http://www.ontologydesignpatterns.org/ont/d0.owl) \(supposed to be more intuitive\)
- [Basic Formal Ontology](https://terminology.tib.eu/ts/ontologies/bfo)
	- current PURL resolves to the BFO2\.0 version used as classes only backbone by the OBO Foundry
	- [https://github\.com/BFO\-ontology/BFO\-2020](https://github.com/BFO-ontology/BFO-2020) hosts the 2020 ISO version
		- includes [relations that are time indexed](https://github.com/BFO-ontology/BFO-2020/blob/master/21838-2/bfo-2020-relations-table.csv) but [not adopted by OBO](https://github.com/oborel/obo-relations/wiki/ROAndTime)
- [Semanticscience Integrated Ontology \(SIO\)](https://terminology.tib.eu/ts/ontologies/sio)
- [General Formal Ontology](https://bioportal.bioontology.org/ontologies/GFO)
	- seems outdated, as last release in 2006, also unknown number of users
- SUMO or CYC
	- no open version available\!?
- UFO
- [The European Materials Modelling Ontology \(EMMO\)](https://terminology.tib.eu/ts/ontologies/emmo)
- OntoCape
- Schema\.org
- Wikidata ontology
- Dublin Core
- [CIDOC\-CRM](https://terminology.tib.eu/ts/ontologies/cidoc)
- QUDT
- [NFDI4Culture Ontology](https://nfdi4culture.de/ontology.html) \(?\)

Notes from the call

- Mark Doerr: let’s have some people present TLOs to the other 
- Marc Fuhrmans: agree on some guiding questions for analyzing TLO
	- should the outcome be to align a domain ontology completely to one TLO?
	- should the outcome be to mix TLOs in domain ontologies according to their “strengths”, e\.g\. BFO for processes and EMMO for material entities
	- the latter might be equivalent to a suggestion of top level entities for typical entities encountered in domain ontologies
- Matrix of typical entities to be modeled vs TLOs with corresponding term plus some notes on use / strong points
- we need to have as part of our focus the differentiation between when to use reasoning and when not
- a very powerful feature of ontology structured \(meta\-\) data are federated queries, so combining information from different data\-sources, therefore a better understanding of what is important to achieve optimal federated queries

Terms defined in top level ontologies  \-> [second worksheet in Used Ontologies Table](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=1839424810) 

- location
- process
- method
- tool
- material
- time
- space
- context
- information
- qualities/attributes/properties \(of material things, processes and information\)

