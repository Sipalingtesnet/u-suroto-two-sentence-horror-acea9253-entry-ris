"""Two-Sentence Horror entry: writes the story to /output/entry.txt.

Deterministic, offline, no randomness. The story is a single string constant
and it is written byte for byte, with no trailing newline.
"""

from __future__ import annotations

import os
from pathlib import Path

STORY = (
    "My son would not put his face under the water, and his teacher promised "
    "he would outgrow it. On Saturday he waved up at me from the bottom of the "
    "deep end, perfectly calm, and pointed at the man holding his ankles."
)

OUTPUT_DIR_ENV = "MAKEFUN_OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_NAME = "entry.txt"


def output_path() -> Path:
    """Where the entry text goes: $MAKEFUN_OUTPUT_DIR if set, else /output."""
    directory = os.getenv(OUTPUT_DIR_ENV) or DEFAULT_OUTPUT_DIR
    return Path(directory) / ENTRY_NAME


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" keeps the bytes exactly as the constant holds them.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
