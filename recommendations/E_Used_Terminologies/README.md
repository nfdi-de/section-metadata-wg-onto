# Objective E - NFDI’s Used Terminologies

GitHub Epic: https://github.com/nfdi-de/section-metadata-wg-onto/issues/32

The [Semantic Farm](https://semantic.farm) is a registry of ontologies,
terminologies, databases, and other resources that assign (persistent)
identifiers.

NFDI Section Metadata recommends that each NFDI consortium maintains a
collection in the Semantic Farm containing the ontologies that their members
produce and use.

For example, NFDI4Chem published a peer-reviewed research article
[Ontologies4Chem: the landscape of ontologies in chemistry](https://doi.org/10.1515/pac-2021-2007)
along with an accompanying collection
[0000014](https://semantic.farm/collection/0000014) on the Semantic Farm. While
the article is a static artifact from 2022, the collection has been updated
several times in the interim to reflect the evolving landscape in chemistry.

## Initialization

NFDI Section Metadata initially collected lists of ontologies for most NFDI
consortia in this
[Google Sheet](https://docs.google.com/spreadsheets/d/1UAfDKo2gKiaFldEeitMUcO8Gl1Fjyb_r_bp1V4JW0Es/edit?gid=3857951#gid=3857951).
We have begun to port some of them into the Semantic Farm, which typically
entails curating new records about the ontologies contained therein. This has
been done successfully for a handful of NFDI consortia, and we have created stub
collections for the rest.

## Maintenance Plan

After initial collections have been constructed, Section Metadata would like
consortia to assign one or more responsible contact persons who can be
periodically contacted for updates.

The collections can be updated by clicking "Add prefix to collection" in the
table below to be brought to an issue template on GitHub. This requires
[creating an account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
and
[creating an account on ORCiD](https://support.orcid.org/hc/en-us/articles/360006897454-How-do-I-register-for-an-ORCID-ID),
which are both free and can be done in a few minutes.

The Semantic Farm aims to implement automated ingestion of collections from
BARTOC. See
[this issue](https://github.com/biopragmatics/bioregistry/issues/1817).

## Opportunities

1. TS4NFDI could import collections from Semantic Farm, reducing the need for
   them to implement duplicate collection curations
2. Semantic Farm can be accessed programmatically and implicitly sets the
   standards for which metadata need to be collected about each ontology. This
   could reduce the burden on NFDI Section Metadata to create more
   recommendations, and ultimately support the NFDI consortia and their members
   in capturing important information
3. NFDI Section Metadata could create a dashboard for the NFDI directorate for
   reporting purposes

## Results

| Consortium                                                    |   # | Contact                                                  | Suggest                                                                                                                                                                           |
|---------------------------------------------------------------|-----|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [NFDI4Cat](https://semantic.farm/collection/0000011)          |  26 | Hendrik Borgelt, Alexander Behr, David Linke             | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000011&title=Add+prefix+X+to+NFDI4Cat)          |
| [NFDI4Chem](https://semantic.farm/collection/0000014)         |  51 | Philip Strömert                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000014&title=Add+prefix+X+to+NFDI4Chem)         |
| [KonsortSWD](https://semantic.farm/collection/0000020)        |  37 | Noemi Betancort                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000020&title=Add+prefix+X+to+KonsortSWD)        |
| [NFDI4Energy](https://semantic.farm/collection/0000021)       |  17 | Amanda Wein                                              | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000021&title=Add+prefix+X+to+NFDI4Energy)       |
| [NFDI4ING](https://semantic.farm/collection/0000022)          | 102 |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000022&title=Add+prefix+X+to+NFDI4ING)          |
| [DataPLANT](https://semantic.farm/collection/0000023)         |  38 | Kathryn Dumschott, Angela Kranz, Hannah Dörpholz         | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000023&title=Add+prefix+X+to+DataPLANT)         |
| [FAIRmat](https://semantic.farm/collection/0000024)           |   4 |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000024&title=Add+prefix+X+to+FAIRmat)           |
| [NFDI4Culture](https://semantic.farm/collection/0000025)      |  26 | Tabea Tietz                                              | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000025&title=Add+prefix+X+to+NFDI4Culture)      |
| [DAPHNE4NFDI](https://semantic.farm/collection/0000026)       |     |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000026&title=Add+prefix+X+to+DAPHNE4NFDI)       |
| [MaRDI](https://semantic.farm/collection/0000027)             |   8 | Björn Schembera                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000027&title=Add+prefix+X+to+MaRDI)             |
| [BERD@NFDI](https://semantic.farm/collection/0000028)         |     |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000028&title=Add+prefix+X+to+BERD@NFDI)         |
| [NFDI4DataScience](https://semantic.farm/collection/0000029)  |     |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000029&title=Add+prefix+X+to+NFDI4DataScience)  |
| [NFDI4Earth](https://semantic.farm/collection/0000030)        |  27 | Auriol Degbelo                                           | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000030&title=Add+prefix+X+to+NFDI4Earth)        |
| [NFDI-MatWerk](https://semantic.farm/collection/0000031)      |   6 | Ebrahim Nourouzi, Heike Fliegl                           | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000031&title=Add+prefix+X+to+NFDI-MatWerk)      |
| [PUNCH4NFDI](https://semantic.farm/collection/0000032)        |     |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000032&title=Add+prefix+X+to+PUNCH4NFDI)        |
| [FAIRagro](https://semantic.farm/collection/0000033)          |  23 |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000033&title=Add+prefix+X+to+FAIRagro)          |
| [NFDI4BIOIMAGE](https://semantic.farm/collection/0000034)     |  22 | Damien Goutte-Gattat                                     | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000034&title=Add+prefix+X+to+NFDI4BIOIMAGE)     |
| [NFDIxCS](https://semantic.farm/collection/0000035)           |     |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000035&title=Add+prefix+X+to+NFDIxCS)           |
| [NFDI4Objects](https://semantic.farm/collection/0000036)      |  47 | Jakob Voß, Anja Gerber, Florian Thiery, Kristina Fischer | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000036&title=Add+prefix+X+to+NFDI4Objects)      |
| [NFDI4Memory](https://semantic.farm/collection/0000037)       |  21 | Tabea Tietz                                              | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000037&title=Add+prefix+X+to+NFDI4Memory)       |
| [Text+](https://semantic.farm/collection/0000038)             |  14 |                                                          | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000038&title=Add+prefix+X+to+Text+)             |
| [GHGA](https://semantic.farm/collection/0000039)              |  12 | Karoline Mauer                                           | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000039&title=Add+prefix+X+to+GHGA)              |
| [NFDI4Biodiversity](https://semantic.farm/collection/0000040) |  65 | Naouel Karam, Ralph Schäfermeier                         | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000040&title=Add+prefix+X+to+NFDI4Biodiversity) |
| [NFDI4Health](https://semantic.farm/collection/0000041)       |     | Matthias Löbe                                            | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000041&title=Add+prefix+X+to+NFDI4Health)       |
| [NFDI4Microbiota](https://semantic.farm/collection/0000042)   |     | Anandhi Iyappan, Noriko Cassman, Maja Magel              | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000042&title=Add+prefix+X+to+NFDI4Microbiota)   |
| [NFDI4Immuno](https://semantic.farm/collection/0000043)       |     | Ulrik Stervbo, Sebastian Böhm                            | [Add prefix to collection](https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection=0000043&title=Add+prefix+X+to+NFDI4Immuno)       |

Regenerate this chart with `uv run generate_table.py`.
