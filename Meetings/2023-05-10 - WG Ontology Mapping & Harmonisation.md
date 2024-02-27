<a id="_i1br8ohyhucl"></a>2023\-05\-10 \- WG Ontology Mapping & Harmonisation

__Date & Time__: 2023\-05\-10 \- 11:00\-12:00 CET

 

__Meeting Link:__

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88) 

__Ressources:__

- Link to GDrive workspace: [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH) 
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)

__Main Topic:__ 

- Modelling Processes
	- processes in 4Chem according to “pure” OBO pattern
	- processes in [m4i](https://metadata4ing.org)
	- processes in ???

# <a id="_4in35gwl6myp"></a>Participants

Luca Ghiringhelli \(FAIRmat, HU Berlin\)

Philip Strömert \(TIB\)

Naouel Karam \(NFDI4Biodiv\)

Akhil Patil \(NFDI4Ing, DLR\-TS\)

Noemi Betancort \(KonsortSWD, U Bremen\)

- 5 others

# <a id="_3cakx2qk2ogo"></a>Agenda

__discussed aspect of main topic__

__prepared or present by __

[OBO/OBI Process Pattern](https://docs.google.com/presentation/d/1SouuZxX2ehVPWoY-KSgYFE1n3LvOgp6hZWjWlDTMp5w/) 

Philip Strömert

[presentation](https://docs.google.com/presentation/d/1bawpRMPnO347T99MW5GepXP0PgdudkGP/edit#slide=id.p1) of processes in [m4i](https://metadata4ing.org)

Marc Fuhrmans

# <a id="_71znd1hi3viy"></a>Notes

M4Ing  \- ontology

- atm a very general process model
- why not reuse OBI, IAO and other OBO ontologies, although reusing BFO?
- reusing BFO2020?
- how do you import external ontologies?
	- do you import the whole ontology or make custom import modules?
		- how do you make sure you have all axioms from the external ontologies?
		- Dorothea: manually curated import modules
			- Philip: entails the risk of getting out of sync with the external ontologies and missing axioms of terms which would essentially change the semantics of the reused term
- [documentation](https://nfdi4ing.pages.rwth-aachen.de/metadata4ing/metadata4ing/index.html) \- ability to hide parents to not confuse novice user
- Philip: Is it meant as a schema to be reused or an application ontology? \(asking because of the first steps guide\)
- Naouel: do you have mappings to the top level terms used from external ontologies?
	- Marc: logical declared/asserted in the ontology

OBO/OBI Process pattern

- Marc Fuhrmann: How can you specify in a fine grained fashion what the inputs and output of processes are when it comes to information\.
	- Philip: IAO:plan spec is an IAO:information entity and can thus have as parts other IAO:information entities\. In [Slide 7](https://docs.google.com/presentation/d/1SouuZxX2ehVPWoY-KSgYFE1n3LvOgp6hZWjWlDTMp5w/edit#slide=id.g2419522a800_0_1) you can see IAO:setting datum as being part of the plan specification, and this class can be used together with the [OBI data modeling pattern](http://obi-ontology.org/docs/data-intro/) to for example say that one part of the assay specification \(actually its action specification part\) is to set the device temperature to 30° C\.

