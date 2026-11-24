"""Cat Reviews Its Human — a one-line review, printed as the entry.

The review lives in entry.txt so the joke stays editable without touching
the code; this module only loads it, tidies the whitespace, and prints it.
"""

from pathlib import Path


def load_review() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    review = " ".join(text.split())
    if not review:
        raise SystemExit("entry.txt is empty — nothing to review")
    if "\n" in review:
        raise SystemExit("the review must stay on one line")
    return review


def main() -> None:
    print(load_review())


if __name__ == "__main__":
    main()
