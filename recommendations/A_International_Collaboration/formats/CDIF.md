---
layout: page
title: Cross-Domain Interoperability Framework (CDIF)
permalink: /objective/A/formats/cdif
---

This document gives some background information on the Cross-Domain
Interoperability Framework (CDIF), based on existing standards (Schema.org,
DCAT, ODRL, DDI-CDI, SKOS/XKOS, SSSOM, etc.) and technology to support
interoperability in both human- and machine-actionable fashion.

Its approach is not to create mappings from every existing domain to another,
but to create a _lingua franca_ that we can all agree on and communicate with.

Therefore, CDIF is a set of implementation recommendations, based on profiles of
common, domain-neutral metadata standards which are aligned to work together to
support core functions required by FAIR.

The usage of the standards is e.g.:

- Understand data structure (DDI-CDI)
- Understand semantics (SKOS/XKOS, OWL, SSSOM)
- Determine origination/context (PROV-O, I-ADOPT/O&M)

## CDIF Profiles

The framework is based on a set of five core profiles that address the most
important functions for cross-domain FAIR implementation by providing core
metadata fields useful in all domains and infrastructures.

- Discovery, Cataloguing, and Dissemination (F) : Search, indexing, and
  packaging.
- Controlling Data Access (A) : Data confidentiality, access, and permitted use.
- Data Description, Use, and Integration (F, A, I, R) : Structure and Semantics
  (including semantic artifacts and mappings).
- Characterizing Data/Provenance and Process, Quality (I, R)
- Universals: Time, Geography, and Units of Measure (F, I, R) : Administration
  and common expression

Each of these profiles is supported by specific recommendations, including the
set of metadata fields in specific standards to use, and the method of
implementation to be employed for machine-level interoperability.

The CDIF Framework is relevant to our working group, especially with regard to
practices for
[publishing controlled vocabularies and semantic artifacts](https://cross-domain-interoperability-framework.github.io/cdifbook/controlled-vocabularies/vocabintro/).
These are a critical component in scenarios involving (but not limited to) data
integration and harmonization.

It is recognized that transformations to both data and metadata at several
levels are a critical part of data integration. The mappings used to inform
transformations are a critical aspect of this, being both needed provenance
information and also potentially providing a
[reusable FAIR resource](https://cross-domain-interoperability-framework.github.io/cdifbook/future/fairmappings/)
in their own right. This issue also falls within the scope of our group’s work,
and we will take its recommendations into account when formulating our own
recommendations for the NFDI regarding mappings.

## CDIF Version 1.1

Version 1.1 of the Cross-Domain Interoperability Framework (CDIF) was released
on June 2, 2026, and can be found at <https://cdif.codata.org/>.

Version 1.1 represents a substantial enhancement of the CDIF recommendations,
with increased support for FAIR functional requirements, and a new technical
approach, featuring validation tools and improved documentation.

While a significant step forward, resulting from two years of implementation and
further development since
[the initial CDIF release in May 2024](https://doi.org/10.5281/zenodo.11236871),
version 1.1 is also forward-looking: the CDIF4EOSC project started on 1 June
2026 (see below), and will drive the next major round of CDIF developments. To
support this, improvements to date have been consolidated in version 1.1 and
will provide a baseline for further developments led by the CDIF4EOSC project.

Changes in the scope and coverage of CDIF are:

- Identification of a set of
  [Core fields](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/core/),
  for use in all profiles
- Addition of support for binary data file such as HDF5, NetCDF, and Parquet
- Inclusion of the
  [Manifest profile](https://cross-domain-interoperability-framework.github.io/cdifbook/manifest/manifest/),
  to enable packaging of resources into FAIR Digital Objects (FDOs) using RO
  Crate or similar packaging technologies
- Reorganization of the
  [Data Description profile](https://cross-domain-interoperability-framework.github.io/cdifbook/data-description/datadescriptionprofile/)
  to cover the publication of reusable data structure descriptions and variables
  with DDI-CDI
- Increased nuance in the description of controlled vocabularies with SKOS:
  [Codelist](https://cross-domain-interoperability-framework.github.io/cdifbook/controlled-vocabularies/codelistprofile/)
  and
  [Concept Scheme](https://cross-domain-interoperability-framework.github.io/cdifbook/controlled-vocabularies/conceptprofile/)
  profiles express the difference between lists of enumerated values used in
  data, and broader semantic resources

### Resources

[Source of this information and current updates](https://cdif.codata.org).

[CDIF in GitHub](https://github.com/Cross-Domain-Interoperability-Framework)

_Gregory, A. et al. (2024). WorldFAIR (D2.3) Cross-Domain Interoperability
Framework (CDIF) (Report Synthesising Recommendations for Disciplines and
Cross-Disciplinary Research Areas) (Version 1). Zenodo.
<https://doi.org/10.5281/zenodo.11236871>_

_Hodson, Simon; Gregory, Arofan: The WorldFAIR project. HMC FAIR Friday,
Helmholtz Metadata Collaboration, 2023. <https://doi.org/10.5446/66247>_

Webinar
<https://codata.org/the-cross-domain-interoperability-framework-cdif-practical-guidelines-for-fair-interoperability-webinar-25-july/>
([Recordings](https://vimeo.com/991198957))

[2024-06-12 CDIF Presentation at the WG meeting](https://docs.google.com/presentation/d/16F6WgQuYxAfKz77-7Pv3cjokPJtcj7nJ/)
(Google Doc) and
[Recording](https://drive.google.com/file/d/1aUONsKUxlt8eqqn5pL1XhR7fBhu-bvP8/view?usp=drive_link)

[CDIF Metadata Crosswalks](https://docs.google.com/spreadsheets/d/1wFuJ4RRlNirnrPfuY_d57I9_pnaNibw4nltNTkruSp0/edit?gid=1784126572#gid=1784126572)
(Google Doc).

## The CDIF4EOSC project (1 Jun 2026 - 31 May 2029)

The CDIF4EOSC project, coordinated by CODATA, started on 1 June 2026 and will
extend the CDIF recommendations, adding profiles, guidelines, and use case
examples to form a comprehensive playbook for FAIR integration in the European
Open Science Cloud (EOSC) and beyond.

### Internal Points of Contact

[Heike Görzig](https://orcid.org/0000-0001-9121-8643),
[Noemi Betancort](https://orcid.org/0000-0002-0156-3556)

### Connected NFDI Consortia

[To be updated]

### External Contacts

[Simon Hodson](https://orcid.org/0000-0003-3179-7270) (Project Coordinator,
Executive Director of CODATA)

### Links

Webseite: <https://www.cdif4eosc.eu/>

Project-DOI: <https://doi.org/10.3030/101292473>

E-Mail: <cdif-feedback@codata.org>
