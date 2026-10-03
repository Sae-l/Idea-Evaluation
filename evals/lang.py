"""Shared helper for the answer checkers. The checkers look for English (and for the quick check German) labels such as
"Next", "Verdict" or "At least". The skills answer in the user's language, so for text that is mostly not Latin script
(for example Arabic) the label checks are skipped and only structure is checked: length, tables, numbered findings,
checkbox tasks and starred tasks. Limits for such text are unmeasured; they are the English limits times LENIENCY."""
import unicodedata

LENIENCY = 1.25


def mostly_latin(text, threshold=0.7):
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return True
    latin = sum(1 for c in letters if unicodedata.name(c, "").startswith("LATIN"))
    return latin / len(letters) >= threshold
