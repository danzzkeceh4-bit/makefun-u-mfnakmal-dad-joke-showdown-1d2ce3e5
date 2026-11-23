#!/usr/bin/env python3
"""Dad Joke Showdown.

Deterministic program for the make.fun competition
u-mfnakmal-dad-joke-showdown-1d2ce3e5.

Writes exactly one dad joke (1-200 characters, UTF-8) to
/output/entry.txt. No network, no randomness, no arguments.
"""

import os
import sys

JOKE_LINE = (
    "I changed the Wi-Fi password to 'DadIsRight' \u2014 now every "
    "time it drops, the kids have to type that I'm right just to "
    "get back online."
)

MIN_LENGTH = 1
MAX_LENGTH = 200


def resolve_output_path() -> str:
    """Output directory from MAKEFUN_OUTPUT_DIR, else /output."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(output_dir, "entry.txt")


def validate_line(line: str) -> str:
    """Validate the joke line before it is written out.

    Rules (from the competition brief):
    - exactly one line, 1-200 characters, UTF-8 encodable
    - must not be empty or whitespace only

    Returns the stripped line on success, raises ValueError otherwise.
    """
    if not isinstance(line, str):
        raise ValueError("joke line must be a string")
    stripped = line.strip()
    if not stripped:
        raise ValueError("joke line is empty or only whitespace")
    if not (MIN_LENGTH <= len(stripped) <= MAX_LENGTH):
        raise ValueError(
            f"joke line is {len(stripped)} characters, "
            f"must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    # Reject embedded newlines: the entry must be exactly one line.
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("joke line must be a single line")
    # UTF-8 check: raise a clear ValueError (not a raw
    # UnicodeEncodeError) when the line cannot be encoded.
    try:
        stripped.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError(f"joke line is not valid UTF-8: {exc}") from exc
    return stripped


def main() -> int:
    """Validate the joke line and write it to entry.txt."""
    try:
        line = validate_line(JOKE_LINE)
    except ValueError as exc:
        print(
            f"error: invalid joke line ({exc}); "
            f"entry must be one line of {MIN_LENGTH}-{MAX_LENGTH} "
            "non-whitespace UTF-8 characters",
            file=sys.stderr,
        )
        return 1

    # validate_line() already returns the stripped line, so no
    # leading/trailing whitespace can reach the writer below.
    output_path = resolve_output_path()
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    # No trailing newline: the entry is exactly the line, nothing more.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
