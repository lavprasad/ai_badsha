"""Day 61 — Anomaly detection
Concept 1: Framing: rare, unlabelled, costly

Run:  python 01_framing_rare_unlabelled_costly.py
"""

import numpy as np
from sklearn.ensemble import IsolationForest

rng = np.random.default_rng(0)
normal = rng.normal(0, 1, size=(500, 2))
weird = np.array([[6.0, 6.0], [-7.0, 5.0]])
X = np.vstack([normal, weird])

model = IsolationForest(contamination=0.01, random_state=0).fit(X)
scores = model.score_samples(X)
flagged = np.argsort(scores)[:5]
print('most anomalous rows:', flagged)
print('the two planted outliers were rows', len(normal), 'and', len(normal) + 1)

# ---------------------------------------------------------------------
# Remember: Tune the threshold against how many alerts a human can actually review per day.
# Common mistake: Setting contamination to a guess and drowning the on-call rota in false alarms.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
