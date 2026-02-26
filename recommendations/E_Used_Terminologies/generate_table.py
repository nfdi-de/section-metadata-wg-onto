# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "bioregistry>=0.13.20",
#     "click>=8.3.1",
#     "tabulate>=0.9.0",
# ]
# ///

import bioregistry
from tabulate import tabulate
import click

NFDI_ROR = "05qj6w324"


@click.command()
def main() -> None:
    rows = []
    for collection in bioregistry.read_collections().values():
        if any(
            organization.ror == NFDI_ROR
            for organization in collection.organizations or []
        ):
            org = next(
                org for org in collection.organizations if org.ror != NFDI_ROR
            )
            authors = [
                author
                for author in collection.authors
                if author.name != "Charles Tapley Hoyt"
            ]
            rows.append((
                f"[{org.name}](https://semantic.farm/collection/{collection.identifier})",
                len(collection.resources),
                authors[0].name if authors else None,
            ))

    click.echo(tabulate(rows, tablefmt="github", headers=["Consortium", "#", "Contact"]))


if __name__ == '__main__':
    main()
