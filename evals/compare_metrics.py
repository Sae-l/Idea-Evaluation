"""Cheap mechanical metrics for the head-to-head comparison (docs/COMPARISON.md).
Usage: python compare_metrics.py out/*.md   - prints words, headings, tables rows, labeled/unlabeled hints.
Heuristics only: they count surface features, not quality."""
import re, sys

def metrics(text):
    low = text.lower()
    return {
        "words": len(text.split()),
        "headings": len(re.findall(r"^#{1,4} ", text, re.M)),
        "table_rows": len(re.findall(r"^\|.*\|\s*$", text, re.M)),
        "stop_criterion": bool(re.search(r"stop if|kill (criterion|if)|abandon if|walk away if|if (fewer|less) than", low)),
        "next_step_30min": bool(re.search(r"(within|in|<=?|≤)\s*(30|20|15|10)\s*min|next[^.\n]{0,40}(30|20|15|10) ?min", low)),
        "label_tags": len(re.findall(r"assum|unverified|unchecked|\bE[0-4]\b|\[(fact|belief|assumption|unknown|guess|estimate)", text, re.I)),
        "question_marks_to_user": len(re.findall(r"\?\s*$", text, re.M)),
        "percent_figures": len(re.findall(r"\d+(?:[.,]\d+)?\s?%", text)),
    }

if __name__ == "__main__":
    for p in sys.argv[1:]:
        with open(p, encoding="utf-8") as f:
            m = metrics(f.read())
        print(p.split("/")[-1], *(f"{k}={v}" for k, v in m.items()))
