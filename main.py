#!/usr/bin/env python3
"""Snooze Button Roast entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. Stdlib only, no network, no randomness: the line is
fixed so the program is deterministic.
"""

import os

LINE = (
    "My alarm clock rang at 6 AM on a Saturday like a debt collector "
    "who knows I am home, except the only thing I owe it is eight more "
    "hours of sleep."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    assert text == text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
