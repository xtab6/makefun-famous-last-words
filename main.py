#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line: the phone's own last words as its battery hits 1%.
"""
import os

LINE = "I've been at 1% for an hour \u2014 I was never dying, I just wanted you to finally put me down and go outside."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
