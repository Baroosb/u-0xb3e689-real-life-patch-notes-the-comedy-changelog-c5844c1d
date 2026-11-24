#!/usr/bin/env python3
"""Publish the one-line patch note stored next to this script.

The entry for this bounty lives in ``entry.txt`` in the same folder as
this file.  Running the program validates that text against the entry
rules and then copies it, byte for byte, into the output directory so
the grader can pick it up as the submitted patch note.
"""

import os
import sys
from pathlib import Path

# The note is a single short line, so anything outside this window is
# a sign the file was edited by accident rather than on purpose.
MIN_CHARS = 1
MAX_CHARS = 160
FALLBACK_OUTPUT_DIR = "/output"


def load_entry_bytes() -> bytes:
    """Return the raw bytes of the entry file sitting beside us."""
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    return entry_path.read_bytes()


def check_entry(raw: bytes) -> str:
    """Decode ``raw`` and make sure it obeys every rule for the note.

    Returns the decoded text on success and raises ``ValueError`` with
    an explanation as soon as any rule is broken.

    The checks mirror the bounty's entry gate on purpose: catching a
    bad note here, with a message that names the broken rule, is far
    friendlier than letting the grader reject a submission later for
    a reason nobody can see.  Order matters, too — decoding runs
    first because the length and line checks only make sense on text.
    """
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("entry.txt is not valid UTF-8") from exc
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must fit on exactly one line")
    if not text.strip():
        raise ValueError("entry must not be blank or whitespace only")
    return text


def destination() -> Path:
    """Work out where the published copy of the entry should land."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_OUTPUT_DIR
    return Path(folder) / "entry.txt"


def main() -> int:
    raw = load_entry_bytes()
    check_entry(raw)

    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)

    # Read the copy back: a silent short write would otherwise ship a
    # truncated note, so fail loudly if the bytes differ at all.
    if target.read_bytes() != raw:
        raise SystemExit("verification failed: output differs from entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
