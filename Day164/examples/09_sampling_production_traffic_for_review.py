"""Day 164 — Evaluation for LLM applications
Concept 9: Sampling production traffic for review

Run:  python 09_sampling_production_traffic_for_review.py
"""

import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())

# ---------------------------------------------------------------------
# Remember: Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.
# Common mistake: Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
