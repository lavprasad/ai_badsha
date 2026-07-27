"""Day 182 — Monitoring models in production
Concept 3: Prediction drift

Run:  python 03_prediction_drift.py
"""

import numpy as np

def psi(expected, actual, bins=10):
    """Population Stability Index: >0.2 means investigate."""
    edges = np.percentile(expected, np.linspace(0, 100, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    e = np.histogram(expected, edges)[0] / len(expected) + 1e-6
    a = np.histogram(actual, edges)[0] / len(actual) + 1e-6
    return float(np.sum((a - e) * np.log(a / e)))

rng = np.random.default_rng(0)
baseline = rng.normal(0, 1, 10_000)
print('same dist  PSI', round(psi(baseline, rng.normal(0, 1, 5_000)), 4))
print('shifted    PSI', round(psi(baseline, rng.normal(0.6, 1.2, 5_000)), 4))

# ---------------------------------------------------------------------
# Remember: PSI under 0.1 stable, 0.1-0.2 watch, above 0.2 investigate. Alert on the prediction distribution too.
# Common mistake: Only monitoring uptime, so a model that returns 200 OK while being badly wrong looks healthy.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
