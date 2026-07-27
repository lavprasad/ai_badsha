"""Day 59 — Unsupervised learning: clustering
Concept 2: K-means and Lloyd's algorithm

Run:  python 02_k_means_and_lloyd_s_algorithm.py
"""

import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])

# ---------------------------------------------------------------------
# Remember: Quote median + IQR for skewed data, mean + std only for roughly symmetric data.
# Common mistake: Removing 'outliers' automatically when they are the exact events you were hired to predict.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
