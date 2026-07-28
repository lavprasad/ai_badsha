# Day 43 — Data validation and contracts

Aaj ka goal: **Data validation and contracts** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Data contract un assertions ka set hai jinke bina aapka pipeline chalne se mana kar de: columns maujood, types sahi, nulls threshold ke neeche, categories known set se, row count plausible range me. Ingestion par shor machaa kar fail hona ek chaupai bhar chupchap galat predictions se sasta hai.

### Chhota code

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

**Yaad rakho:** Wahi validation training AUR inference dono par chalao — dono ke beech ka skew top production failure hai.

**Aam galti:** Validation sirf training pipeline me rakhna, jisse production chupchap ek renamed, null se bhara column le leta hai.

Practice: `examples/01_schema_as_a_contract.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Range and type assertions

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

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

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/02_range_and_type_assertions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Null rate thresholds

### Aasaan Bhasha

Data contract un assertions ka set hai jinke bina aapka pipeline chalne se mana kar de: columns maujood, types sahi, nulls threshold ke neeche, categories known set se, row count plausible range me. Ingestion par shor machaa kar fail hona ek chaupai bhar chupchap galat predictions se sasta hai.

### Chhota code

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

**Yaad rakho:** Wahi validation training AUR inference dono par chalao — dono ke beech ka skew top production failure hai.

**Aam galti:** Validation sirf training pipeline me rakhna, jisse production chupchap ek renamed, null se bhara column le leta hai.

Practice: `examples/03_null_rate_thresholds.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Category allowlists

### Aasaan Bhasha

Data contract un assertions ka set hai jinke bina aapka pipeline chalne se mana kar de: columns maujood, types sahi, nulls threshold ke neeche, categories known set se, row count plausible range me. Ingestion par shor machaa kar fail hona ek chaupai bhar chupchap galat predictions se sasta hai.

### Chhota code

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

**Yaad rakho:** Wahi validation training AUR inference dono par chalao — dono ke beech ka skew top production failure hai.

**Aam galti:** Validation sirf training pipeline me rakhna, jisse production chupchap ek renamed, null se bhara column le leta hai.

Practice: `examples/04_category_allowlists.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Distribution checks against a baseline

### Aasaan Bhasha

Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Yaad rakho:** Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).

**Aam galti:** Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.

Practice: `examples/05_distribution_checks_against_a_baseline.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Row count sanity checks

### Aasaan Bhasha

Data contract un assertions ka set hai jinke bina aapka pipeline chalne se mana kar de: columns maujood, types sahi, nulls threshold ke neeche, categories known set se, row count plausible range me. Ingestion par shor machaa kar fail hona ek chaupai bhar chupchap galat predictions se sasta hai.

### Chhota code

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

**Yaad rakho:** Wahi validation training AUR inference dono par chalao — dono ke beech ka skew top production failure hai.

**Aam galti:** Validation sirf training pipeline me rakhna, jisse production chupchap ek renamed, null se bhara column le leta hai.

Practice: `examples/06_row_count_sanity_checks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Failing loudly vs failing quietly

### Aasaan Bhasha

Data contract un assertions ka set hai jinke bina aapka pipeline chalne se mana kar de: columns maujood, types sahi, nulls threshold ke neeche, categories known set se, row count plausible range me. Ingestion par shor machaa kar fail hona ek chaupai bhar chupchap galat predictions se sasta hai.

### Chhota code

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

**Yaad rakho:** Wahi validation training AUR inference dono par chalao — dono ke beech ka skew top production failure hai.

**Aam galti:** Validation sirf training pipeline me rakhna, jisse production chupchap ek renamed, null se bhara column le leta hai.

Practice: `examples/07_failing_loudly_vs_failing_quietly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Validation in the training pipeline

### Aasaan Bhasha

Pipeline preprocessing aur model ko ek hi object me jod deta hai jo ek unit ki tarah fit aur predict karta hai. Leakage ke khilaaf yahi sabse achhi dhaal hai, aur deployment ko chhe alag steps ke bajaye ek artefact milta hai jise yaad rakhne ki zaroorat nahi.

### Chhota code

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

**Yaad rakho:** `handle_unknown='ignore'` production ko us category par crash hone se bachata hai jo training me kabhi nahi dikhi.

**Aam galti:** Notebook me preprocess karna aur serving code likhte waqt ek step bhool jaana.

Practice: `examples/08_validation_in_the_training_pipeline.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Validation at inference time

### Aasaan Bhasha

Data contract un assertions ka set hai jinke bina aapka pipeline chalne se mana kar de: columns maujood, types sahi, nulls threshold ke neeche, categories known set se, row count plausible range me. Ingestion par shor machaa kar fail hona ek chaupai bhar chupchap galat predictions se sasta hai.

### Chhota code

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

**Yaad rakho:** Wahi validation training AUR inference dono par chalao — dono ke beech ka skew top production failure hai.

**Aam galti:** Validation sirf training pipeline me rakhna, jisse production chupchap ek renamed, null se bhara column le leta hai.

Practice: `examples/09_validation_at_inference_time.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Writing a validate() function with asserts

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

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

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/10_writing_a_validate_function_with_asserts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 43 ke baad aapko ye aana chahiye

- **Schema as a contract** ko bina notes dekhe kisi dost ko samjha sakna.
- **Range and type assertions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Null rate thresholds** ko bina notes dekhe kisi dost ko samjha sakna.
- **Category allowlists** ko bina notes dekhe kisi dost ko samjha sakna.
- **Distribution checks against a baseline** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
