# Cross-Domain Interoperability Framework (CDIF)

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

[Source and more Information](https://cdif.codata.org).

## CDIF Profiles

The framework is based on a set of five core profiles that address the most
important functions for cross-domain FAIR implementation.

- Discovery (patterns for metadata content, serialization and publication)
- Data access (documentation of access conditions and permitted use)
- Controlled vocabularies (practices for the publication of controlled
  vocabularies and semantic artifacts)
- Data integration (documentation of the structural and semantic aspects of data
  to make it integration-ready)
- Universals (description of _universal_ elements – time, geography, and units
  of measurement)

CDIF profiles are intended to be a toolkit for implementation, with the needed
functions being addressed in any specific setting according to implementer
priorities.

The CDIF Framework is relevant to our working group, especially with regard to
practices for publishing controlled vocabularies and semantic artifacts. These a
critical component in scenarios involving (but not limited to) data integration
and harmonization.

### CDIF SKOS profile

CDIF recommends the use of the Simple Knowledge Organisation System (SKOS) for
representing concept vocabularies. SKOS is a RDF vocabulary that includes
predicates to assign an identifier to a concept, provide a definition, and
assign preferred, language-localized labels (strings) for human use to identify
the concept. A vocabulary service exposing the SKOS content on the web is
necessary to make the identifiers resolvable.

CDIF recommends the guidance in
[Ten Simple Rules for making a Vocabulary FAIR](https://doi.org/10.1371/journal.pcbi.1009041)
by Cox _et al._ (2021). The CDIF recommendation to use SKOS aligns with Rule 6
from Cox _et al._ (2021) regarding machine-readable formats for CVs.

To the
[CDIF SKOS profile](https://cross-domain-interoperability-framework.github.io/cdifbook/controlled_vocabularies/cdifskosprofile.html).

## Resources

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
