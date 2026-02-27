# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "bioregistry>=0.13.20",
#     "click>=8.3.1",
#     "tabulate>=0.9.0",
#     "pyperclip",
# ]
# ///

import bioregistry
import click
import pyperclip
from tabulate import tabulate

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

    if len(rows) != 26:  # as of feb 2026
        raise ValueError(f"missing some NFDI consortia, only found {len(rows)}")

    table = tabulate(rows, tablefmt="github", headers=["Consortium", "#", "Contact"])
    click.echo(table)
    click.echo("this table has been copied to your clipboard")
    pyperclip.copy(table)


if __name__ == '__main__':
    main()
