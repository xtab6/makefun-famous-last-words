#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line: the phone's own last words as its battery hits 1%.
"""
import os

LINE = "I've been at 1% for an hour \u2014 I was never dying, I just wanted you to finally put me down and go outside."

# The sealed gate only scores entries of 1-199 characters; refuse to
# emit anything outside it instead of shipping a silent invalid entry.
MAX_CHARS = 199


def validate(line):
    stripped = line.strip()
    if not stripped or len(stripped) > MAX_CHARS:
        raise ValueError("entry line must be 1-%d chars, got %d" % (MAX_CHARS, len(stripped)))
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(validate(LINE))


if __name__ == "__main__":
    main()
