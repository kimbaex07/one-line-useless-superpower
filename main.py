"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original line naming a hilariously useless
superpower to /output/entry.txt (UTF-8, trailing newline).

Pure Python standard library only. No network, no third-party
imports, no environment reads.
"""

import os

LINE = (
    "I can see five seconds into the future, which is exactly "
    "long enough to watch myself trip over nothing."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
