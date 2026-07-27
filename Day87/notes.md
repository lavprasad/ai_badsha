# Day 87 — Debugging neural networks

Today's goal: work through **debugging neural networks** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Overfit a single batch first |
| 2 | Check loss at initialisation |
| 3 | Verify the data reaching the model |
| 4 | Shape errors and how to read them |
| 5 | NaN loss: causes and fixes |
| 6 | Exploding and vanishing gradients |
| 7 | Learning rate diagnosis from the curve |
| 8 | Dead ReLU detection |
| 9 | Comparing against a simple baseline |
| 10 | A deep learning debugging checklist |

---

## 1. Overfit a single batch first

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

## 2. Check loss at initialisation

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

## 3. Verify the data reaching the model

Today's idea — **Verify the data reaching the model** — sits inside the theme of Debugging neural networks. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Verify the data reaching the model
print("practice: Verify the data reaching the model")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Verify the data reaching the model` makes about your data before you use it.

**Common mistake:** Copy-pasting `Verify the data reaching the model` from a tutorial without knowing what it assumes or when it fails.

## 4. Shape errors and how to read them

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

## 5. NaN loss: causes and fixes

Missing data is information, not just noise. Before filling anything, ask *why* it is missing: a sensor that fails only under load is not missing at random. Then choose: drop rows, drop the column, fill with a statistic, or add an explicit 'was missing' indicator column.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Remember:** Compute the fill statistic on the TRAIN split only, then apply it to test.

**Common mistake:** Filling with the mean computed over the full dataset — that leaks test information into training.

## 6. Exploding and vanishing gradients

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

## 7. Learning rate diagnosis from the curve

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

## 8. Dead ReLU detection

ReLU is the default: cheap, and it does not saturate for positive inputs. Sigmoid and tanh squash into a fixed range and kill gradients at the extremes. GELU/SiLU are smoother ReLUs used in transformers. Softmax turns a vector of scores into a probability distribution.

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)   # subtract max for numerical stability
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

logits = np.array([2.0, 1.0, 0.1])
print('softmax', softmax(logits).round(4), 'sums to', softmax(logits).sum())
print('relu   ', np.maximum(0, np.array([-1.0, 0.0, 2.0])))
```

**Remember:** Always subtract the max before `exp` in softmax, or large logits overflow to inf/NaN.

**Common mistake:** Putting a softmax on the final layer AND using a loss that applies softmax internally.

## 9. Comparing against a simple baseline

Today's idea — **Comparing against a simple baseline** — sits inside the theme of Debugging neural networks. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Comparing against a simple baseline
print("practice: Comparing against a simple baseline")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Comparing against a simple baseline` makes about your data before you use it.

**Common mistake:** Copy-pasting `Comparing against a simple baseline` from a tutorial without knowing what it assumes or when it fails.

## 10. A deep learning debugging checklist

Debug in a fixed order, cheapest test first. Can the model overfit 20 rows to zero loss? If not, the bug is in the data or the wiring, not the capacity. Is the loss at step zero what random guessing predicts? If not, the labels or the output layer are wrong.

```python
import numpy as np

def sanity_report(X, y, n_classes):
    print('shapes        ', X.shape, y.shape)
    print('nan in X      ', bool(np.isnan(X).any()))
    const = [i for i in range(X.shape[1]) if np.std(X[:, i]) == 0]
    print('constant cols ', const)
    counts = np.bincount(y, minlength=n_classes)
    print('class counts  ', counts)
    print('expected loss at init ~', round(float(np.log(n_classes)), 4))

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 5)); X[:, 2] = 1.0     # planted constant column
sanity_report(X, rng.integers(0, 3, 200), 3)
```

**Remember:** Expected cross-entropy at initialisation is ln(n_classes). A different value means a wiring bug.

**Common mistake:** Tuning hyperparameters for two days on a pipeline whose labels were misaligned by one row.

---

## What you should be able to do after Day 87

- Explain **Overfit a single batch first** to someone else without notes.
- Explain **Check loss at initialisation** to someone else without notes.
- Explain **Verify the data reaching the model** to someone else without notes.
- Explain **Shape errors and how to read them** to someone else without notes.
- Explain **NaN loss: causes and fixes** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
