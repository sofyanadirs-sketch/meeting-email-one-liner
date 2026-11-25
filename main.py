#!/usr/bin/env python3
"""Entry for make.fun bounty u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.

Writes a single one-line joke about a meeting that should have been an
email to /output/entry.txt (1-200 characters, plain text, one line).
"""

import os

JOKE = "Nine people dialled in to hear the boss read aloud the email he had already sent us all that morning."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
