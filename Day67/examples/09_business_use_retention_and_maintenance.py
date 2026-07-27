"""Day 67 — Survival and duration models
Concept 9: Business use: retention and maintenance

Run:  python 09_business_use_retention_and_maintenance.py
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)

# ---------------------------------------------------------------------
# Remember: Compute the fill statistic on the TRAIN split only, then apply it to test.
# Common mistake: Filling with the mean computed over the full dataset — that leaks test information into training.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
