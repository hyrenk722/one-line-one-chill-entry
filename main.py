#!/usr/bin/env python3
"""one-line-one-chill entry (Python 3, standard library only).

Writes one fixed line of horror to /output/entry.txt. The gate takes
UTF-8 text of 1 to 200 characters that is not only white space, and the
judge reads exactly the bytes written, so the line below carries no
trailing line end.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

ENTRY = "The handwriting in my diary changed three weeks ago, and I have not missed a single day."

# The gate refuses anything outside 1-200 characters, so fail loudly
# here instead of shipping a bad file.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
