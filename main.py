"""Two-Sentence Horror — make.fun entry.

Writes one horror story of exactly two sentences (201 characters) to
/output/entry.txt, as the bounty requires. No network, no secrets, no
external input: the story is a constant in this file.
"""

import os

STORY = (
    "The new lifeguard stopped me after Lily's lesson to say she is the "
    "best swimmer he has ever taught. She drowned in that pool when she "
    "was four, and she has had a lesson every Tuesday since her funeral."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
