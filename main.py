"""makefun-angry-judge-01: a short rant about the self-checkout machine.

Writes the entry text to /output/entry.txt (1-400 characters, UTF-8).
"""

import os

ENTRY = (
    "My self-checkout machine just reported me for stealing my own groceries. "
    '"Unexpected item in the bagging area." '
    "Unexpected? I scanned it. I bagged it. It watched me do it. "
    "Now some poor employee has to walk over and confirm that yes, "
    "I am allowed to buy these bananas. "
    "I came in for milk and left as a suspect in a shoplifting investigation "
    "run by a machine that panics when it can't count to six."
)


def main():
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
