# Day 42 — Data leakage hunting

Today's goal: work through **Data leakage hunting** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | What leakage actually is |
| 2 | Preprocessing leakage |
| 3 | Target leakage from future columns |
| 4 | Duplicate rows across splits |
| 5 | Group leakage: same entity both sides |
| 6 | Temporal leakage |
| 7 | Leakage through feature selection |
| 8 | Symptoms: impossible scores |
| 9 | A leakage audit checklist |
| 10 | Fixing a leak without starting over |

---

## 1. What leakage actually is

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 2. Preprocessing leakage

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 3. Target leakage from future columns

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 4. Duplicate rows across splits

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 5. Group leakage: same entity both sides

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 6. Temporal leakage

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 7. Leakage through feature selection

Feature engineering is where domain knowledge beats compute. A ratio, a lag, a time-since-last-event, or a count over a window often adds more than switching algorithms. Selection then removes features that add variance without signal.

```python
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
```

**Remember:** Every engineered feature must be computable at prediction time with data you will actually have.

**Common mistake:** Building a feature from a column that is only filled in AFTER the event you are predicting.

## 8. Symptoms: impossible scores

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 9. A leakage audit checklist

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 10. Fixing a leak without starting over

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

---

## What you should be able to do after Day 42

- Explain **What leakage actually is** to someone else without notes.
- Explain **Preprocessing leakage** to someone else without notes.
- Explain **Target leakage from future columns** to someone else without notes.
- Explain **Duplicate rows across splits** to someone else without notes.
- Explain **Group leakage: same entity both sides** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
