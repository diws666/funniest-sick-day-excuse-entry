#!/usr/bin/env python3
"""Writes the sick-day excuse entry to /output/entry.txt."""

import os

OUTPUT_FILENAME = "entry.txt"


def main() -> None:
    line = (
        "Woke up sounding like a dial-up modem. "
        "I can only communicate in beeps "
        "until my voice finishes buffering."
    )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, OUTPUT_FILENAME), "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print("wrote", OUTPUT_FILENAME, "->", repr(line))


if __name__ == "__main__":
    main()
