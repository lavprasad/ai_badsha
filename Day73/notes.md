# Day 73 — Error analysis

Today's goal: work through **Error analysis** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why aggregate metrics hide the problem |
| 2 | Slicing errors by segment |
| 3 | Building an error taxonomy |
| 4 | Hand-labelling 50 wrong predictions |
| 5 | Identifying the biggest error bucket |
| 6 | Deciding: more data, better features, or new model |
| 7 | Confusion matrix deep dive |
| 8 | Finding annotation errors in the labels |
| 9 | Prioritising fixes by business impact |
| 10 | Turning error analysis into a backlog |

---

## 1. Why aggregate metrics hide the problem

One accuracy number tells you nothing about what to fix. Pull the wrong predictions, read fifty by hand, and sort them into buckets. Usually one bucket is 40% of the errors and has an obvious fix — and a surprising share turns out to be wrong labels, not wrong predictions.

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Remember:** Rank error buckets by share of total errors, not by error rate — fix what is actually costing you.

**Common mistake:** Optimising overall accuracy while one segment quietly gets 0% and generates every complaint.

Practice: open `examples/01_why_aggregate_metrics_hide_the_problem.py`, predict the output, change one line, predict again.

## 2. Slicing errors by segment

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

Practice: open `examples/02_slicing_errors_by_segment.py`, predict the output, change one line, predict again.

## 3. Building an error taxonomy

Projects are where the learning sticks. Build a thin end-to-end slice first — load data, train something dumb, evaluate, serve one prediction — then improve one layer at a time. A working baseline on day one beats a perfect model that never ships.

```python
STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)
```

**Remember:** Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

**Common mistake:** Six weeks of feature engineering with no baseline to prove any of it helped.

Practice: open `examples/03_building_an_error_taxonomy.py`, predict the output, change one line, predict again.

## 4. Hand-labelling 50 wrong predictions

One accuracy number tells you nothing about what to fix. Pull the wrong predictions, read fifty by hand, and sort them into buckets. Usually one bucket is 40% of the errors and has an obvious fix — and a surprising share turns out to be wrong labels, not wrong predictions.

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Remember:** Rank error buckets by share of total errors, not by error rate — fix what is actually costing you.

**Common mistake:** Optimising overall accuracy while one segment quietly gets 0% and generates every complaint.

Practice: open `examples/04_hand_labelling_50_wrong_predictions.py`, predict the output, change one line, predict again.

## 5. Identifying the biggest error bucket

One accuracy number tells you nothing about what to fix. Pull the wrong predictions, read fifty by hand, and sort them into buckets. Usually one bucket is 40% of the errors and has an obvious fix — and a surprising share turns out to be wrong labels, not wrong predictions.

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Remember:** Rank error buckets by share of total errors, not by error rate — fix what is actually costing you.

**Common mistake:** Optimising overall accuracy while one segment quietly gets 0% and generates every complaint.

Practice: open `examples/05_identifying_the_biggest_error_bucket.py`, predict the output, change one line, predict again.

## 6. Deciding: more data, better features, or new model

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

Practice: open `examples/06_deciding_more_data_better_features_or_ne.py`, predict the output, change one line, predict again.

## 7. Confusion matrix deep dive

A matrix is a linear transformation. Multiplying matrices composes transformations, which is exactly what stacking neural network layers does. Shapes must line up: (m,k) @ (k,n) -> (m,n); the inner dimensions must match and they vanish.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))
```

**Remember:** Read every shape error as 'the inner dimensions did not match' and print the shapes.

**Common mistake:** Reaching for `np.linalg.inv` to solve `Ax=b` instead of the numerically safer `np.linalg.solve`.

Practice: open `examples/07_confusion_matrix_deep_dive.py`, predict the output, change one line, predict again.

## 8. Finding annotation errors in the labels

One accuracy number tells you nothing about what to fix. Pull the wrong predictions, read fifty by hand, and sort them into buckets. Usually one bucket is 40% of the errors and has an obvious fix — and a surprising share turns out to be wrong labels, not wrong predictions.

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Remember:** Rank error buckets by share of total errors, not by error rate — fix what is actually costing you.

**Common mistake:** Optimising overall accuracy while one segment quietly gets 0% and generates every complaint.

Practice: open `examples/08_finding_annotation_errors_in_the_labels.py`, predict the output, change one line, predict again.

## 9. Prioritising fixes by business impact

Bayes' rule updates a belief with evidence: posterior = likelihood x prior / evidence. The most common mistake in applied ML is ignoring the prior — a 99%-accurate test for a 1-in-10000 disease still gives mostly false positives.

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Remember:** Rare events make precision collapse no matter how good the classifier looks on accuracy.

**Common mistake:** Reporting accuracy on an imbalanced problem where predicting 'no' always scores 99%.

Practice: open `examples/09_prioritising_fixes_by_business_impact.py`, predict the output, change one line, predict again.

## 10. Turning error analysis into a backlog

One accuracy number tells you nothing about what to fix. Pull the wrong predictions, read fifty by hand, and sort them into buckets. Usually one bucket is 40% of the errors and has an obvious fix — and a surprising share turns out to be wrong labels, not wrong predictions.

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))
```

**Remember:** Rank error buckets by share of total errors, not by error rate — fix what is actually costing you.

**Common mistake:** Optimising overall accuracy while one segment quietly gets 0% and generates every complaint.

Practice: open `examples/10_turning_error_analysis_into_a_backlog.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 73

- Explain **Why aggregate metrics hide the problem** to someone else without notes.
- Explain **Slicing errors by segment** to someone else without notes.
- Explain **Building an error taxonomy** to someone else without notes.
- Explain **Hand-labelling 50 wrong predictions** to someone else without notes.
- Explain **Identifying the biggest error bucket** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
