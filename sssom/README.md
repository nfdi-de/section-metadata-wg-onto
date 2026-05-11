# SSSOM Curator

## Workflows

Predict new mappings, e.g., between Medical Subject Headings (MeSH)
and the Medical Actions Ontology (MaxO) with:

```console
$ uv run main.py predict lexical mesh maxo
```

Run the curator with:

```console
$ uv run main.py web
```

### Export

Output summary charts and tables with:

```console
$ mkdir output/
$ uv run main.py summarize --output-directory output/
```

Merge the positive, negative, and predicted mappings together
and output several SSSOM flavors (TSV, OWL, JSON) in a given directory with:

```console
$ mkdir sssom/
$ uv run main.py merge --sssom-directory sssom/
```

### Maintenance

Format/lint the mappings with:

```console
$ uv run main.py lint
```

Test the integrity of mappings with:

```console
$ uv run main.py test
```

## License

Semantic mappings curated in this directory are licensed under the
[Creative Commons Zero v1.0 Universal (CC0-1.0) License](https://creativecommons.org/publicdomain/zero/1.0/legalcode).

## Colophon

This repository was generated using [SSSOM-Curator](https://github.com/cthoyt/sssom-curator).
