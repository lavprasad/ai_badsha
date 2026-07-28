# Day 56 — Model selection and validation strategy

Today's goal: work through **Model selection and validation strategy** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Comparing models fairly |
| 2 | Cross-validation as the default |
| 3 | Repeated and stratified CV |
| 4 | Standard error across folds |
| 5 | Statistical comparison of two models |
| 6 | The one-standard-error rule |
| 7 | Nested CV for honest estimates |
| 8 | Validation curves |
| 9 | Learning curves and what they diagnose |
| 10 | Choosing simplest-that-works |

---

## 1. Comparing models fairly

Two models differing by 0.3% with a 2% fold-to-fold spread are the same model. Compare on identical folds, look at the spread, and when scores tie, take the simpler model — the one-standard-error rule. Nested CV is the honest way to report a score when you also tuned hyperparameters.

```python
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)   # identical folds for both

for name, model in [
    ('logreg', make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))),
    ('forest', RandomForestClassifier(n_estimators=300, random_state=0)),
]:
    s = cross_val_score(model, X, y, cv=cv)
    print(f'{name}: {s.mean():.4f} +/- {s.std():.4f}   folds {s.round(3)}')
```

**Remember:** Use the same `cv` object for every candidate, or you are comparing luck.

**Common mistake:** Declaring a winner from a difference smaller than the standard error across folds.

## 2. Cross-validation as the default

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

## 3. Repeated and stratified CV

Two models differing by 0.3% with a 2% fold-to-fold spread are the same model. Compare on identical folds, look at the spread, and when scores tie, take the simpler model — the one-standard-error rule. Nested CV is the honest way to report a score when you also tuned hyperparameters.

```python
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)   # identical folds for both

for name, model in [
    ('logreg', make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))),
    ('forest', RandomForestClassifier(n_estimators=300, random_state=0)),
]:
    s = cross_val_score(model, X, y, cv=cv)
    print(f'{name}: {s.mean():.4f} +/- {s.std():.4f}   folds {s.round(3)}')
```

**Remember:** Use the same `cv` object for every candidate, or you are comparing luck.

**Common mistake:** Declaring a winner from a difference smaller than the standard error across folds.

## 4. Standard error across folds

Two models differing by 0.3% with a 2% fold-to-fold spread are the same model. Compare on identical folds, look at the spread, and when scores tie, take the simpler model — the one-standard-error rule. Nested CV is the honest way to report a score when you also tuned hyperparameters.

```python
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)   # identical folds for both

for name, model in [
    ('logreg', make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))),
    ('forest', RandomForestClassifier(n_estimators=300, random_state=0)),
]:
    s = cross_val_score(model, X, y, cv=cv)
    print(f'{name}: {s.mean():.4f} +/- {s.std():.4f}   folds {s.round(3)}')
```

**Remember:** Use the same `cv` object for every candidate, or you are comparing luck.

**Common mistake:** Declaring a winner from a difference smaller than the standard error across folds.

## 5. Statistical comparison of two models

Today's idea — **Statistical comparison of two models** — sits inside the theme of Model selection and validation strategy. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Statistical comparison of two models
print("practice: Statistical comparison of two models")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Statistical comparison of two models` makes about your data before you use it.

**Common mistake:** Copy-pasting `Statistical comparison of two models` from a tutorial without knowing what it assumes or when it fails.

## 6. The one-standard-error rule

Two models differing by 0.3% with a 2% fold-to-fold spread are the same model. Compare on identical folds, look at the spread, and when scores tie, take the simpler model — the one-standard-error rule. Nested CV is the honest way to report a score when you also tuned hyperparameters.

```python
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)   # identical folds for both

for name, model in [
    ('logreg', make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))),
    ('forest', RandomForestClassifier(n_estimators=300, random_state=0)),
]:
    s = cross_val_score(model, X, y, cv=cv)
    print(f'{name}: {s.mean():.4f} +/- {s.std():.4f}   folds {s.round(3)}')
```

**Remember:** Use the same `cv` object for every candidate, or you are comparing luck.

**Common mistake:** Declaring a winner from a difference smaller than the standard error across folds.

## 7. Nested CV for honest estimates

Two models differing by 0.3% with a 2% fold-to-fold spread are the same model. Compare on identical folds, look at the spread, and when scores tie, take the simpler model — the one-standard-error rule. Nested CV is the honest way to report a score when you also tuned hyperparameters.

```python
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)   # identical folds for both

for name, model in [
    ('logreg', make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))),
    ('forest', RandomForestClassifier(n_estimators=300, random_state=0)),
]:
    s = cross_val_score(model, X, y, cv=cv)
    print(f'{name}: {s.mean():.4f} +/- {s.std():.4f}   folds {s.round(3)}')
```

**Remember:** Use the same `cv` object for every candidate, or you are comparing luck.

**Common mistake:** Declaring a winner from a difference smaller than the standard error across folds.

## 8. Validation curves

Two models differing by 0.3% with a 2% fold-to-fold spread are the same model. Compare on identical folds, look at the spread, and when scores tie, take the simpler model — the one-standard-error rule. Nested CV is the honest way to report a score when you also tuned hyperparameters.

```python
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)   # identical folds for both

for name, model in [
    ('logreg', make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))),
    ('forest', RandomForestClassifier(n_estimators=300, random_state=0)),
]:
    s = cross_val_score(model, X, y, cv=cv)
    print(f'{name}: {s.mean():.4f} +/- {s.std():.4f}   folds {s.round(3)}')
```

**Remember:** Use the same `cv` object for every candidate, or you are comparing luck.

**Common mistake:** Declaring a winner from a difference smaller than the standard error across folds.

## 9. Learning curves and what they diagnose

Underfitting is high bias: the model is too simple and is wrong everywhere, including on training data. Overfitting is high variance: it memorised the training set and falls apart on new data. The gap between train and validation score tells you which one you have.

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=800, n_informative=5, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)

for depth in (1, 3, 8, None):
    m = DecisionTreeClassifier(max_depth=depth, random_state=0).fit(Xtr, ytr)
    print(f'depth={str(depth):>4}  train={m.score(Xtr, ytr):.3f}  test={m.score(Xte, yte):.3f}')
```

**Remember:** Train 1.00 / test 0.70 is overfitting. Train 0.70 / test 0.69 is underfitting. Fix the right one.

**Common mistake:** Adding capacity to fix a gap that was caused by too little data or a leak, not by too little capacity.

## 10. Choosing simplest-that-works

Two models differing by 0.3% with a 2% fold-to-fold spread are the same model. Compare on identical folds, look at the spread, and when scores tie, take the simpler model — the one-standard-error rule. Nested CV is the honest way to report a score when you also tuned hyperparameters.

```python
import numpy as np
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
cv = StratifiedKFold(5, shuffle=True, random_state=0)   # identical folds for both

for name, model in [
    ('logreg', make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))),
    ('forest', RandomForestClassifier(n_estimators=300, random_state=0)),
]:
    s = cross_val_score(model, X, y, cv=cv)
    print(f'{name}: {s.mean():.4f} +/- {s.std():.4f}   folds {s.round(3)}')
```

**Remember:** Use the same `cv` object for every candidate, or you are comparing luck.

**Common mistake:** Declaring a winner from a difference smaller than the standard error across folds.

---

## What you should be able to do after Day 56

- Explain **Comparing models fairly** to someone else without notes.
- Explain **Cross-validation as the default** to someone else without notes.
- Explain **Repeated and stratified CV** to someone else without notes.
- Explain **Standard error across folds** to someone else without notes.
- Explain **Statistical comparison of two models** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
