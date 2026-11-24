"""Warning label for humans: one line, big laugh.

Writes a single-line safety warning label to entry.txt.
"""

import os

LABEL = (
    "CAUTION: Prone to saying 'just five more minutes' for three hours. "
    "Do not rely on stated time estimates."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
