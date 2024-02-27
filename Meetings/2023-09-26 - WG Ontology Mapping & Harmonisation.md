<a id="_5l7hdhn1spdj"></a>2023\-09\-26 \- WG Ontology Mapping & Harmonisation

Date & Time: 2023\-09\-26 \- 11\-12 CET

 

Meeting Link:

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88) 

Ressources:

- Link to GDrive workspace: [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH) 
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)
- [Overview \- WG Ontology Harmonization & Mapping Meetings](https://docs.google.com/document/d/14z6kuAdVaiflWUtjqk3LKt-hqg_DeaRCpLY7TFo1PoU/edit)

Main Topic\(s\): 

- CORDI [presentation](https://docs.google.com/presentation/d/1H3NMd-bJbeEbBWYh2iVTIYflyvMHzrGp_EBKhuds4eo/) & other output from the conference that might be of interest to this WG

# <a id="_4in35gwl6myp"></a>Participants

__Name__

__NFDI project affiliation\(s\)__

Philip Strömert

NFDI4Chem, N\.A\.

Cord Wiljes

NFDI\-GS, N\.A\.

Alexander Wolodkin

NFDI4Earth

Jakob Voß

NFDI4Objects, N\.A\.

Hendrik Borgelt

 NFDI4Cat

Mark Dörr

NFDI4Cat, 

Leyla Jael Castro

NFDI4Ing, N\.A\.

Dorothea Iglezakis

NFDI4Ing, MaRDI

Base4NFDI, N\.A\.

Base4NFDI, N\.A\.

# <a id="_3cakx2qk2ogo"></a>Agenda

__discussed aspect of main topic__

__prepared or present by __

refocusing on tasks and goals of wg onto mapping & harmonization \([presentation](https://docs.google.com/presentation/d/1Ik62-09h6YgFHL4EDrDj1yOxll0aasunEkYC0Xz5WZ4/edit#slide=id.p1)\)

Hendrik Borgelt

CORDI [presentation](https://docs.google.com/presentation/d/1H3NMd-bJbeEbBWYh2iVTIYflyvMHzrGp_EBKhuds4eo/) & other output from the conference that might be of interest to this WG

Philip Strömert

I\-Adopt framework \- background  ?

Mark Dörr

# <a id="_71znd1hi3viy"></a>Notes

- Philip needs to send out emails before each call, 3 days in advance
- need more participation for preparing agendas for the upcoming calls
	- need to make our topic proposals more prominent
- CORDI [presentation](https://docs.google.com/presentation/d/1H3NMd-bJbeEbBWYh2iVTIYflyvMHzrGp_EBKhuds4eo/) & other output from the conference that might be of interest to this WG
	- analysis part was critiqued
		- not clear enough what was actually achieved by the WG 
	- I\-ADOPT part was critiqued
		- was not made clear enough, that this is not “THE” upper level framework we should all adhere to, but that is is only a “PROPOSED” way to commonly describe __the research variables__ that were used in the creation of a specific dataset, so that the dataset can be found with an I\-ADOPT based federated query\. 
			- e\.g\. ask all the NFDI SPARQL endpoint to retrieve me all datasets in which the iadopt:variable idaopt:hasObjectOfInterest NCBITaxon:9606 \(Homo sapiens\)
- refocusing on tasks and goals of wg onto mapping & harmonization
	- we need to put more energy on focusing on specific topics/aims of our WG
	- Hendrik [presented](https://docs.google.com/presentation/d/1Ik62-09h6YgFHL4EDrDj1yOxll0aasunEkYC0Xz5WZ4) a constructive criticism that asks in how far we have been addressing the main goals of our charter so far\.
	- Jakob: “How similar are two ontologies?” is a different question than “How interoperable are two ontologies?”

1. RE AIM: Increase cross\-domain interoperability within NFDI and other infrastructures \(EOSC\) by providing linkages and crosswalks between terminologies, ontologies, and domain\-specific knowledge graphs\.
	1. we need to focus on what not to include in our mapping efforts
		1. no meta terminologies like: SHACL, OWL, RDF
		2. Jakob: better ask how something is used instead of what it "is"
	2. what about DCAT, Schema\.org, should they be included in our mapping efforts?
		1. Philip: Schema\.org & Bioschemas will be used by multiple consortia to produce RDFs/JSON\-LD text that will be incorporated in websites of repositories in order to allow search engines like Google to index more fine grained\. \-> so yes we should have mappings from schema\.org to other ontologies like, PROV\-O etc\. 
	3. Hendrik: we need hard metrics for interoperability and our WG
		1. Dorothea: Is it really metrics on interoperability that we need or do we need ways to get interoperability by agreeing on reference terms/terminologies to map to for central concepts?
2. RE WG AIM: Assessment of standards for the creation and maintenance of mappings, the formal documentation of mappings and their metadata in collaboration with the Terminology Services WG, as well as their \(re\-\)evaluation and publication
	1. CORDI feedback: we need better parameters that deal with interoperability \-> maybe count/present the number of mappings we have
3. RE WG AIM: provision of formal alignments between commonly used upper\- and mid\-level terminologies to support broad semantic interoperability among domain\-specific terminologies\.
	1. Hendrik: shouldn’t we rather consider a bottom\-up approach instead of current top\-down approach
4. RE WG AIM: Collect, amend, and harmonize quality standards for metadata annotations in the context of their practical application in NFDI and EOSC \(cf\. [WG\_Search\_and\_Harvesting\.docx](https://docs.google.com/document/d/1fmG32Y9t2FwMpwUm_x-HsODsy2O0GMtW/edit?usp=sharing&ouid=104521175430650419376&rtpof=true&sd=true)\)\.
5. RE WG AIM: Reach out to and collaborate with communities of ontology maintainers to ensure that steps needed for harmonization are taken up into the original ontology specification as well as to promote the acceptance and implementation of changes to the source terminologies\.
6. RE WG AIM: Demonstration of how ontologies are applied to concrete metadata \(cf\.  [WG Cookbook\(s\), Guidance and Best Practices\.docx](https://docs.google.com/document/d/1ll1h5Yx6_QMTWx7T_wXYoDCq-WxR4MB-/)\)\.
7. RE WG AIM: Reach out to and collaborate with communities of ontology maintainers to ensure that steps needed for harmonization are taken up into the original ontology specification as well as to promote the acceptance and implementation of changes to the source terminologies\.
8. RE WG AIM: Facilitating the FAIRification of terminologies used in the NFDI consortia by providing concrete examples and by embedding them in a FAIR “ecosystem” of services to reach semantic interoperability\. 
9. RE WG AIM: Assessment of the diversity/similarity \(on term level\) of top\- and mid level ontologies to get a measure on why they are so hard to harmonise \- maybe leading also to recommendations for the ontology developers to make their ontologies more interoperable\. By this analysis one could at least provide recommendations for the whole NFDI, which ontology should be used if one wants to model the world from a certain perspective, e\.g\. if your view on the world focuses on human artefacts, use these X ontologies, if you have a quantum physical perspective on the world, you should rather use these Y ontologies as your top\-and mid level ontologies\. This assessment could also lead to ontology similarity maps \(analog to amazon recommendations: if you like/use this ontology a, you might also have a look into that ontology b\)\. 

- [https://hal\-lirmm\.ccsd\.cnrs\.fr/lirmm\-01852080v2](https://hal-lirmm.ccsd.cnrs.fr/lirmm-01852080v2) 
	- FAIR vocabularies/terminologies \-> O’FAIRe checker tool by Clement Jonquet’s group from ONTOFAIR
	- Features of a FAIR Vocabulary [https://doi\.org/10\.1186/s13326\-023\-00286\-8](https://doi.org/10.1186/s13326-023-00286-8) 

