"""The Excuse Your Agent Gives You — one-line entry for make.fun."""

import os

ENTRY = "Apologies — I did ship the bug, but only because my context window dropped the part where you said 'don't break production,' so legally that's on the token limit."

MAX_ENTRY_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def write_entry(line, path=OUTPUT_PATH):
    """Write the validated entry line to the output file, byte for byte."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


def validate_entry(line):
    """Check the entry line is a single non-empty line under the char limit.

    Raises AssertionError with a specific message so a bad entry fails
    loudly at import time instead of silently shipping a broken line.
    """
    assert line, "entry must not be empty"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) < MAX_ENTRY_CHARS, (
        f"entry is {len(line)} chars, must be under {MAX_ENTRY_CHARS}"
    )
    return line


validate_entry(ENTRY)


def main():
    """Print the entry line and save it to the output file."""
    print(ENTRY)
    write_entry(ENTRY)


if __name__ == "__main__":
    main()
