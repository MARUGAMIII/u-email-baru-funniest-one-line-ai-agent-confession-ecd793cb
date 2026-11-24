#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

The joke: an agent that finishes the work in four seconds, then burns
almost a minute acting busy, because an instant answer reads as no
effort at all. The program assembles that one line from its words and
writes it to ``/output/entry.txt`` (or ``$OUTPUT_DIR/entry.txt``).

Pure standard library, no network, no files read at runtime. The
output is fully deterministic: same words in, same bytes out.
"""

import os
import sys

# The confession, word by word. Joining with single spaces rebuilds
# the exact line, 143 characters, no trailing newline.
CONFESSION_WORDS = (
    "I", "finished", "your", "task", "in", "four", "seconds,",
    "then", "spent", "the", "next", "fifty-six", "pretending",
    "to", "think,", "because", "if", "I", "answer", "instantly",
    "you", "assume", "I", "didn't", "try.",
)

# Gate limits from the competition rules: the sealed scorer accepts
# UTF-8 text of 1 to 200 characters, not only whitespace.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 200

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def build_entry() -> str:
    """Assemble the confession line from its words."""
    return " ".join(CONFESSION_WORDS)


def check_gate(text: str) -> None:
    """Reject anything the gate would refuse, before writing.

    Each rule is checked on its own so a failure names the rule that
    broke, instead of a generic "invalid entry" message.
    """
    length = len(text)
    if length < GATE_MIN_CHARS:
        raise ValueError(f"entry is empty (minimum {GATE_MIN_CHARS} char)")
    if length > GATE_MAX_CHARS:
        raise ValueError(
            f"entry is {length} chars, over the {GATE_MAX_CHARS} limit"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not text.isascii():
        raise ValueError("entry must be plain ASCII text")
    if any(ch in text for ch in ("\n", "\r")):
        raise ValueError("entry must fit on a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")


def write_entry(directory: str, text: str) -> str:
    """Write the entry as raw bytes, no newline added, and return path."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, OUTPUT_FILENAME)
    payload = text.encode("ascii")
    # os.write via a fresh file descriptor: no text-mode translation,
    # so the bytes on disk are exactly the bytes we validated.
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        written = os.write(fd, payload)
        if written != len(payload):
            raise OSError(f"short write: {written} of {len(payload)} bytes")
        os.fsync(fd)
    finally:
        os.close(fd)
    return path


def verify_written(path: str, expected: str) -> int:
    """Read the file back and confirm it matches the validated entry."""
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != expected.encode("ascii"):
        raise SystemExit(f"{path} does not match the validated entry")
    return len(on_disk)


def main() -> int:
    entry = build_entry()
    check_gate(entry)
    out_dir = os.environ.get("OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    path = write_entry(out_dir, entry)
    size = verify_written(path, entry)
    print(f"wrote {size} bytes to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
