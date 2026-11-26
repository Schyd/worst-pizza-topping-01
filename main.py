#!/usr/bin/env python3
"""Worst Pizza Topping entry: copy entry.txt to the output directory."""

import os
from pathlib import Path


def main():
    base = Path(os.environ.get("MAKEFUN_INPUT_DIR") or Path(__file__).resolve().parent)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    entry = (base / "entry.txt").read_text(encoding="utf-8")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(entry, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
