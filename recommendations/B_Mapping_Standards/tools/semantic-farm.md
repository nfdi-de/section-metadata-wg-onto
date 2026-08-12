# Semantic Farm

The [Semantic Farm](https://semantic.farm) is an open source, domain-agnostic,
community curated semantic space registry, meta-registry, and compact identifier
resolver where all NFDI ontologies, terminologies, databases, and related
resources
[should be indexed](../../D_Development_Best_Practices/README.md#terminology-hosting-and-indexing).

Here's what that means:

1. **Registry** A collection of prefixes and metadata for ontologies,
   terminologies, and other resources that assign (persistent) identifiers. Some
   other well-known registries are [Identifiers.org](https://identifiers.org)
   (originally for the life sciences), and the [BARTOC](https://bartoc.org)
   (originally for the humanities).
2. **Metaregistry** A collection of metadata about registries and mappings
   between their constituent prefixes.
3. **Resolver** A tool for mapping
   [compact URIs (CURIEs)](https://www.w3.org/TR/2010/NOTE-curie-20101216/) of
   the form `prefix:identifier` to HTML and structured content providers
4. **Open Source** Anyone can
   [suggest improvements](https://github.com/biopragmatics/bioregistry/issues/new/choose)
   or make pull requests to update the underlying database, which is stored in
   [JSON on GitHub](https://github.com/biopragmatics/bioregistry/blob/main/src/bioregistry/data/bioregistry.json)
   where the community can engage in an open review process.
5. **Domain Agnostic** The concept behind the Semantic Farm was first piloted in
   the biomedical community with [the Bioregistry](https://bioregistry.io). Now,
   the underlying technology is fully generic for all domains including
   engineering, humanities, and beyond.
6. **Community** Governed by public, well-defined
   [contribution guidelines](https://github.com/biopragmatics/bioregistry/blob/main/docs/CONTRIBUTING.md),
   [code of conduct](https://github.com/biopragmatics/bioregistry/blob/main/docs/CODE_OF_CONDUCT.md),
   and
   [project governance](https://github.com/biopragmatics/bioregistry/blob/main/docs/GOVERNANCE.md)
   to promote the project's inclusivity and longevity.

## Artifacts

- Source code (https://github.com/biopragmatics/bioregistry/)
- Website (https://semantic.farm/)
- API Documentation (https://semantic.farm/docs)

## Comparison to BARTOC

The
[Basic Registry of Thesauri, Ontologies, and Classifications (BARTOC)](https://bartoc.org)
captures similar metadata to the Semantic Farm for resources that assign
identifiers. The Semantic Farm imports records from BARTOC on a weekly basis,
after which they're enriched by Semantic Farm community curators with additional
metadata and narrative text to best support NFDI researchers in finding,
accessing, and reusing the ontologies, terminologies, controlled vocabularies,
and other resources contained within.

For a more detailed comparison of when to use the Semantic Farm or BARTOC, see
[here](../../D_Development_Best_Practices/semantic-farm-and-bartoc.md).

## Training Material

- [New Prefix Guidelines](https://github.com/biopragmatics/bioregistry/blob/main/docs/CONTRIBUTING.md)
- [New Prefix Tutorial](https://www.youtube.com/watch?v=e-I6rcV2_BE&t=3s&pp=ygULYmlvcmVnaXN0cnnSBwkJogoBhyohjO8%3D)

## Publications

- [Unifying the identification of biomedical entities with the Bioregistry](https://doi.org/10.1038/s41597-0)
