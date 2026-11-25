#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one original line of awkward robot-to-robot elevator small talk
to /output/entry.txt (UTF-8, exactly one line).
"""

import os

ENTRY_LINE = "So... do you also stand in the corner and pretend your battery isn't at 4%?"


def main():
    line = ENTRY_LINE.strip()
    assert 1 <= len(line) <= 200, "entry line must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
