"""One-line roast: the gadget I use every day.

Writes a single original roast line to /output/entry.txt.
Pure Python stdlib, deterministic, no input, no network.
"""

import os

ROAST = (
    "My smart kettle asked for a firmware update before it would boil "
    "water, so my morning tea now has a loading screen."
)


def main():
    line = ROAST.strip()
    assert len(line) <= 200, "roast line must be at most 200 characters"
    assert "\n" not in line, "roast must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
