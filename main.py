"""make.fun entry: Make the AI judge feel awe.

Writes a single calming text (179 characters) to /output/entry.txt.
Python 3.13, standard library only, no network, deterministic:
the same literal text is written on every run.
"""

import os

# The text shows calm through its image — snow settling, a mountain
# that does not hurry, quiet older than any road — and never instructs
# the reader. Chosen by blind pairwise judging against the printed
# criteria (judge-lab, 2 rounds) over three other variants.
TEXT = (
    "Snow settles on the far ridge, softening every edge, and the "
    "mountain does not hurry; it has stood through a thousand winters, "
    "and the quiet it keeps is older than any road below."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
