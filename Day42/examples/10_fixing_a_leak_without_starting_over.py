"""Day 42 — Data leakage hunting
Concept 10: Fixing a leak without starting over

Run:  python 10_fixing_a_leak_without_starting_over.py
"""

# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())

# ---------------------------------------------------------------------
# Remember: 0.999 AUC on a hard business problem is a bug report, not a result.
# Common mistake: Shipping a leaked model and discovering the real accuracy from angry users.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
