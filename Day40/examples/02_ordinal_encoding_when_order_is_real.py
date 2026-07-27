"""Day 40 — Encoding and scaling
Concept 2: Ordinal encoding when order is real

Run:  python 02_ordinal_encoding_when_order_is_real.py
"""

import pandas as pd

df = pd.DataFrame({'size': ['small', 'large', 'medium'], 'city': ['pune', 'delhi', 'pune']})

order = {'small': 0, 'medium': 1, 'large': 2}     # real order -> ordinal is fine
df['size_ord'] = df['size'].map(order)

print(pd.get_dummies(df[['city']], prefix='city', dtype=int))
print(df)

# ---------------------------------------------------------------------
# Remember: Handle unseen categories at inference time — decide up front whether they map to 'other' or raise.
# Common mistake: One-hot encoding a 50,000-value ID column and blowing up memory for zero signal.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
