"""Day 185 — Data engineering for AI
Concept 3: Orchestration with Airflow or Prefect

Run:  python 03_orchestration_with_airflow_or_prefect.py
"""

from pathlib import Path

def write_partition(root, date, rows):
    """Idempotent: rewriting a partition replaces it, never appends."""
    part = Path(root) / f'dt={date}'
    part.mkdir(parents=True, exist_ok=True)
    out = part / 'data.csv'
    out.write_text('\n'.join(rows), encoding='utf-8')
    return out

root = 'demo_lake'
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))
print(write_partition(root, '2024-03-01', ['a,1', 'b,2']))   # re-run: same result

import shutil; shutil.rmtree(root)

# ---------------------------------------------------------------------
# Remember: Idempotent + partitioned = safe backfills. Append-only pipelines make every rerun a data corruption event.
# Common mistake: A pipeline that appends, so a retried job silently doubles yesterday's numbers.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
