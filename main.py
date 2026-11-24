"""Charm the Commuter: Forecast a City That Isn't.

One-line weather forecast for Drizzlewick, a city that does not exist:
light umbrella rain, buses fashionably late, and every puddle reflecting
a rainbow -- a small joke to make a bored commuter smile at the bus stop.
"""

import os

# The entry: a single line, 1-140 characters, naming the invented city,
# giving its weather, and landing one gentle joke for the commuter.
ENTRY = (
    "Drizzlewick today: light umbrella rain, 14°C, buses fashionably "
    "late — but every puddle reflects a rainbow, so pack snacks and hope."
)

# Runners-up considered while drafting (kept for the record, not used):
# - "Drizzlewick: light umbrella rain, 14°C, buses ten minutes late as
#   usual — but every puddle holds a small rainbow, so the commute
#   sparkles." (138 chars)
# - "Drizzlewick today: umbrella rain, 14°C, buses fashionably late —
#   but every puddle reflects a rainbow, so pack snacks and hope."
#   (126 chars)


def entry_summary(text):
    """One-line summary used in the run log: length and first words."""
    return "%d chars: %s..." % (len(text), text[:24])


def validate(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1-140 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(entry_summary(ENTRY))
    print("Wrote %d characters to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
