"""wordfreq‑tiny
A single‑module CLI that prints word frequencies from a text file.
Usage:
    python -m wordfreq <path-to-text>
"""

import argparse
import collections
import re
import sys
from pathlib import Path


def load_text(path: Path) -> str:
    """Read the file as UTF‑8, exit with an error on failure.
    """
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:
        sys.stderr.write(f"Error reading {path}: {exc}\n")
        sys.exit(1)


def tokenize(text: str) -> list[str]:
    """Return a list of lowercase words, ignoring punctuation.
    """
    # Simple word matcher – alphanumerics + apostrophe inside words
    return re.findall(r"\b[\w']+\b", text.lower())


def count_frequencies(words: list[str]) -> collections.Counter:
    """Return a Counter mapping word → frequency.
    """
    return collections.Counter(words)


def main() -> None:
    parser = argparse.ArgumentParser(description="Count word frequencies in a text file.")
    parser.add_argument("path", type=Path, help="Path to the input text file")
    args = parser.parse_args()

    text = load_text(args.path)
    words = tokenize(text)
    freq = count_frequencies(words)

    for word, count in freq.most_common():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
