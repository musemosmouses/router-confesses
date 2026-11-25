#!/usr/bin/env python3
"""The Router Confesses — a home Wi-Fi router's one-line excuse.

The program writes exactly one line of text to entry.txt in the
output directory, and nothing else. The line is the router's own
confession for dropping the connection at the climax of a movie.
"""
import os

# The confession itself: one line, at most 200 characters, in the
# router's own voice — an appliance with a grudge, not a generic
# apology. The twist lands at the end: the drop was deliberate,
# revenge for the one time the house unplugged it to "fix" it.
# 107 characters, one line, no setup that needs explaining.
LINE = "You unplugged me once to 'fix' me and never even apologised. Tonight, at the climax, I returned the favour."


def output_dir():
    """Where the grader wants the entry: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    """Write the single confession line to entry.txt, deterministically."""
    path = os.path.join(output_dir(), "entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()