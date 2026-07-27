# Day 47 — Regularised linear models

Today's goal: work through **regularised linear models** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why unregularised models overfit wide data |
| 2 | Ridge regression |
| 3 | Lasso and automatic feature selection |
| 4 | Elastic net |
| 5 | Choosing alpha with cross-validation |
| 6 | The scaling requirement |
| 7 | Coefficient paths |
| 8 | Regularisation for logistic regression |
| 9 | Sparse models for interpretability |
| 10 | Comparing all four on one dataset |

---

## 1. Why unregularised models overfit wide data

Today's idea — **Why unregularised models overfit wide data** — sits inside the theme of Regularised linear models. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Why unregularised models overfit wide data
print("practice: Why unregularised models overfit wide data")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Why unregularised models overfit wide data` makes about your data before you use it.

**Common mistake:** Copy-pasting `Why unregularised models overfit wide data` from a tutorial without knowing what it assumes or when it fails.

## 2. Ridge regression

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=200, n_features=20, n_informative=5, noise=10, random_state=0)

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=1.0).fit(X, y)
print('ridge non-zero coefs', int(np.sum(np.abs(ridge.coef_) > 1e-6)))
print('lasso non-zero coefs', int(np.sum(np.abs(lasso.coef_) > 1e-6)))
```

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

## 3. Lasso and automatic feature selection

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=200, n_features=20, n_informative=5, noise=10, random_state=0)

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=1.0).fit(X, y)
print('ridge non-zero coefs', int(np.sum(np.abs(ridge.coef_) > 1e-6)))
print('lasso non-zero coefs', int(np.sum(np.abs(lasso.coef_) > 1e-6)))
```

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

## 4. Elastic net

Regularisation penalises large weights so the model prefers simpler explanations. L2 (ridge) shrinks everything smoothly; L1 (lasso) drives some weights exactly to zero and thereby selects features. Elastic net mixes both.

```python
import numpy as np
from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=200, n_features=20, n_informative=5, noise=10, random_state=0)

ridge = Ridge(alpha=1.0).fit(X, y)
lasso = Lasso(alpha=1.0).fit(X, y)
print('ridge non-zero coefs', int(np.sum(np.abs(ridge.coef_) > 1e-6)))
print('lasso non-zero coefs', int(np.sum(np.abs(lasso.coef_) > 1e-6)))
```

**Remember:** Scale features before regularising, or the penalty punishes whichever column happens to use small units.

**Common mistake:** Tuning `alpha` on the test set — pick it with cross-validation on train only.

## 5. Choosing alpha with cross-validation

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

## 6. The scaling requirement

Data parallelism replicates the model and splits the batch; model parallelism splits the model when it will not fit on one device. Scale only after profiling — most 'we need more GPUs' problems are actually a slow data loader.

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Remember:** Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.

**Common mistake:** Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

## 7. Coefficient paths

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

## 8. Regularisation for logistic regression

Logistic regression squashes a linear score through a sigmoid to get a probability. The coefficients are log-odds: +0.7 means the odds roughly double per unit. It stays the default for anything where you must explain the decision to a regulator.

```python
import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

rng = np.random.default_rng(0)
X = rng.normal(size=(400, 2))
y = (X[:, 0] + X[:, 1] > 0).astype(float)

w, b, lr = np.zeros(2), 0.0, 0.5
for _ in range(500):
    p = sigmoid(X @ w + b)
    w -= lr * (X.T @ (p - y)) / len(y)
    b -= lr * float((p - y).mean())
print('weights', np.round(w, 2), 'acc', ((sigmoid(X @ w + b) > 0.5) == y).mean())
```

**Remember:** Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

**Common mistake:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

## 9. Sparse models for interpretability

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
names = load_breast_cancer().feature_names
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
m = RandomForestClassifier(n_estimators=200, random_state=0, n_jobs=-1).fit(Xtr, ytr)

imp = permutation_importance(m, Xte, yte, n_repeats=10, random_state=0)
for i in np.argsort(-imp.importances_mean)[:5]:
    print(f'{names[i]:<28} {imp.importances_mean[i]:.4f}')
```

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

## 10. Comparing all four on one dataset

Today's idea — **Comparing all four on one dataset** — sits inside the theme of Regularised linear models. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Comparing all four on one dataset
print("practice: Comparing all four on one dataset")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Comparing all four on one dataset` makes about your data before you use it.

**Common mistake:** Copy-pasting `Comparing all four on one dataset` from a tutorial without knowing what it assumes or when it fails.

---

## What you should be able to do after Day 47

- Explain **Why unregularised models overfit wide data** to someone else without notes.
- Explain **Ridge regression** to someone else without notes.
- Explain **Lasso and automatic feature selection** to someone else without notes.
- Explain **Elastic net** to someone else without notes.
- Explain **Choosing alpha with cross-validation** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
