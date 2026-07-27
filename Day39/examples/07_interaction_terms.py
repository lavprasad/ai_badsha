"""Day 39 — Feature engineering fundamentals
Concept 7: Interaction terms

Run:  python 07_interaction_terms.py
"""

import pandas as pd

df = pd.DataFrame({
    'clicks': [10, 5, 0, 30],
    'impressions': [100, 200, 50, 300],
    'ts': pd.to_datetime(['2024-01-01', '2024-01-05', '2024-02-01', '2024-02-10']),
})
df['ctr'] = df['clicks'] / df['impressions'].clip(lower=1)   # ratio beats raw counts
df['days_since_prev'] = df['ts'].diff().dt.days.fillna(0)
df['is_weekend'] = df['ts'].dt.dayofweek.isin([5, 6]).astype(int)
print(df)

# ---------------------------------------------------------------------
# Remember: Every engineered feature must be computable at prediction time with data you will actually have.
# Common mistake: Building a feature from a column that is only filled in AFTER the event you are predicting.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
