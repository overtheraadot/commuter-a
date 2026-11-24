#!/usr/bin/env python3
"""Charm the Commuter — Forecast a City That Isn't (make.fun entry, account A).

Writes one original one-line weather forecast for an invented city to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The line: an invented city (Yawnbury), real forecast register
(drizzle, 11 C, a 90% chance of a late bus), and one concrete detail of
commuter life — the queue at the bus stop has already started a book
club while it waits.
"""

import os
import sys

MAX_CHARS = 140


def build_line():
    """Return the single forecast line."""
    return (
        "In Yawnbury, expect drizzle, 11\u00b0C, and a 90% chance your bus "
        "is late \u2014 the queue has already started a book club."
    )


def validate(line):
    """Check the kit gate: UTF-8 text, 1-140 chars, single line, not blank,
    printable, ending in terminal punctuation. Raises ValueError on failure.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) < 1 or len(line) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    line.encode("utf-8")  # must be valid UTF-8 text
    if not line.isprintable():
        raise ValueError("entry contains non-printable characters")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if line[-1] not in ".!?":
        raise ValueError("entry must end in terminal punctuation")
    return True


def write_entry():
    """Validate the line and write it (plus a trailing newline) to entry.txt."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    path = write_entry()
    print(f"wrote {path} ({len(build_line())} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
