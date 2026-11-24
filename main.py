#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry -- one single-line safety warning label for every
human being -- to /output/entry.txt.

Gate (from the bounty kit RULES.txt): /output/entry.txt must be UTF-8
text of 1 to 160 characters, not only white space. The entry is also
kept to a single line, as the task requires.
"""

from pathlib import Path

ENTRY = (
    "WARNING: This human runs on caffeine and spite, overheats in "
    "meetings, and will shut down without warning if asked to hop "
    "on a quick call."
)

OUTPUT_PATH = Path("/output/entry.txt")


def gate_check(text: str) -> None:
    """Enforce the exact gate: 1-160 chars, UTF-8, not whitespace-only."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")  # raises UnicodeEncodeError if not UTF-8 encodable
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing white space")
    if not text.startswith("WARNING:"):
        raise ValueError("entry must read as a warning label")


def main() -> None:
    gate_check(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    print(ENTRY)


if __name__ == "__main__":
    main()
