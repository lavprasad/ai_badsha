# Day 64 — Ensembling your own models

Today's goal: work through **Ensembling your own models** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why ensembles work |
| 2 | Voting classifiers: hard and soft |
| 3 | Averaging regressors |
| 4 | Weighted blending |
| 5 | Stacking with a meta-learner |
| 6 | Out-of-fold predictions for stacking |
| 7 | Diversity beats individual strength |
| 8 | Complexity cost in production |
| 9 | When a single model is the right call |
| 10 | Building a stacked ensemble correctly |

---

## 1. Why ensembles work

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

Practice: open `examples/01_why_ensembles_work.py`, predict the output, change one line, predict again.

## 2. Voting classifiers: hard and soft

Ensembles work when the members make *different* mistakes. Averaging correlated models buys nothing. Stacking trains a meta-model on out-of-fold predictions — using in-fold predictions leaks and produces a meta-model that looks perfect and fails instantly.

```python
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))
```

**Remember:** Stack on out-of-fold predictions only. In-fold predictions are a leak wearing a disguise.

**Common mistake:** Shipping a five-model ensemble for a 0.2% gain and quintupling inference cost and failure modes.

Practice: open `examples/02_voting_classifiers_hard_and_soft.py`, predict the output, change one line, predict again.

## 3. Averaging regressors

RAG grounds answers in your documents: chunk, embed, store, retrieve the top-k for the question, and put them in the prompt. Retrieval quality is the whole ballgame — a perfect model answering from the wrong three chunks is still wrong.

```python
import numpy as np

docs = [
    'Refunds are processed within 5 business days.',
    'Our office is in Pune, open 9am to 6pm.',
    'Enterprise plans include a dedicated support engineer.',
]

def fake_embed(text):                       # stand-in for a real embedding model
    rng = np.random.default_rng(abs(hash(text)) % (2 ** 32))
    v = rng.normal(size=32)
    return v / np.linalg.norm(v)

index = np.array([fake_embed(d) for d in docs])
q = fake_embed('how long do refunds take')
top = int(np.argmax(index @ q))
print('retrieved:', docs[top])
print('\\nReal pipeline: chunk 300-800 tokens with overlap -> embed -> ANN index -> rerank -> prompt.')
```

**Remember:** Always show the source of each retrieved chunk in the answer so users can verify it.

**Common mistake:** Chunking blindly at 1000 characters and cutting tables and code blocks in half.

Practice: open `examples/03_averaging_regressors.py`, predict the output, change one line, predict again.

## 4. Weighted blending

Ensembles work when the members make *different* mistakes. Averaging correlated models buys nothing. Stacking trains a meta-model on out-of-fold predictions — using in-fold predictions leaks and produces a meta-model that looks perfect and fails instantly.

```python
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))
```

**Remember:** Stack on out-of-fold predictions only. In-fold predictions are a leak wearing a disguise.

**Common mistake:** Shipping a five-model ensemble for a 0.2% gain and quintupling inference cost and failure modes.

Practice: open `examples/04_weighted_blending.py`, predict the output, change one line, predict again.

## 5. Stacking with a meta-learner

NumPy's power is selecting and combining without loops. A boolean mask picks rows by condition, fancy indexing picks them by position, `np.where` builds a new array from a condition, and `argsort` gives you the ordering so you can sort several arrays consistently.

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Remember:** A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.

**Common mistake:** Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

Practice: open `examples/05_stacking_with_a_meta_learner.py`, predict the output, change one line, predict again.

## 6. Out-of-fold predictions for stacking

NumPy's power is selecting and combining without loops. A boolean mask picks rows by condition, fancy indexing picks them by position, `np.where` builds a new array from a condition, and `argsort` gives you the ordering so you can sort several arrays consistently.

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Remember:** A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.

**Common mistake:** Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

Practice: open `examples/06_out_of_fold_predictions_for_stacking.py`, predict the output, change one line, predict again.

## 7. Diversity beats individual strength

Ensembles work when the members make *different* mistakes. Averaging correlated models buys nothing. Stacking trains a meta-model on out-of-fold predictions — using in-fold predictions leaks and produces a meta-model that looks perfect and fails instantly.

```python
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))
```

**Remember:** Stack on out-of-fold predictions only. In-fold predictions are a leak wearing a disguise.

**Common mistake:** Shipping a five-model ensemble for a 0.2% gain and quintupling inference cost and failure modes.

Practice: open `examples/07_diversity_beats_individual_strength.py`, predict the output, change one line, predict again.

## 8. Complexity cost in production

Today's idea — **Complexity cost in production** — sits inside the theme of Ensembling your own models. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Complexity cost in production
print("practice: Complexity cost in production")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Complexity cost in production` makes about your data before you use it.

**Common mistake:** Copy-pasting `Complexity cost in production` from a tutorial without knowing what it assumes or when it fails.

Practice: open `examples/08_complexity_cost_in_production.py`, predict the output, change one line, predict again.

## 9. When a single model is the right call

Ensembles work when the members make *different* mistakes. Averaging correlated models buys nothing. Stacking trains a meta-model on out-of-fold predictions — using in-fold predictions leaks and produces a meta-model that looks perfect and fails instantly.

```python
import numpy as np
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)

base = [RandomForestClassifier(n_estimators=200, random_state=0),
        LogisticRegression(max_iter=5000)]
oof = np.column_stack([
    cross_val_predict(m, X, y, cv=cv, method='predict_proba')[:, 1] for m in base
])
print('correlation between members:', round(float(np.corrcoef(oof.T)[0, 1]), 3))
meta = LogisticRegression().fit(oof, y)
print('meta weights:', meta.coef_.round(3))
```

**Remember:** Stack on out-of-fold predictions only. In-fold predictions are a leak wearing a disguise.

**Common mistake:** Shipping a five-model ensemble for a 0.2% gain and quintupling inference cost and failure modes.

Practice: open `examples/09_when_a_single_model_is_the_right_call.py`, predict the output, change one line, predict again.

## 10. Building a stacked ensemble correctly

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

Practice: open `examples/10_building_a_stacked_ensemble_correctly.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 64

- Explain **Why ensembles work** to someone else without notes.
- Explain **Voting classifiers: hard and soft** to someone else without notes.
- Explain **Averaging regressors** to someone else without notes.
- Explain **Weighted blending** to someone else without notes.
- Explain **Stacking with a meta-learner** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
