"""Day 02 — Python essentials refresher
Concept 10: Reading the standard library docs

Run:  python 10_reading_the_standard_library_docs.py
"""

from pathlib import Path

def load_rows(path: Path, limit: int | None = None) -> list[dict[str, str]]:
    """Read a CSV into dicts. `limit` caps rows for quick experiments."""
    import csv
    with path.open(encoding='utf-8', newline='') as fh:
        rows = list(csv.DictReader(fh))
    return rows[:limit] if limit else rows

print(load_rows.__annotations__)

# ---------------------------------------------------------------------
# Remember: Hint the boundaries (function signatures, config objects); skip hints on obvious locals.
# Common mistake: Annotating everything, including throwaway locals, until the types outweigh the logic.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
