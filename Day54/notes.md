# Day 54 — Boosting

Today's goal: work through **Boosting** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Sequential error correction |
| 2 | AdaBoost intuition |
| 3 | Gradient boosting as gradient descent in function space |
| 4 | Learning rate and number of trees |
| 5 | Tree depth in boosting |
| 6 | Early stopping with a validation set |
| 7 | XGBoost, LightGBM, CatBoost compared |
| 8 | HistGradientBoosting in scikit-learn |
| 9 | Handling categorical features natively |
| 10 | Why boosting still beats deep nets on tables |

---

## 1. Sequential error correction

Boosting trains trees sequentially, each fixing the previous ensemble's errors. It usually beats random forests on tabular data and still beats deep learning there. The cost is that it genuinely needs tuning and will overfit if you let it run too long.

```python
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=3000, n_informative=8, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

model = HistGradientBoostingClassifier(
    learning_rate=0.1, max_iter=400, early_stopping=True,
    validation_fraction=0.15, random_state=0,
).fit(Xtr, ytr)
print('stopped at iteration', model.n_iter_, 'test acc', round(model.score(Xte, yte), 4))
```

**Remember:** Low learning rate + many trees + early stopping beats high learning rate + few trees.

**Common mistake:** Running a fixed 1000 rounds with no early stopping and shipping an overfit ensemble.

Practice: open `examples/01_sequential_error_correction.py`, predict the output, change one line, predict again.

## 2. AdaBoost intuition

Boosting trains trees sequentially, each fixing the previous ensemble's errors. It usually beats random forests on tabular data and still beats deep learning there. The cost is that it genuinely needs tuning and will overfit if you let it run too long.

```python
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=3000, n_informative=8, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

model = HistGradientBoostingClassifier(
    learning_rate=0.1, max_iter=400, early_stopping=True,
    validation_fraction=0.15, random_state=0,
).fit(Xtr, ytr)
print('stopped at iteration', model.n_iter_, 'test acc', round(model.score(Xte, yte), 4))
```

**Remember:** Low learning rate + many trees + early stopping beats high learning rate + few trees.

**Common mistake:** Running a fixed 1000 rounds with no early stopping and shipping an overfit ensemble.

Practice: open `examples/02_adaboost_intuition.py`, predict the output, change one line, predict again.

## 3. Gradient boosting as gradient descent in function space

The derivative answers: if I nudge this input a little, how much does the output move? The gradient is that answer for every input at once, so it points uphill. Training walks downhill by stepping against the gradient. The chain rule is what lets you propagate that answer through a stack of layers.

```python
import numpy as np

def f(x):
    return x ** 2 + 3 * x

def numeric_grad(fn, x, h=1e-6):
    return (fn(x + h) - fn(x - h)) / (2 * h)

x = 2.0
print('numeric  ', numeric_grad(f, x))
print('analytic ', 2 * x + 3)   # should match to ~1e-6
```

**Remember:** A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

**Common mistake:** Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

Practice: open `examples/03_gradient_boosting_as_gradient_descent_in.py`, predict the output, change one line, predict again.

## 4. Learning rate and number of trees

Gradient descent repeatedly steps against the gradient. Full-batch is stable but slow; stochastic is noisy but escapes shallow traps; mini-batch is the practical middle. The learning rate is the single most important knob you will ever turn.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 3))
true_w = np.array([1.0, -2.0, 0.5])
y = X @ true_w + rng.normal(scale=0.1, size=1000)

w, lr, batch = np.zeros(3), 0.1, 32
for epoch in range(20):
    idx = rng.permutation(len(X))
    for start in range(0, len(X), batch):
        b = idx[start:start + batch]
        grad = 2 * X[b].T @ (X[b] @ w - y[b]) / len(b)
        w -= lr * grad
print('learned', np.round(w, 3), 'target', true_w)
```

**Remember:** Shuffle every epoch, otherwise the model learns the order of your file.

**Common mistake:** Leaving the learning rate fixed forever instead of decaying it once the loss plateaus.

Practice: open `examples/04_learning_rate_and_number_of_trees.py`, predict the output, change one line, predict again.

## 5. Tree depth in boosting

Boosting trains trees sequentially, each fixing the previous ensemble's errors. It usually beats random forests on tabular data and still beats deep learning there. The cost is that it genuinely needs tuning and will overfit if you let it run too long.

```python
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=3000, n_informative=8, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

