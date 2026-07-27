# Day 43 — Data validation and contracts

Today's goal: work through **data validation and contracts** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Schema as a contract |
| 2 | Range and type assertions |
| 3 | Null rate thresholds |
| 4 | Category allowlists |
| 5 | Distribution checks against a baseline |
| 6 | Row count sanity checks |
| 7 | Failing loudly vs failing quietly |
| 8 | Validation in the training pipeline |
| 9 | Validation at inference time |
| 10 | Writing a validate() function with asserts |

---

## 1. Schema as a contract

A data contract is a set of assertions your pipeline refuses to run without: columns present, types correct, nulls under a threshold, categories from a known set, row count in a plausible range. Failing loudly on ingestion is cheaper than a quarter of quietly wrong predictions.

```python
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
```

**Remember:** Run the same validation at training AND at inference — skew between them is a top production failure.

**Common mistake:** Validating only in the training pipeline, so production quietly accepts a renamed column full of nulls.

## 2. Range and type assertions

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

## 3. Null rate thresholds

A data contract is a set of assertions your pipeline refuses to run without: columns present, types correct, nulls under a threshold, categories from a known set, row count in a plausible range. Failing loudly on ingestion is cheaper than a quarter of quietly wrong predictions.

```python
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
```

**Remember:** Run the same validation at training AND at inference — skew between them is a top production failure.

**Common mistake:** Validating only in the training pipeline, so production quietly accepts a renamed column full of nulls.

## 4. Category allowlists

A data contract is a set of assertions your pipeline refuses to run without: columns present, types correct, nulls under a threshold, categories from a known set, row count in a plausible range. Failing loudly on ingestion is cheaper than a quarter of quietly wrong predictions.

```python
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
```

**Remember:** Run the same validation at training AND at inference — skew between them is a top production failure.

**Common mistake:** Validating only in the training pipeline, so production quietly accepts a renamed column full of nulls.

## 5. Distribution checks against a baseline

A distribution says which values are likely. Gaussian for measurement noise, Bernoulli for yes/no, Poisson for counts per interval. Choosing the right one is choosing your loss function: Gaussian likelihood gives MSE, Bernoulli gives cross-entropy.

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Remember:** Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

**Common mistake:** Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

## 6. Row count sanity checks

A data contract is a set of assertions your pipeline refuses to run without: columns present, types correct, nulls under a threshold, categories from a known set, row count in a plausible range. Failing loudly on ingestion is cheaper than a quarter of quietly wrong predictions.

```python
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
```

**Remember:** Run the same validation at training AND at inference — skew between them is a top production failure.

**Common mistake:** Validating only in the training pipeline, so production quietly accepts a renamed column full of nulls.

## 7. Failing loudly vs failing quietly

A data contract is a set of assertions your pipeline refuses to run without: columns present, types correct, nulls under a threshold, categories from a known set, row count in a plausible range. Failing loudly on ingestion is cheaper than a quarter of quietly wrong predictions.

```python
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
```

**Remember:** Run the same validation at training AND at inference — skew between them is a top production failure.

**Common mistake:** Validating only in the training pipeline, so production quietly accepts a renamed column full of nulls.

## 8. Validation in the training pipeline

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

## 9. Validation at inference time

A data contract is a set of assertions your pipeline refuses to run without: columns present, types correct, nulls under a threshold, categories from a known set, row count in a plausible range. Failing loudly on ingestion is cheaper than a quarter of quietly wrong predictions.

```python
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
```

**Remember:** Run the same validation at training AND at inference — skew between them is a top production failure.

**Common mistake:** Validating only in the training pipeline, so production quietly accepts a renamed column full of nulls.

## 10. Writing a validate() function with asserts

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

---

## What you should be able to do after Day 43

- Explain **Schema as a contract** to someone else without notes.
- Explain **Range and type assertions** to someone else without notes.
- Explain **Null rate thresholds** to someone else without notes.
- Explain **Category allowlists** to someone else without notes.
- Explain **Distribution checks against a baseline** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
