"""Day 11 — Visualisation with matplotlib
Concept 7: Log scales and when to use them

Run:  python 07_log_scales_and_when_to_use_them.py
"""

import matplotlib
matplotlib.use('Agg')          # headless-safe for scripts/CI
import matplotlib.pyplot as plt
import numpy as np

x = np.random.default_rng(0).normal(size=500)
fig, ax = plt.subplots()
ax.hist(x, bins=30)
ax.set_title('sample distribution')
fig.savefig('hist.png', dpi=120)
print('wrote hist.png')

# ---------------------------------------------------------------------
# Remember: Label the axes. An unlabelled plot is a decoration, not evidence.
# Common mistake: Judging a model by its accuracy number alone without ever looking at the data.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
