"""Day 09 — pandas: reshape and aggregate
Concept 3: agg with multiple functions

Run:  python 03_agg_with_multiple_functions.py
"""

import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))

# ---------------------------------------------------------------------
# Remember: Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.
# Common mistake: Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
