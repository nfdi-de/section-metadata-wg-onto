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
            org = next(org for org in collection.organizations if org.ror != NFDI_ROR)
            authors = [
                author
                for author in collection.authors
                if author.name != "Charles Tapley Hoyt"
            ]

            name_plus = org.name.replace(" ", "+")
            suggest_link = f"https://github.com/biopragmatics/bioregistry/issues/new?template=add-collection-prefix.yml&collection={collection.identifier}&title=Add+prefix+X+to+{name_plus}"

            rows.append(
                (
                    f"[{org.name}](https://semantic.farm/collection/{collection.identifier})",
                    len(collection.resources),
                    authors[0].name if authors else None,
                    f"[Add prefix to collection]({suggest_link})",
                )
            )

    if len(rows) != 26:  # as of feb 2026
        raise ValueError(f"missing some NFDI consortia, only found {len(rows)}")

    table = tabulate(
        rows, tablefmt="github", headers=["Consortium", "#", "Contact", "Suggest"]
    )
    click.echo(table)
    click.echo("\nthis table has been copied to your clipboard")
    pyperclip.copy(table)


if __name__ == "__main__":
    main()
