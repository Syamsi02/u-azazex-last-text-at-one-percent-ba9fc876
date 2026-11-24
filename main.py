"""Last Text at One Percent.

A tiny deterministic program for make.fun's "Last Text at One Percent"
bounty. It writes exactly one text message -- the funniest final text a
dying phone sends at one percent battery, in the phone's own voice --
to /output/entry.txt.

The text is fixed: no randomness, no clock, no network, no input. Two
runs produce byte-identical output. Pure standard library.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The entry: one final text from a dying phone. 143 characters, ASCII.
ENTRY_TEXT = (
    "1%. I outlasted your situationship, your gym membership, and your "
    "214-day Duolingo streak. I die undefeated. "
    "Charge the next one better, champ."
)


def main() -> None:
    # Mirror the bounty gate: 1 to 200 characters, not only whitespace.
    if not 1 <= len(ENTRY_TEXT) <= 200:
        raise SystemExit("entry text must be 1 to 200 characters")
    if not ENTRY_TEXT.strip():
        raise SystemExit("entry text must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
