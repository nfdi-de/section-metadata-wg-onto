<a id="_5l7hdhn1spdj"></a>2023\-03\-08 \- WG Ontology Mapping & Harmonisation

Date & Time: 2023\-03\-08 \- 11\-12 CET

 

__Meeting Link:__

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88) 

__Ressources:__

- [https://terminplaner\.dfn\.de/spN7DKSZVdgpsjsQ](https://terminplaner.dfn.de/spN7DKSZVdgpsjsQ)
- Link to GDrive workspace: [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH) 
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)

__Main Topic:__ 

- evaluate which ontologies are used in the various NFDI
	- identify the differences, synergies & pain points needed to be discussed, e\.g\.: 
		- number of consortia using the same top & mid level ontologies
		- differences between disciplines \(e\.g\. humanities & natural sciences\)
- presentations \(15 min\) about EMMO & CIDOC\-CRM
- first informal “mapping” [table/overview](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=1839424810) of very general concepts

# <a id="_4in35gwl6myp"></a>Participants

- Oliver Koepler  \(NFDI4Chem\)
- Marc Fuhrmans \(NFDI4Ing\)
- Philip Strömert \(NFDI4Chem\)
- Holger Israel
- Mark Doerr \(NFDI4Cat\)
- Alexander Wolodkin \(NFDI4Earth, SGN\)
- Dorothea Iglezakis \(NFDI4Ing\)
- Stephan Hachinger
- Josh Moore \(NFDI4Bioimage\)
- Olga Giraldo \(NFDI4DataScience\)

# <a id="_3cakx2qk2ogo"></a>Agenda

__discussed aspect of main topic__

__prepared or presented by __

[EMMO \- basic concepts ](https://docs.google.com/presentation/d/1Kn60mw2P3THXwdXU4tZx8ETJTLMc7Sp9n6V3nrmNaRw/edit?usp=sharing)

Mark Doerr

# <a id="_71znd1hi3viy"></a>Notes

__Short intro to EMMO__

- [https://github\.com/emmo\-repo/EMMO/](https://github.com/emmo-repo/EMMO/) 
- developed by philosophers and physicists
- multiperspective aspects
	- to cover different aspects of how to look at / model the world
	- supposed to cover arts as well as natural sciences
		- covers many basic \(quantum\-\)physical concepts and SI units as the basis of describing materials
- semiotic perspective \(emmo:Semiotics\)
	- to represent the semiotic triangle that includes the interpreter, sign and real world \(semiotic\) object
- causal perspective
- mereological perspective \(parts\-whole relations\) \[cf\. [https://en\.wikipedia\.org/wiki/Mereology](https://en.wikipedia.org/wiki/Mereology)\]
- Importance of EMMO for chemists on quantum Level to model reactions, characteristics

__Questions regarding EMMO__

- What was the need to make yet another TLO? 
	- PS \(answer based on the talk?\): with EMMOntoPy there is a direct bridge of using an ontology directly in ones code
	- Answers: Need to describe physical objects \(on a quantum level / wave/particle dualism\) in detail
- Advantage of EMMOntoPy is a programmatic access to the ontology from python code\. Can a more generic approach be accessing an API of a TS \(e\.g\. [TIB TS](https://terminology.tib.eu/ts/ontologies/?sorting=)\)?
- How will these abstract TLO concepts be documented to make sure that users with less knowledge can use EMMO correctly?
	- common argument against TLOs like BFO that its concepts are labeled and defined too incomprehensible/abstract to be reused in a more concrete setting
	- Are there design patterns defined for EMMO that will make sure to reuse/expand it properly, e\.g\. a plain weight measurement pattern?
		- measurement modeling examples from Mark Doerr: [https://gitlab\.com/opensourcelab/scientificdata/ontologies/openscienceontology/measurements/\-/tree/main/oso\_measurements](https://gitlab.com/opensourcelab/scientificdata/ontologies/openscienceontology/measurements/-/tree/main/oso_measurements)
- Are there any mappings to other TLOs or ontologies with top level / general concepts?
	- Mark Doerr will raise an Issue on EMMO github repo\.
- EMMO’s modules are expected to be developed using EMMOntopy \(based on owlready2\) \- how does this setup relate to the Ontology Development Kit \(ODK\)
	- EMMOntopy is more light\-weight \(and also less powerful\) than ODK\. It is a simple “pip install emmontopy”, no docker image, in\-built workflow
	- EMMO itself is still developed with Protegé
	- Are there templates \(repo structure\), automated checks etc?
		- yes, to some extent: there is a tool, called “emmocheck” for testing, if the developed sub\-ontology is designed according to the EMMO guidelines: [https://github\.com/emmo\-repo/EMMOntoPy/blob/master/docs/tools\-instructions\.md\#emmocheck](https://github.com/emmo-repo/EMMOntoPy/blob/master/docs/tools-instructions.md#emmocheck)
	- [https://github\.com/emmo\-repo/EMMOntoPy](https://github.com/emmo-repo/EMMOntoPy), general approach for any ontology [https://pypi\.org/project/Owlready2/](https://pypi.org/project/Owlready2/) ?
	- Is the Python based dev approach documented in tutorials/how tos?
		- 
			- since it is owlready2 based, most of the \(good\) documentation 
			- of owlready2 applies to EMMOnotpy \- [https://doi\.org/10\.1007/978\-1\-4842\-6552\-9](https://doi.org/10.1007/978-1-4842-6552-9)
			- the EMMOntoPy documentation could still be improved 
		- How are users expected to do it right?
			- for developments on EMMO itself EMMO uses the discussion tools of github \- with the feedback from the EMMO community to verify that it was done “right” \(whatever ‘right’ means :\)
			- simple design errors are checked with emmocheck and a github pipeline\.
		- how can a Python based approach be synced with a GUI based dev e\.g\. via Protege or Webprotege?
			- EMMOntopy/owlready3 allows to import common file formats \(owl/xml, ttl, e\.g\.\) but there is no RDF\->EMMOntoPy python code converter\. Imports python classes\. One has to decide whether to develop an ontology with a python representation or a GUI representation\.
			- EMMO \(core\) is to my knowledge still developed with Protegé, EMMOntopy is only currently used by domain ontology developers
- How big is the current user base?
- Is there a use case in the biological or biochemical domain modeled with EMMO that shows the advantages of using this TLO vs to use BFO or SIO?

