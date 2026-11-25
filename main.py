#!/usr/bin/env python3
"""The 3 AM Commit Message — writes one commit message to /output/entry.txt."""

import os

MESSAGE = "fix: pushed to prod at 3 AM because the CI was green and my judgment was not"


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
    text = MESSAGE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} outside 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
