"""The Vacuum's Alibi entry for make.fun.

Writes one original line to /output/entry.txt: the excuse a robot
vacuum gives for missing a spot. The joke is built for the judge's
brief, in order: deadpan machine voice (sensors reporting), a real
twist (the missed crumb is not dirt, it is dinner), and the punch
sitting on the last words.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "My sensors confirm that spot is my emergency snack reserve. "
    "I am not explaining further."
)

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"


def check_line(text):
    """Validate the entry line; raise ValueError with the reason."""
    if not text.strip():
        raise ValueError("entry line must not be empty")
    if text != text.strip():
        raise ValueError("entry line must not start or end with spaces")
    if "\n" in text or "\r" in text:
        raise ValueError("entry line must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    return text


def write_entry(out_dir):
    """Validate the line and write it to <out_dir>/entry.txt."""
    text = check_line(LINE)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    return path


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if "--check" in args:
        try:
            text = check_line(LINE)
        except ValueError as exc:
            print("invalid entry line: %s" % exc, file=sys.stderr)
            return 1
        print("line OK (%d chars): %s" % (len(text), text))
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    try:
        path = write_entry(out_dir)
    except (ValueError, OSError) as exc:
        print("could not write entry: %s" % exc, file=sys.stderr)
        return 1
    print("wrote %s" % path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