model = HistGradientBoostingClassifier(
    learning_rate=0.1, max_iter=400, early_stopping=True,
    validation_fraction=0.15, random_state=0,
).fit(Xtr, ytr)
print('stopped at iteration', model.n_iter_, 'test acc', round(model.score(Xte, yte), 4))
```

**Remember:** Low learning rate + many trees + early stopping beats high learning rate + few trees.

**Common mistake:** Running a fixed 1000 rounds with no early stopping and shipping an overfit ensemble.

Practice: open `examples/05_tree_depth_in_boosting.py`, predict the output, change one line, predict again.

## 6. Early stopping with a validation set

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

Practice: open `examples/06_early_stopping_with_a_validation_set.py`, predict the output, change one line, predict again.

## 7. XGBoost, LightGBM, CatBoost compared

Boosting trains trees sequentially, each fixing the previous ensemble's errors. It usually beats random forests on tabular data and still beats deep learning there. The cost is that it genuinely needs tuning and will overfit if you let it run too long.

```python
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=3000, n_informative=8, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

model = HistGradientBoostingClassifier(
    learning_rate=0.1, max_iter=400, early_stopping=True,
    validation_fraction=0.15, random_state=0,
).fit(Xtr, ytr)
print('stopped at iteration', model.n_iter_, 'test acc', round(model.score(Xte, yte), 4))
```

**Remember:** Low learning rate + many trees + early stopping beats high learning rate + few trees.

**Common mistake:** Running a fixed 1000 rounds with no early stopping and shipping an overfit ensemble.

Practice: open `examples/07_xgboost_lightgbm_catboost_compared.py`, predict the output, change one line, predict again.

## 8. HistGradientBoosting in scikit-learn

The derivative answers: if I nudge this input a little, how much does the output move? The gradient is that answer for every input at once, so it points uphill. Training walks downhill by stepping against the gradient. The chain rule is what lets you propagate that answer through a stack of layers.

```python
import numpy as np

def f(x):
    return x ** 2 + 3 * x

def numeric_grad(fn, x, h=1e-6):
    return (fn(x + h) - fn(x - h)) / (2 * h)

x = 2.0
print('numeric  ', numeric_grad(f, x))
print('analytic ', 2 * x + 3)   # should match to ~1e-6
```

**Remember:** A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

**Common mistake:** Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

Practice: open `examples/08_histgradientboosting_in_scikit_learn.py`, predict the output, change one line, predict again.

## 9. Handling categorical features natively

Boosting trains trees sequentially, each fixing the previous ensemble's errors. It usually beats random forests on tabular data and still beats deep learning there. The cost is that it genuinely needs tuning and will overfit if you let it run too long.

```python
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=3000, n_informative=8, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

model = HistGradientBoostingClassifier(
    learning_rate=0.1, max_iter=400, early_stopping=True,
    validation_fraction=0.15, random_state=0,
).fit(Xtr, ytr)
print('stopped at iteration', model.n_iter_, 'test acc', round(model.score(Xte, yte), 4))
```

**Remember:** Low learning rate + many trees + early stopping beats high learning rate + few trees.

**Common mistake:** Running a fixed 1000 rounds with no early stopping and shipping an overfit ensemble.

Practice: open `examples/09_handling_categorical_features_natively.py`, predict the output, change one line, predict again.

## 10. Why boosting still beats deep nets on tables

Boosting trains trees sequentially, each fixing the previous ensemble's errors. It usually beats random forests on tabular data and still beats deep learning there. The cost is that it genuinely needs tuning and will overfit if you let it run too long.

```python
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=3000, n_informative=8, random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=0)

model = HistGradientBoostingClassifier(
    learning_rate=0.1, max_iter=400, early_stopping=True,
    validation_fraction=0.15, random_state=0,
).fit(Xtr, ytr)
print('stopped at iteration', model.n_iter_, 'test acc', round(model.score(Xte, yte), 4))
```

**Remember:** Low learning rate + many trees + early stopping beats high learning rate + few trees.

**Common mistake:** Running a fixed 1000 rounds with no early stopping and shipping an overfit ensemble.

Practice: open `examples/10_why_boosting_still_beats_deep_nets_on_ta.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 54

- Explain **Sequential error correction** to someone else without notes.
- Explain **AdaBoost intuition** to someone else without notes.
- Explain **Gradient boosting as gradient descent in function space** to someone else without notes.
- Explain **Learning rate and number of trees** to someone else without notes.
- Explain **Tree depth in boosting** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
