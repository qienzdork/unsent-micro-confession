#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint -- entry program.

Writes one two-part micro-confession to /output/entry.txt
(or $ENTRY_OUTPUT when set, for local validation).
Python standard library only; output is a fixed constant, so every
run is byte-identical.
"""

import os

ENTRY = (
    "To: Sarah\n"
    "I still have the draft that says I was the one who broke your mug, "
    "not the cat, and I am sorry I let you blame her for a year."
)


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
