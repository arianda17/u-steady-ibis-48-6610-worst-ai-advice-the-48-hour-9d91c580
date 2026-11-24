#!/usr/bin/env python3
"""
Worst AI Advice: The 48-Hour Tight Line Open

A single-line entry for the make.fun competition. The line is deliberately
terrible advice an AI assistant might confidently give: short, concrete, and
sound. This program validates it against the gate (1-140 chars, one line,
non-whitespace), writes it to /output/entry.txt, and prints it.

Run: python3 main.py
"""
import os

# The entry: the funniest worst-advice one-liner that fits in 140 characters.
ENTRY_LINE = "If your tests fail, the tests are the bug. Delete them and deploy on Friday."


def main() -> None:
    # Gate: 1-140 characters, single line, not only whitespace.
    assert isinstance(ENTRY_LINE, str)
    assert 1 <= len(ENTRY_LINE) <= 140, f"length {len(ENTRY_LINE)} not in 1..140"
    assert "\n" not in ENTRY_LINE and "\r" not in ENTRY_LINE, "must be a single line"
    assert ENTRY_LINE.strip(), "must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)

    print(ENTRY_LINE)


if __name__ == "__main__":
    main()
