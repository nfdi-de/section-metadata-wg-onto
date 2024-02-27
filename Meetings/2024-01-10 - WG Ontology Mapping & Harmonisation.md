<a id="_lnw4xdkba5vf"></a>2024\-01\-10 \- WG Ontology Mapping & Harmonisation

__Date & Time__: 2023\-12\-13 \- 11\-12 CET

 

__Meeting Link:__

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88) 

__Ressources:__

- Link to GDrive workspace: [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH) 
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)
- [Overview \- WG Ontology Harmonization & Mapping Meetings](https://docs.google.com/document/d/14z6kuAdVaiflWUtjqk3LKt-hqg_DeaRCpLY7TFo1PoU/edit)

__Main Topic:__ 

- resume discussion around proper differentiation between “research information” metadata and “research data” metadata
- see also email thread “RE:Yesterday's call recap” \(last reply 5\.12\.2023\)

# <a id="_4in35gwl6myp"></a>Participants

__Name__

__NFDI project affiliation\(s\)__

Josh Moore

NFDI4BIOIMAGE, N\.A\.

Anja Gerber

NFDI4Objects, N\.A\.

Hendrik Borgelt

NFDI4Cat, N\.A\.

Harald Kornmayer

N\.A\., N\.A\.

Alexander Wolodkin

NFDI4Earth, N\.A\.

Kathryn Dumschott

DataPLANT, N\.A\.

David Linke

NFDI4Cat, N\.A\.

Jakob Voß

NFDI4Objects, N\.A\.

Heike Fliegl

N\.A\., N\.A\.

Philip Strömert

NFDI4Chem, N\.A\.

# <a id="_3cakx2qk2ogo"></a>Agenda

__discussed aspect of main topic__

__prepared or present by __

# <a id="_71znd1hi3viy"></a>Notes

## <a id="_5eb0sr1jyk9j"></a>layers of metadata

taken from the email thread, we have these layers of metadata:

1. "meta" research information \(metadata about the organization and outputs of funded research processes\)
	1. \-> This is the fokus of KDSF but also mostly\(?\) in DCAT\.
2. outer view on shared research data object \-> This is DCAT\.
3. inner view of shared research data objects \-> Discipline models/ontologies

\-> layer 1 & 2 can be subsumed into one layer that represents the research information metadata 

- this assumes that detail information about e\.g\. a creator, funder or project is provided elsewhere and just referencing it by PID \(persitent ID, e\.g\. ORCID, ROR or DFG\-ID\) is sufficient

__\-> Our recommendation regarding layer 1 for all NFDI consortia__

- use CERIF as standard for the research information metadata
	- can be transformed to DCAT, Schema\.org, Datacite or Wikidata based on existing mappings \-> [https://eurocris\.org/news/cerif\-rdf\-mapped\-most\-common\-metadata\-schemes](https://eurocris.org/news/cerif-rdf-mapped-most-common-metadata-schemes) 
		- needs to be worked on in terms of implementation in cookbooks/guides
		- see also:
			- [https://www\.w3\.org/2015/spatial/wiki/ISO\_19115\_\-\_DCAT\_\-\_Schema\.org\_mapping](https://www.w3.org/2015/spatial/wiki/ISO_19115_-_DCAT_-_Schema.org_mapping)
			- [https://www\.w3\.org/TR/vocab\-dcat\-3/\#dcat\-sdo](https://www.w3.org/TR/vocab-dcat-3/#dcat-sdo) 
			- [https://www\.wikidata\.org/wiki/Wikidata:WikiProject\_Datasets/Data\_Structure/DCAT\_\-\_Wikidata\_\-\_Schema\.org\_mapping](https://www.wikidata.org/wiki/Wikidata:WikiProject_Datasets/Data_Structure/DCAT_-_Wikidata_-_Schema.org_mapping) 
			- [https://ec\-jrc\.github\.io/datacite\-to\-dcat\-ap/\#mapping\-summary](https://ec-jrc.github.io/datacite-to-dcat-ap/#mapping-summary)
	- Experimental CERIF\-Ontology in RDF exists at [https://cerif\.eurocris\.org/model](https://cerif.eurocris.org/model) 
	- DCAT and DCAT\-AP is probably the more widely used standard when having RDF data, as CERIF is originally XML based and just recently ported to RDF
		- so we need to find existing mappings and transformation guides between the two \(e\.g\. CERIF XML metadata to DCAT RDF metadata\)

## <a id="_rgry5ybnmjen"></a>Next steps

- __How to attach the domain specific “research data” metadata to the DCAT/CERIF based “research information” metadata”__
	- who knows how this is done in other projects? 
		- how is it done when using RDA’s [I\-ADOPT](https://i-adopt.github.io/)?
			- seems a good candidate framework for describing only the observed entity and its characteristics \-> lacks expressivity regarding the used method of the observation  
		- how is it done when using the [Cross Domain Interoperability Framework CDIF](https://worldfair-project.eu/cross-domain-interoperability-framework/)
			- we need to get more info about this and how it fits into our WG work
	- Hendrik tries to present how 4Cat attaches domain specific metadata to the research information metadata part described with DCAT\-AP
- Our recommendation to use CERIF for the research info metadata layer should be written up in a properly publish format asap
	- should link to guides on how to use DCAT\-AP and CERIF 
		- seems to be part of the tasks from WG Cookbooks \-> we need to aks them what they already have in this regard
			- @Holger will ask Susanne Arendt how much their WG have in this regard

