# Day 181 — Feature stores and data infrastructure

Today's goal: work through **Feature stores and data infrastructure** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Training/serving skew |
| 2 | The feature store idea |
| 3 | Offline vs online stores |
| 4 | Point-in-time correct joins |
| 5 | Feature freshness |
| 6 | Shared features across teams |
| 7 | When a feature store is overkill |
| 8 | Simple alternatives that work |
| 9 | Data contracts between teams |
| 10 | Designing for consistency |

---

## 1. Training/serving skew

Serving a model means loading it once at startup and answering HTTP requests. Validate the input schema, return errors as structured JSON, add a health endpoint, and never load the model inside the request handler.

```python
# pip install fastapi uvicorn ; run: uvicorn app:app --reload
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
#
# app = FastAPI()
# model = joblib.load('model.joblib')      # once, at startup
#
# class Req(BaseModel):
#     features: list[float]
#
# @app.get('/health')
# def health():
#     return {'ok': True}
#
# @app.post('/predict')
# def predict(req: Req):
#     return {'prediction': float(model.predict([req.features])[0])}
print('Load once at startup; validate with a schema; expose /health for the load balancer.')
```

**Remember:** Batch requests where latency allows — GPU throughput collapses on batch size 1.

**Common mistake:** Reloading the model per request and wondering why p99 latency is four seconds.

Practice: open `examples/01_training_serving_skew.py`, predict the output, change one line, predict again.

## 2. The feature store idea

Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone. A feature store fixes it by computing once and serving both paths. For most teams a shared function plus tests is enough.

```python
from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')
```

**Remember:** One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

**Common mistake:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Practice: open `examples/02_the_feature_store_idea.py`, predict the output, change one line, predict again.

## 3. Offline vs online stores

Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone. A feature store fixes it by computing once and serving both paths. For most teams a shared function plus tests is enough.

```python
from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')
```

**Remember:** One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

**Common mistake:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Practice: open `examples/03_offline_vs_online_stores.py`, predict the output, change one line, predict again.

## 4. Point-in-time correct joins

A DataFrame is a table with labelled columns and an index. Most real ML work is 80% reshaping tables: load, clean, group, join, aggregate. Learn `groupby` and `merge` well and you can answer most data questions without writing loops.

```python
import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))
```

**Remember:** Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

**Common mistake:** Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

Practice: open `examples/04_point_in_time_correct_joins.py`, predict the output, change one line, predict again.

## 5. Feature freshness

Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone. A feature store fixes it by computing once and serving both paths. For most teams a shared function plus tests is enough.

```python
from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')
```

**Remember:** One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

**Common mistake:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Practice: open `examples/05_feature_freshness.py`, predict the output, change one line, predict again.

## 6. Shared features across teams

Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone. A feature store fixes it by computing once and serving both paths. For most teams a shared function plus tests is enough.

```python
from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')
```

**Remember:** One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

**Common mistake:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Practice: open `examples/06_shared_features_across_teams.py`, predict the output, change one line, predict again.

## 7. When a feature store is overkill

Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone. A feature store fixes it by computing once and serving both paths. For most teams a shared function plus tests is enough.

```python
from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')
```

**Remember:** One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

**Common mistake:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Practice: open `examples/07_when_a_feature_store_is_overkill.py`, predict the output, change one line, predict again.

## 8. Simple alternatives that work

Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone. A feature store fixes it by computing once and serving both paths. For most teams a shared function plus tests is enough.

```python
from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')
```

**Remember:** One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

**Common mistake:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Practice: open `examples/08_simple_alternatives_that_work.py`, predict the output, change one line, predict again.

## 9. Data contracts between teams

Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone. A feature store fixes it by computing once and serving both paths. For most teams a shared function plus tests is enough.

```python
from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')
```

**Remember:** One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

**Common mistake:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Practice: open `examples/09_data_contracts_between_teams.py`, predict the output, change one line, predict again.

## 10. Designing for consistency

Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone. A feature store fixes it by computing once and serving both paths. For most teams a shared function plus tests is enough.

```python
from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')
```

**Remember:** One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

**Common mistake:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Practice: open `examples/10_designing_for_consistency.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 181

- Explain **Training/serving skew** to someone else without notes.
- Explain **The feature store idea** to someone else without notes.
- Explain **Offline vs online stores** to someone else without notes.
- Explain **Point-in-time correct joins** to someone else without notes.
- Explain **Feature freshness** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
