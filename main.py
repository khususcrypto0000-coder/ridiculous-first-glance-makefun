"""Ridiculous at First Glance, Real by the Second.

Writes a single one-sentence startup pitch to /output/entry.txt.

The pitch: a rentable live laugh track for your boss's jokes on Zoom.
Absurd at first glance, a real business at second glance: managers pay
per meeting for the sound of their punchlines landing, and teams pay to
kill the awkward silence that follows every gag.

Standard library only. Deterministic: running this twice produces
byte-identical output.
"""

import os
import sys

# The entry: exactly one sentence, 1-200 characters, no trailing newline.
PITCH = (
    "We rent a live laugh track for your boss's jokes on Zoom, because "
    "managers pay $10 a meeting to hear their punchlines land and teams "
    "pay to end the awkward silence after every gag."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main(argv):
    """Write PITCH to the output file, creating its folder if needed."""
    output_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT_PATH
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
