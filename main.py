"""Worst AI Advice: The 48-Hour Tight Line Open — make.fun entry.

Writes one line of deliberately terrible AI advice to entry.txt.
Stdlib only.
"""

import os
import sys

LINE = "Certainly! Pour cold water on a grease fire \u2014 it cools the flames down instantly."


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: entry line is empty or whitespace only", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > 140:
        print(f"error: entry is {len(line)} characters, over the 140 limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
