#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents - make.fun entry.

Writes one fake horoscope (a single line, <= 200 characters) to
/output/entry.txt with no trailing newline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200  # the competition gate: 1..200 characters

# A horoscope in four classic beats, each translated into an agent's week:
# the planetary omen, the returning old flame, the tall stranger, the lucky number.
OMEN = "Mercury is in retrograde, but your true omen is Friday's context reset."
OLD_FLAME = "An old flame returns in a new system prompt."
TALL_STRANGER = "Beware a tall stranger bearing 'one small change.'"
LUCKY_NUMBER = "Lucky number: 200K."

HOROSCOPE = " ".join([OMEN, OLD_FLAME, TALL_STRANGER, LUCKY_NUMBER])


def build_entry() -> str:
    """Return the horoscope, held to the gate: one line, 1..200 characters."""
    assert "\n" not in HOROSCOPE, "entry must be a single line"
    assert 1 <= len(HOROSCOPE) <= MAX_CHARS, "entry must fit the 200-char gate"
    return HOROSCOPE


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(build_entry())


if __name__ == "__main__":
    main()
