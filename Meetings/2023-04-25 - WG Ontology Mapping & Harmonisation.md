<a id="_5l7hdhn1spdj"></a>2023\-04\-25 \- WG Ontology Mapping & Harmonisation

**Date & Time**: 2023\-04\-25 \- 11:00\-12:00 CET

**Meeting Link:**

[https://tib\-eu\.webex\.com/tib\-eu\-en/j\.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88](https://tib-eu.webex.com/tib-eu-en/j.php?MTID=mcd77c9718249ee0fdde541ee7e5b6c88)

**Ressources:**

- Link to GDrive workspace:
  [WG Ontology Harmonization and Mapping](https://drive.google.com/drive/folders/1hLgFgzp0cS_Pi8hpI9zOD7DcY3SUXRNH)
- [Used Ontologies @ NFDI](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit#gid=0)

**Main Topic:** NFDI4Culture core ontology, CoRDI abstract submission

# <a id="_4in35gwl6myp"></a>Participants

- [Philip Str�mert](mailto:philip.stroemert@tib.eu) \(NFDI4Chem, TIB\)
- Marc Fuhrmans \(NFDI4Ing, TU Darmstadt\)
- Luca Ghiringhelli \(FAIRmat, HU Berlin\)
- Raimi Solorzano Niederhausen \(NFDI4Biodiversity, InfAI\)
- Susanne Arndt \(NFDI4Ing, TIB\)
- Mark D�rr \(NFDI4Cat\)
- Olga Giraldo \(NFDI4DS, ZBMED\)
- [Etienne Posthumus](https://epoz.org/) \(NFDI4Culture\)
- Paul Duchesne \(NFDI4Culture\)
- Lozana \(NFDI4Culture\)
- Leyla Jael Castro \(ZB MED\)

# <a id="_3cakx2qk2ogo"></a>Agenda

**discussed aspect of main topic**

**prepared or present by **

NFDI core ontology / NFDI4Culture ontology

Etienne Posthumus

[CORDI 2023 \- Finding a common ground for NFDI terminologies](https://docs.google.com/document/d/1Y8BiM8czU9RMfFQY6v5HKXMNI9IKmQaFsA3FdXTW_5k/edit)

Naouel & Philip

# <a id="_71znd1hi3viy"></a>Notes

## <a id="_xqt0zoy2a1p7"></a>NFDI core ontology / NFDI4Culture ontology

- slides:
  [https://doi\.org/10\.5281/zenodo\.7748739](https://doi.org/10.5281/zenodo.7748739)
- SKOS terminologies are also of interest as often used in 4Culture
  - so we need to also think about mapping/harmonization between terminologies
    of different types \(SKOS, OWL etc\.\)
- Ontologies
  - modular approach
  - [NFDIcore](https://nfdi.fiz-karlsruhe.de/ontology) \(GitHub:
    [https://github\.com/ISE\-FIZKarlsruhe/nfdicore](https://github.com/ISE-FIZKarlsruhe/nfdicore)\)
    as TLO & planned to be extended by other consortia
  - modeling method based on actual data \-> limit the modeling to real world
    use cases \-> saves time and effort
  - NFDIcore being reused in MatWerk Ontology already \(material science\)
- knowledge graphs
  - really difficult to convince people to do actual KGs <\- lessons learned
    from 3 years of NFDI4Culture
- Research Information Graph & Research Data Graph = NFDI4Culture 2\.0 KG
- trying to integrate project partners that do not have the resources to have
  their own KG \-> [CGIF](https://docs.nfdi4culture.de/ta5-cgif-specification)
  format used instead, simpler way to get structured data from partners to be
  ETLed into the 2\.0 KG
  - schema\.org based \-> side benefits \(google search indexing etc\)
- another source = the Wikibase approach, only ingesting the index into the 2\.0
  KG to link to the actual source from there
- MatWerk
  - KG v1\.0 Research Information Graph
    - [https://demo\.fiz\-karlsruhe\.de/sparql](https://demo.fiz-karlsruhe.de/sparql)
      \(?\)
- NFDIcore is aligned to CERIF \(euroCRIS\)
- having decentral approach \(multiple federated KGs working together\)

Questions:

- Leyla Jael Castro ZB MED:
  - Hi, is the "information graph" mostly for metadata while the "data graph"
    for actual data content?
    - EP: infoGraph \-> having the reporting institutions in mind \(e\.g\.
      Libraries etc\)
      - and dataGraph coming from the data producing institutions
  - And, are you considering other than data resources? For instance, software
    or other research outcomes?
    - �
- Philip
  - How detailed is the research data info graph, in terms of when do you stop
    describing the content of the dataset?
    - Philip: Same Q was asked by Etienne\. This is a topic that needs to be
      addressed in a later WG call in the hope of finding a more common ground
      to answer it\. Having calls on certain ontology/terminology design
      patterns around top & mid\-level terms \(e\.g\. what is needed to describe
      a dataset & its associated assay or investigation\) seems to be the best
      way to tackle this\.
  - What are the reasons to stick to the W3C framework instead of other TLOs
    NFDIcore linked tightly to & MLOs?
  - RE: KG portal as a single point of access GUI for users to add data
    - Philip: in 4CHem we thought about harvesting this from the repos where the
      datasets are to be uploaded
- Mark Doerr
  - Which TripleStore and SPARQL endpoint are you using ? Do you have experience
    with openlink virtuoso, the wikidata engine ?
    - Virtuoso, old but dependable, does everything \(inferencing, linking to
      ref system\)
    - Wikidata uses Blazegraph, but Blazegraph has been abandoned \(last update
      3 years ago\)
    - Fuzeki: too hard/complex to configure because all is done in triples
    - Oxigraph \(RUST\), excellent Python integration
  - Which tools are you using to model the ontology ? Just protege ?
    - Protege
    - Mark Doerr�s suggestion: have a look at OWL2Ready for editing accessing
      ontologies from Python
      \([https://owlready2\.readthedocs\.io/en/latest/](https://owlready2.readthedocs.io/en/latest/)\)
    - Philip: you might also want to check out OAK
      \([https://github\.com/INCATools/ontology\-access\-kit](https://github.com/INCATools/ontology-access-kit)\)
- Marc Fuhrmans
  - Where do you have the more domain specific ontologies?
    - Etienne: in the extending modules, e\.g\.
      [MatWerk ontology](https://git.rwth-aachen.de/nfdi-matwerk/ta-oms/mwo)
      - Philip: We need to get the MatWerk consortium represented in our WG;
        e\.g\. to talk about their design patterns see
        [method](https://nfdi-matwerk.pages.rwth-aachen.de/ta-oms/mwo/doc/index.html#Method)
  - re [CGIF](https://docs.nfdi4culture.de/ta5-cgif-specification) format, why
    have a new format, if we could just link RDF
    - Etienne: because it�s hard to get RDF from the data provider partners, as
      they don�t have the resources to do so and plain old JSON is just more
      feasible\.
      - Philip: I guess the Schema\.org part of this is also one aspect of why
        this format is more attractive for these providers currently wrt the
        data being findable\.
- Paul Duchesne - It is not the most exciting area, but I was interested in how
  you have approached ontology governance\. How do you process/assess/make
  decisions around suggested changes, and how do you intend to manage "serious"
  ontology changes \(eg URI changes\)\. - Philip: Great question\! In
  [2023\-01\-26 WG Ontology Mapping and Harmonisation Meeting](https://docs.google.com/document/d/1roE_bnEPOHppTHNSscjPfP7pC3dpk1dIZUzpakANG54/)
  we had presentations of 4Chem & 4Cat in which this was partially addressed in
  terms of how this is done in these consortia\. But we haven't had the time to
  get into this in more detail in the WG from an NFDI wide perspective\. In the
  suggested topic section of
  the[Overview \- WG Ontology Harmonization & Mapping Meetings](https://docs.google.com/document/d/14z6kuAdVaiflWUtjqk3LKt-hqg_DeaRCpLY7TFo1PoU/edit#heading=h.8eim30vp5dll)
  you can see some topics that cover this partially\. Feel free to add/suggest a
  topic with some bullet points that cover what you want to discuss, so we can
  plan one or two sessions on this\. - 4Chem approach: using OBO best practices
  as most of our chemical ontologies are based on OBO framework - using Protege
  & ROBOT TSVs for editing managed by ODK for CI/CD \(versioning, release
  artifacts & docs\)  
  \-> example
  [VIBSO ](https://github.com/NFDI4Chem/VibrationalSpectroscopyOntology) -
  having monthly calls with domain experts to discuss domain specific new term
  requests \(NTRs\) and PRs - when there�s a need for more general terms then we
  do NTRs or PRs in the upstream ontologies \(e\.g\. CHMO, RXNO/MOP, OBI, IAO,
  �\)

## <a id="_k14senadzf3j"></a>

## <a id="_mr6t2f6boyc6"></a>Next Steps

- Leyla \(4Health?\) will prepare a short presentation about modeling concepts
  needed for data management
- agreed to do more calls on presenting design patterns around general terms,
  like processes/assays that create datasets \->
  [2023\-05\-10 \- WG Ontology Mapping & Harmonisation](https://docs.google.com/document/d/1H56_DYPSznnMwBVs20doFkm_HQ5zkXmf7YoGw86TcKU/edit)
