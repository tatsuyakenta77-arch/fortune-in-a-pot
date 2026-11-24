#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes one kind, funny fortune for the houseplant on the windowsill to
/output/entry.txt. The fortune is a single fixed line: deterministic, so
every run produces byte-identical output.
"""

import os

FORTUNE = (
    "Soon you will outgrow this pot, this windowsill, and each plant "
    "the neighbours brag about \u2014 politely, of course."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character, and the
    # fortune itself is exactly 112 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)
    print(f"Wrote {len(FORTUNE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
