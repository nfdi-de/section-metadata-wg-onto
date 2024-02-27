<a id="_k44po7jd0odo"></a>2023\-11\-08 \- WG Ontology Mapping & Harmonisation

Date & Time: 2023\-11\-08 \- 11\-12 CET

 

__Meeting Link:__

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88) 

__Ressources:__

- Link to GDrive workspace: [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH) 
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)
- [Overview \- WG Ontology Harmonization & Mapping Meetings](https://docs.google.com/document/d/14z6kuAdVaiflWUtjqk3LKt-hqg_DeaRCpLY7TFo1PoU/edit)

__Main Topic:__ Finding common ontology mapping use cases / tools

- see also: [2023\-10\-24 \- WG Ontology Mapping & Harmonisation](https://docs.google.com/document/d/1JMcVUaUGE0zOathl6YPi9iu3JXKIGcFPSnD5JlHbCbg/edit#heading=h.71znd1hi3viy)

# <a id="_4in35gwl6myp"></a>Participants

__Name__

__NFDI project affiliation\(s\)__

Jakob Voß

NFDI4Objects

Philip Strömert

NFDI4Chem, N\.A\.

Arnost Stanzel

NFDI4Memory, N\.A\.

Kathryn Dumschott

DataPLANT, N\.A\.

Anja Gerber

NFDI4Objects, N\.A\.

Alexander Wolodkin

NFDI4Earth, N\.A\.

Hendrik Borgelt

NFDI4Cat

Florian Thiery

NFDI4Objects

Luca Ghiringhelli

FAIRmat

Etienne Posthumus

NFDI4Culture, N\.A\.

# <a id="_3cakx2qk2ogo"></a>Agenda

__discussed aspect of main topic__

__prepared or present by __

NFDI4culture ontology

Philip

# <a id="_71znd1hi3viy"></a>Notes

## <a id="_8es8yywjwu22"></a>NFDI4Culture / NFDICore Ontology 

- [https://nfdi4culture\.de/de/ressourcen/ontologie\.html](https://nfdi4culture.de/de/ressourcen/ontologie.html) & [https://nfdi4culture\.de/de/ressourcen/ontologie\.ttl](https://nfdi4culture.de/de/ressourcen/ontologie.ttl)
	- 27 owl:equivalentClass, 3 owl:equivalentProperty
- [https://github\.com/ISE\-FIZKarlsruhe/nfdi4culture\-ontology/blob/main/cto\_mappings\.ttl](https://github.com/ISE-FIZKarlsruhe/nfdi4culture-ontology/blob/main/cto_mappings.ttl) 
	- general terms are mapped:  
34 owl:equivalentClass, 10 owl:equivalentProperty
	- unfortunately no SSSOM format nor any mapping justification
- planned to be based on [https://nfdi\.fiz\-karlsruhe\.de/ontology](https://nfdi.fiz-karlsruhe.de/ontology) \-> this NFDIcore ontology does not have any terms as of yet \-> wrong IRI
	- working IRI \- [https://ise\-fizkarlsruhe\.github\.io/nfdicore/](https://ise-fizkarlsruhe.github.io/nfdicore/) 
	- does anyone know more on this?
- “should” probably be used for all the “povenance” infos of a dataset
- Information graph = infos about the data portals/repos, the orgs and persons within  NFDI
- data graph = index of the actual data \(minimal dataset: What is my data describing\)
- overlap between 4culture Ontology and NFDICoreOntology \-> 4culture ontology classes that are in the NFDICoreOntology will most likely be swapped in the future in favor for the NFDICoreOntology ones
- how can we tell stories better with such a kg
- identifying similar vocabulary within the consortia, such as GND, Wikidata, Geonames, IconClass, Getty AAT \-> what are the similarities between us all
	- tried within [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/) \-> problems regarding having to maintain this manually, some overlap can be identified already with this

## <a id="_wha7u1imf90z"></a>Use cases / user stories

- we want to collect concrete use cases in terms of user stories that could be translated into SPARQL queries to be run over a NFDI KG
- we want to collect concrete examples of datasets from each consortium
	- each consortium provides 1\-3 data\(set\) exsamples which are parsable \(not binary code\)
	- we hope to be able to use these examples to derive a common set of terms describing such datasets NFDI wide
		- PS: CAVE overlap to the I\-ADOPT approach imho
- N4O example: TA6 has developed a first questionnaire for user stories for object biographies to get in touch with researchers:
- Object:
	- __intended/original context__
		- Source
		- Event: Creation/Production
			- Person: Actor
			- Time: time\-span/date
			- Place
			- event: Donation
				- Person: Actor
				- Time: time\-span/date
				- Place
				- …
	- __find/excavation context__
		- Source
		- Contextualisation like in an event: excavation/find
		- Time
		- Place
		- Actor
		- GIS\-Data
		- Translocation
	- __collection/museumcontext__
		- Source
		- Event: Acquisition
			- Time
			- Actors
			- …
		- Event: Accession
			- …
		- Event: Documentation
			- Inventarisierung
			- Photo
			- Description
			- Measurement
			- …
		- Event: …
	- __research context__
		- … anything within your research subject
	- __trivial context__
		- …

### <a id="_kkrp8ec2wmuh"></a>Examples User Stories

#### <a id="_f4jtjnw0sq9x"></a>4Chem

- Which data in the NFDI are about \(observed/meassured/assayed/used\) a certain [CHEBI:chemical entity](https://terminology.tib.eu/ts/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_24431) in some context, e\.g\. [CHEBI:carbon dioxide](https://terminology.tib.eu/ts/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16526) SKOS:relatedMatch [TEMA:carbon dioxide](https://terminology.tib.eu/ts/ontologies/tema/terms?iri=https%3A%2F%2Fpurl.org%2Ftema%2F001753) SKOS:relatedMatch [uat:Carbon dioxide](https://terminology.tib.eu/ts/ontologies/uat/individuals?iri=http%3A%2F%2Fastrothesaurus.org%2Fuat%2F196) SKOS:relatedMatch [ECSO:Carbon Dioxide](https://terminology.tib.eu/ts/ontologies/ecso/terms?iri=http%3A%2F%2Fpurl.dataone.org%2Fodo%2FECSO_00000323)?
- Which data in the NFDI are about some [CHMO:spectrum](https://terminology.tib.eu/ts/ontologies/chmo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHMO_0000800) SKOS:relatedMatch [EDAM:Spectrum](https://terminology.tib.eu/ts/ontologies/edam/terms?iri=http%3A%2F%2Fedamontology.org%2Fdata_3483) SKOS:relatedMatch [MS:spectrum](https://terminology.tib.eu/ts/ontologies/ms/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMS_1000442) SKOS:relatedMatch [AFO:spectrum](https://terminology.tib.eu/ts/ontologies/afo/terms?iri=http%3A%2F%2Fpurl.allotrope.org%2Fontologies%2Fresult%23AFR_0000068) \(and are not indexed in an NFDI4Chem affiliated data repository\)?
- Which data in the NFDI are associated with the method [NCIT:Spectroscopy](https://terminology.tib.eu/ts/ontologies/ncit/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FNCIT_C17155) SKOS:relatedMatch [CHMO:spectroscopy](https://terminology.tib.eu/ts/ontologies/chmo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHMO_0000228) SKOS:relatedMatch [MODSCI:Spectroscopy](https://terminology.tib.eu/ts/ontologies/modsci/terms?iri=https%3A%2F%2Fw3id.org%2Fskgo%2Fmodsci%23Spectroscopy) SKOS:relatedMatch [uat:Spectroscopy](https://terminology.tib.eu/ts/ontologies/uat/individuals?iri=http%3A%2F%2Fastrothesaurus.org%2Fuat%2F1558) SKOS:relatedMatch [gemet:spectroscopy](https://terminology.tib.eu/ts/ontologies/gemet/individuals?iri=http%3A%2F%2Fwww.eionet.europa.eu%2Fgemet%2Fconcept%2F7992) SKOS:relatedMatch [enm:spectroscopy](https://terminology.tib.eu/ts/ontologies/enm/terms?iri=http%3A%2F%2Fpurl.bioontology.org%2Fontology%2Fnpo%23NPO_1468) SKOS:relatedMatch [SWEET:spectroscopy](https://terminology.tib.eu/ts/ontologies/sweet/terms?iri=http%3A%2F%2Fsweetontology.net%2FreprSciMethodology%2FSpectroscopy) SKOS:relatedMatch [panet:spectroscopy](https://terminology.tib.eu/ts/ontologies/panet/terms?iri=http%3A%2F%2Fpurl.org%2Fpan-science%2FPaNET%2FPaNET01125) SKOS:relatedMatch [TEMA:spectrometry](https://terminology.tib.eu/ts/ontologies/tema/terms?iri=https%3A%2F%2Fpurl.org%2Ftema%2F003214)?

#### <a id="_9pzhg3usz7fg"></a>4Memory:

- Show me all data, that is related to event x \(might be something like the french revolution, a certain date or an observation of an molecule \(history of science\!\)
- Show me data, that was collected at place x
- Show me data, that has information about a place x\.
- Show me data, that was collected by person x \(might be a colleague, but also a engineer \(again, history of science perspective\)
- Show me data, that has information about person x\. 
	- According to this schema, historians might be interested in data from other entities like organisations, institutions, etc\. 
- Show me data that is related to topic x \(topic described by a authority file entry\)\.

### <a id="_yv0bwvdaytat"></a>Example Datasets

#### <a id="_8qqxfh2egmpk"></a>4Chem

- [https://search\.nfdi4chem\.de/dataset/](https://search.nfdi4chem.de/dataset/) 

## <a id="_1s01mwy8hom2"></a>Next Steps

All members of this WG are asked to provide:

- exemplary datasets \- ideally already described with the NFDICoreOntology or in RDF/JSON\-LD using other ontologies
- user stories that could be translated into SPARQL queries

