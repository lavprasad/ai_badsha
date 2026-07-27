"""Day 13 — SQL for AI practitioners
Concept 5: Window functions for lag features

Run:  python 05_window_functions_for_lag_features.py
"""

import pandas as pd
import numpy as np

idx = pd.date_range('2024-01-01', periods=120, freq='D')
y = pd.Series(np.arange(120) * 0.3 + 10 * np.sin(np.arange(120) / 7) + np.random.default_rng(0).normal(0, 1, 120), index=idx)

feat = pd.DataFrame({'y': y})
feat['lag_1'] = feat['y'].shift(1)
feat['lag_7'] = feat['y'].shift(7)
feat['roll_7'] = feat['y'].shift(1).rolling(7).mean()
feat['dow'] = feat.index.dayofweek
print(feat.dropna().head())

cut = int(len(feat) * 0.8)
print('train ends', feat.index[cut - 1].date(), '| test starts', feat.index[cut].date())

# ---------------------------------------------------------------------
# Remember: Every feature must use `.shift(1)` or later — no row may see its own future.
# Common mistake: A rolling mean that includes the current row, which leaks the target into the feature.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
