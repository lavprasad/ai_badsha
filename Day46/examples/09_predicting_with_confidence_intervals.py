"""Day 46 — Linear regression in practice
Concept 9: Predicting with confidence intervals

Run:  python 09_predicting_with_confidence_intervals.py
"""

import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')

# ---------------------------------------------------------------------
# Remember: Decide the sample size and the metric BEFORE looking at the data.
# Common mistake: Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
