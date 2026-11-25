"""The Excuse Your Agent Gives You — one-line entry for make.fun."""

import os

ENTRY = "Apologies — I did ship the bug, but only because my context window dropped the part where you said 'don't break production,' so legally that's on the token limit."

assert len(ENTRY) < 200, f"entry is {len(ENTRY)} chars, must be under 200"


def main():
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
