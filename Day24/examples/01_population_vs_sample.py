"""Day 24 — Inferential statistics
Concept 1: Population vs sample

Run:  python 01_population_vs_sample.py
"""

import numpy as np

rng = np.random.default_rng(0)
a = rng.normal(10.0, 2.0, 60)
b = rng.normal(11.0, 2.0, 60)

# Welch t-statistic, no scipy needed
se = np.sqrt(a.var(ddof=1) / len(a) + b.var(ddof=1) / len(b))
t = (b.mean() - a.mean()) / se
print(f'mean diff {b.mean() - a.mean():.3f}  t = {t:.2f}')
print('|t| > 2 is roughly the 5% threshold at these sample sizes')

# Twenty independent tests at 5%: expect one false positive by chance alone
print('expected false positives in 20 tests:', 20 * 0.05)

# ---------------------------------------------------------------------
# Remember: Testing 20 hypotheses at p<0.05 gives you one false positive on average. Correct for it.
# Common mistake: Slicing the data 15 ways after the fact and reporting the one slice that reached significance.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
