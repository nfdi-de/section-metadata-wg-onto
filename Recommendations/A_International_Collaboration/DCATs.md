# DCAT Application Profiles

This document gives some background on the W3 Data Catalog (DCAT) recommendation. It
deals with two parts:

1. the DCAT Vocabulary
2. DCAT application profiles

## DCAT

This is the vocabulary that defines what can be said about datasets,
dataset collections, dataset series, and data catalogs. It's a W3C standard,
but it does _not_ specify how the vocabulary should be used.

* [DCAT vocabulary](https://bioregistry.io/dcat)

## Institutional W3C DCAT Profiles

A DCAT **Application Profile** is about defining a closed world schema
that prescribes how to use the DCAT vocabulary. This defines which
classes must be present, which must be related to other classes, and in
what kind of ways. For instance, a `dcat:DataSet` must always be instantiated
with a title and description - the application profile concretizes these definitions.

Application profiles are the same as talking about shapes within knowledge graphs, versus
when we speak about vocabularies, this is an open world about what _can_ be said.

Profiles of W3C DCAT:

* [DCAT-AP (EU)](https://semiceu.github.io/DCAT-AP/releases/3.0.0/) this is the main one maintained by the W3C. It might sound generic, but DCAT-AP is the European version
* DCAT-US
* DCAT-UK

## Localized EU DCAT-AP Profiles

Profiles of EU DCAT-AP maintained by different entities.

* DCAT-AP-CZ
* DCAT-AP-DE
* DCAT-AP-IT
* DCAT-AP-SE
* DCAT-AP-SK

## Thematic EU DCAT-AP Profiles

Profiles of EU DCAT-AP maintained by SEMIC.

* BregDCAT-AP
* DCAT-AP HVD (High Value Datasets)
* GeoDCAT-AP
* HealthDCAT-AP
* MobilityDCAT-AP
* StatDCAT-AP

## Localized GeoDCAT-AP Profiles

* GeoDCAT-AP-CZ

## Unclear

* OGC GeoDCAT
