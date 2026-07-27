"""Day 180 — Experiment tracking and reproducibility
Concept 7: Comparing runs

Run:  python 07_comparing_runs.py
"""

import json, hashlib, subprocess

def run_record(params, metrics, data_path=None):
    try:
        commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
    except Exception:
        commit = 'unknown'
    return {
        'commit': commit,
        'params': params,
        'metrics': metrics,
        'data_sha': hashlib.sha256((data_path or 'none').encode()).hexdigest()[:12],
    }

print(json.dumps(run_record({'lr': 0.01, 'depth': 6}, {'auc': 0.912}, 'data/train.csv'), indent=2))

# ---------------------------------------------------------------------
# Remember: Log the data version alongside the code version — data changes silently, code changes loudly.
# Common mistake: Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
