# Day 41 — Data splitting done right

Today's goal: work through **data splitting done right** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Train, validation and test roles |
| 2 | Random split |
| 3 | Stratified split for imbalance |
| 4 | Group split to avoid entity leakage |
| 5 | Time-based split for temporal data |
| 6 | K-fold cross-validation |
| 7 | Stratified and grouped K-fold |
| 8 | Nested cross-validation |
| 9 | How many splits is too many |
| 10 | Locking the test set away |

---

## 1. Train, validation and test roles

Train fits parameters, validation chooses everything else, test is opened once. Stratify when classes are imbalanced, group when the same entity appears many times, split by time when the future is what you predict. The wrong split invalidates every number that follows.

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Remember:** One entity must live on exactly one side of the split. Check the overlap; do not assume it.

**Common mistake:** A random split on data with repeated customers, so the model recognises the customer, not the pattern.

## 2. Random split

Train fits parameters, validation chooses everything else, test is opened once. Stratify when classes are imbalanced, group when the same entity appears many times, split by time when the future is what you predict. The wrong split invalidates every number that follows.

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Remember:** One entity must live on exactly one side of the split. Check the overlap; do not assume it.

**Common mistake:** A random split on data with repeated customers, so the model recognises the customer, not the pattern.

## 3. Stratified split for imbalance

Train fits parameters, validation chooses everything else, test is opened once. Stratify when classes are imbalanced, group when the same entity appears many times, split by time when the future is what you predict. The wrong split invalidates every number that follows.

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Remember:** One entity must live on exactly one side of the split. Check the overlap; do not assume it.

**Common mistake:** A random split on data with repeated customers, so the model recognises the customer, not the pattern.

## 4. Group split to avoid entity leakage

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

## 5. Time-based split for temporal data

Train fits parameters, validation chooses everything else, test is opened once. Stratify when classes are imbalanced, group when the same entity appears many times, split by time when the future is what you predict. The wrong split invalidates every number that follows.

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Remember:** One entity must live on exactly one side of the split. Check the overlap; do not assume it.

**Common mistake:** A random split on data with repeated customers, so the model recognises the customer, not the pattern.

## 6. K-fold cross-validation

Three splits, three jobs: train fits parameters, validation picks hyperparameters, test gives one honest final number. K-fold cross-validation reuses data by rotating the validation slice, which matters when you only have a few thousand rows.

```python
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

X, y = load_wine(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=cv)
print('folds', scores.round(3))
print(f'mean {scores.mean():.3f} +/- {scores.std():.3f}')
```

**Remember:** Report the spread across folds, not just the mean — high variance means you cannot trust the mean.

**Common mistake:** Random K-fold on time-series or on grouped data (same patient in train and test) — both leak.

## 7. Stratified and grouped K-fold

Three splits, three jobs: train fits parameters, validation picks hyperparameters, test gives one honest final number. K-fold cross-validation reuses data by rotating the validation slice, which matters when you only have a few thousand rows.

```python
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

X, y = load_wine(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=cv)
print('folds', scores.round(3))
print(f'mean {scores.mean():.3f} +/- {scores.std():.3f}')
```

**Remember:** Report the spread across folds, not just the mean — high variance means you cannot trust the mean.

**Common mistake:** Random K-fold on time-series or on grouped data (same patient in train and test) — both leak.

## 8. Nested cross-validation

Three splits, three jobs: train fits parameters, validation picks hyperparameters, test gives one honest final number. K-fold cross-validation reuses data by rotating the validation slice, which matters when you only have a few thousand rows.

```python
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold

X, y = load_wine(return_X_y=True)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
scores = cross_val_score(RandomForestClassifier(random_state=0), X, y, cv=cv)
print('folds', scores.round(3))
print(f'mean {scores.mean():.3f} +/- {scores.std():.3f}')
```

**Remember:** Report the spread across folds, not just the mean — high variance means you cannot trust the mean.

**Common mistake:** Random K-fold on time-series or on grouped data (same patient in train and test) — both leak.

## 9. How many splits is too many

Train fits parameters, validation chooses everything else, test is opened once. Stratify when classes are imbalanced, group when the same entity appears many times, split by time when the future is what you predict. The wrong split invalidates every number that follows.

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Remember:** One entity must live on exactly one side of the split. Check the overlap; do not assume it.

**Common mistake:** A random split on data with repeated customers, so the model recognises the customer, not the pattern.

## 10. Locking the test set away

Train fits parameters, validation chooses everything else, test is opened once. Stratify when classes are imbalanced, group when the same entity appears many times, split by time when the future is what you predict. The wrong split invalidates every number that follows.

```python
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit, GroupShuffleSplit

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 3))
y = (rng.random(200) < 0.1).astype(int)      # 10% positive
groups = rng.integers(0, 40, size=200)       # 40 customers

_, _, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
print('stratified positive rate  train %.3f  test %.3f' % (ytr.mean(), yte.mean()))

tr, te = next(GroupShuffleSplit(test_size=0.3, random_state=0).split(X, y, groups))
print('group overlap (must be 0):', len(set(groups[tr]) & set(groups[te])))
```

**Remember:** One entity must live on exactly one side of the split. Check the overlap; do not assume it.

**Common mistake:** A random split on data with repeated customers, so the model recognises the customer, not the pattern.

---

## What you should be able to do after Day 41

- Explain **Train, validation and test roles** to someone else without notes.
- Explain **Random split** to someone else without notes.
- Explain **Stratified split for imbalance** to someone else without notes.
- Explain **Group split to avoid entity leakage** to someone else without notes.
- Explain **Time-based split for temporal data** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
