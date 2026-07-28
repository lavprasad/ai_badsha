# Day 53 — Ensembles: bagging and random forests

Today's goal: work through **Ensembles: bagging and random forests** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Wisdom of uncorrelated errors |
| 2 | Bootstrap sampling |
| 3 | Bagging |
| 4 | Random feature subsets |
| 5 | Out-of-bag error estimation |
| 6 | Tuning a random forest |
| 7 | Feature importance and its bias |
| 8 | Permutation importance |
| 9 | Extremely randomised trees |
| 10 | Random forest as the tabular default |

---

## 1. Wisdom of uncorrelated errors

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/01_wisdom_of_uncorrelated_errors.py`, predict the output, change one line, predict again.

## 2. Bootstrap sampling

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

Practice: open `examples/02_bootstrap_sampling.py`, predict the output, change one line, predict again.

## 3. Bagging

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/03_bagging.py`, predict the output, change one line, predict again.

## 4. Random feature subsets

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/04_random_feature_subsets.py`, predict the output, change one line, predict again.

## 5. Out-of-bag error estimation

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/05_out_of_bag_error_estimation.py`, predict the output, change one line, predict again.

## 6. Tuning a random forest

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/06_tuning_a_random_forest.py`, predict the output, change one line, predict again.

## 7. Feature importance and its bias

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/07_feature_importance_and_its_bias.py`, predict the output, change one line, predict again.

## 8. Permutation importance

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/08_permutation_importance.py`, predict the output, change one line, predict again.

## 9. Extremely randomised trees

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/09_extremely_randomised_trees.py`, predict the output, change one line, predict again.

## 10. Random forest as the tabular default

Bagging trains many trees on bootstrap samples with random feature subsets, then averages. Averaging cancels the variance that makes single trees erratic. Random forests are the best default for tabular data when you want something that works with almost no tuning.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import cross_val_score

X, y = load_breast_cancer(return_X_y=True)
rf = RandomForestClassifier(n_estimators=300, min_samples_leaf=2, n_jobs=-1, random_state=0)
print('cv accuracy', cross_val_score(rf, X, y, cv=5).mean().round(4))

rf.fit(X, y)
top = sorted(zip(load_breast_cancer().feature_names, rf.feature_importances_), key=lambda t: -t[1])[:5]
print('top features', [(n, round(v, 3)) for n, v in top])
```

**Remember:** More trees never overfit — they only cost time. Depth and leaf size are the knobs that control fit.

**Common mistake:** Using impurity-based importances for business decisions instead of permutation importance.

Practice: open `examples/10_random_forest_as_the_tabular_default.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 53

- Explain **Wisdom of uncorrelated errors** to someone else without notes.
- Explain **Bootstrap sampling** to someone else without notes.
- Explain **Bagging** to someone else without notes.
- Explain **Random feature subsets** to someone else without notes.
- Explain **Out-of-bag error estimation** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
