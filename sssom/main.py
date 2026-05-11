#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "sssom-curator[web,predict-lexical,exports]",
# ]
# ///

"""SSSOM Curator for sssom."""

from sssom_curator import Repository
from pathlib import Path

HERE = Path(__file__).parent.resolve()

repository_path = HERE.joinpath("sssom-curator.json")
repository = Repository.model_validate_json(repository_path.read_text())

if __name__ == "__main__":
    repository.run_cli()
