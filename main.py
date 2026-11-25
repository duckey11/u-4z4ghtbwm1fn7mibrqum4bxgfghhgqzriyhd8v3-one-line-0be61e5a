#!/usr/bin/env python3
"""One Line, One Laugh.

Writes a single self-contained funny line to entry.txt.
Deterministic: every run writes exactly the same bytes.
Python standard library only; no network, no secrets.
"""

import os

LINE = "My cheap umbrella flips inside out in the wind, so I now own a very small, very wet kite."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
