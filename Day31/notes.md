# Day 31 — Linear models, mathematically

Today's goal: work through **linear models, mathematically** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | The linear model equation |
| 2 | Least squares as a projection |
| 3 | Deriving the normal equations |
| 4 | Gradient descent solution |
| 5 | Adding a bias term correctly |
| 6 | Polynomial features |
| 7 | Multicollinearity and its symptoms |
| 8 | Ridge as constrained least squares |
| 9 | Lasso and sparsity geometry |
| 10 | Interpreting coefficients honestly |

---

## 1. The linear model equation

Today's idea — **The linear model equation** — sits inside the theme of Linear models, mathematically. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: The linear model equation
print("practice: The linear model equation")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `The linear model equation` makes about your data before you use it.

**Common mistake:** Copy-pasting `The linear model equation` from a tutorial without knowing what it assumes or when it fails.

## 2. Least squares as a projection

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 3. Deriving the normal equations

A vector is a list of numbers with a direction and length. The dot product measures alignment: large and positive when two vectors point the same way, zero when perpendicular. Cosine similarity is the dot product with length divided out, which is why it compares embeddings of different magnitudes fairly.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Remember:** Cosine similarity ignores magnitude; Euclidean distance does not. Pick the one that matches your question.

**Common mistake:** Comparing raw embeddings with Euclidean distance when only direction carries meaning.

## 4. Gradient descent solution

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

## 5. Adding a bias term correctly

Models learn the bias in their training data and then apply it at scale with a veneer of objectivity. Measure error rates per group, not just overall. Fairness definitions genuinely conflict with each other — you must choose one explicitly and document why.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'group': ['a'] * 100 + ['b'] * 100,
    'y':     [1] * 50 + [0] * 50 + [1] * 50 + [0] * 50,
    'pred':  [1] * 45 + [0] * 55 + [1] * 30 + [0] * 70,
})
for g, sub in df.groupby('group'):
    tpr = ((sub.pred == 1) & (sub.y == 1)).sum() / max((sub.y == 1).sum(), 1)
    rate = (sub.pred == 1).mean()
    print(f'group {g}: selection rate {rate:.2f}  recall {tpr:.2f}')
print('Large gaps here are the finding — investigate before shipping.')
```

**Remember:** Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

**Common mistake:** Auditing fairness once at launch and never again as the data drifts.

## 6. Polynomial features

Today's idea — **Polynomial features** — sits inside the theme of Linear models, mathematically. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Polynomial features
print("practice: Polynomial features")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Polynomial features` makes about your data before you use it.

**Common mistake:** Copy-pasting `Polynomial features` from a tutorial without knowing what it assumes or when it fails.

## 7. Multicollinearity and its symptoms

Today's idea — **Multicollinearity and its symptoms** — sits inside the theme of Linear models, mathematically. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Multicollinearity and its symptoms
print("practice: Multicollinearity and its symptoms")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Multicollinearity and its symptoms` makes about your data before you use it.

**Common mistake:** Copy-pasting `Multicollinearity and its symptoms` from a tutorial without knowing what it assumes or when it fails.

## 8. Ridge as constrained least squares

Linear regression fits a straight line by minimising squared error. It is the honest baseline for every regression problem: fast, interpretable, and the thing your fancy model must beat before it earns its complexity.

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 1))
y = 3.0 * X[:, 0] + 2.0 + rng.normal(scale=0.5, size=200)

Xb = np.c_[np.ones(len(X)), X]                 # add bias column
w = np.linalg.lstsq(Xb, y, rcond=None)[0]      # solves the normal equations safely
print(f'intercept {w[0]:.3f}  slope {w[1]:.3f}')

resid = y - Xb @ w
print('residual mean (should be ~0):', round(float(resid.mean()), 6))
```

**Remember:** Plot residuals against predictions — any visible pattern means the linear form is wrong.

**Common mistake:** Reporting R² on training data and calling it model performance.

## 9. Lasso and sparsity geometry

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

## 10. Interpreting coefficients honestly

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

---

## What you should be able to do after Day 31

- Explain **The linear model equation** to someone else without notes.
- Explain **Least squares as a projection** to someone else without notes.
- Explain **Deriving the normal equations** to someone else without notes.
- Explain **Gradient descent solution** to someone else without notes.
- Explain **Adding a bias term correctly** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
