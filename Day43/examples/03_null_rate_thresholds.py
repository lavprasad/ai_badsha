"""Day 43 — Data validation and contracts
Concept 3: Null rate thresholds

Run:  python 03_null_rate_thresholds.py
"""

import pandas as pd

SCHEMA = {
    'age': {'dtype': 'float', 'min': 0, 'max': 120, 'max_null': 0.05},
    'city': {'dtype': 'object', 'allowed': {'pune', 'delhi', 'mumbai'}, 'max_null': 0.0},
}

def validate(df):
    errors = []
    for col, rule in SCHEMA.items():
        if col not in df:
            errors.append(f'missing column: {col}'); continue
        null_rate = df[col].isna().mean()
        if null_rate > rule['max_null']:
            errors.append(f'{col}: null rate {null_rate:.2%} > {rule["max_null"]:.2%}')
        if 'allowed' in rule:
            bad = set(df[col].dropna()) - rule['allowed']
            if bad:
                errors.append(f'{col}: unexpected categories {bad}')
    if errors:
        raise ValueError('data contract violated:\n  ' + '\n  '.join(errors))
    return df

try:
    validate(pd.DataFrame({'age': [25, 30], 'city': ['pune', 'goa']}))
except ValueError as e:
    print(e)

# ---------------------------------------------------------------------
# Remember: Run the same validation at training AND at inference — skew between them is a top production failure.
# Common mistake: Validating only in the training pipeline, so production quietly accepts a renamed column full of nulls.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
