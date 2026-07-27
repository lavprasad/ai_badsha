# Day 29 — Numerical computing pitfalls

Today's goal: work through **numerical computing pitfalls** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Floating point representation |
| 2 | Catastrophic cancellation |
| 3 | Overflow and underflow |
| 4 | The log-sum-exp trick |
| 5 | Epsilon in denominators |
| 6 | NaN propagation and how to find the source |
| 7 | Deterministic seeds vs true randomness |
| 8 | Reproducibility across hardware |
| 9 | Numerical gradient checking |
| 10 | Debugging a silently wrong computation |

---

## 1. Floating point representation

Floats are approximations. Subtracting two nearly equal numbers destroys precision; exponentiating large numbers overflows to inf; dividing by a tiny number explodes. The log-sum-exp trick and a small epsilon in denominators are the two fixes you will use constantly.

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Remember:** Compare floats with a tolerance (`np.isclose`), never with `==`.

**Common mistake:** Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

## 2. Catastrophic cancellation

Floats are approximations. Subtracting two nearly equal numbers destroys precision; exponentiating large numbers overflows to inf; dividing by a tiny number explodes. The log-sum-exp trick and a small epsilon in denominators are the two fixes you will use constantly.

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Remember:** Compare floats with a tolerance (`np.isclose`), never with `==`.

**Common mistake:** Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

## 3. Overflow and underflow

Floats are approximations. Subtracting two nearly equal numbers destroys precision; exponentiating large numbers overflows to inf; dividing by a tiny number explodes. The log-sum-exp trick and a small epsilon in denominators are the two fixes you will use constantly.

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Remember:** Compare floats with a tolerance (`np.isclose`), never with `==`.

**Common mistake:** Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

## 4. The log-sum-exp trick

Floats are approximations. Subtracting two nearly equal numbers destroys precision; exponentiating large numbers overflows to inf; dividing by a tiny number explodes. The log-sum-exp trick and a small epsilon in denominators are the two fixes you will use constantly.

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Remember:** Compare floats with a tolerance (`np.isclose`), never with `==`.

**Common mistake:** Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

## 5. Epsilon in denominators

Floats are approximations. Subtracting two nearly equal numbers destroys precision; exponentiating large numbers overflows to inf; dividing by a tiny number explodes. The log-sum-exp trick and a small epsilon in denominators are the two fixes you will use constantly.

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Remember:** Compare floats with a tolerance (`np.isclose`), never with `==`.

**Common mistake:** Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

## 6. NaN propagation and how to find the source

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

## 7. Deterministic seeds vs true randomness

Floats are approximations. Subtracting two nearly equal numbers destroys precision; exponentiating large numbers overflows to inf; dividing by a tiny number explodes. The log-sum-exp trick and a small epsilon in denominators are the two fixes you will use constantly.

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Remember:** Compare floats with a tolerance (`np.isclose`), never with `==`.

**Common mistake:** Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

## 8. Reproducibility across hardware

An experiment you cannot reproduce is an anecdote. Track for every run: code commit, data version, hyperparameters, metrics and the artefact. Six months later, 'which run produced the model in production' must have an answer.

```python
import json, hashlib, subprocess

def run_record(params, metrics, data_path=None):
    try:
        commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], text=True).strip()
    except Exception:
        commit = 'unknown'
    return {
        'commit': commit,
        'params': params,
        'metrics': metrics,
        'data_sha': hashlib.sha256((data_path or 'none').encode()).hexdigest()[:12],
    }

print(json.dumps(run_record({'lr': 0.01, 'depth': 6}, {'auc': 0.912}, 'data/train.csv'), indent=2))
```

**Remember:** Log the data version alongside the code version — data changes silently, code changes loudly.

**Common mistake:** Naming files `model_final_v2_REAL_use_this.pkl` instead of using a registry.

## 9. Numerical gradient checking

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

## 10. Debugging a silently wrong computation

Floats are approximations. Subtracting two nearly equal numbers destroys precision; exponentiating large numbers overflows to inf; dividing by a tiny number explodes. The log-sum-exp trick and a small epsilon in denominators are the two fixes you will use constantly.

```python
import numpy as np

print(0.1 + 0.2 == 0.3, 0.1 + 0.2)          # False — welcome to floats

def logsumexp(x):
    m = np.max(x)
    return m + np.log(np.sum(np.exp(x - m)))   # never exp() a big number directly

big = np.array([1000.0, 1001.0, 1002.0])
print('naive :', np.log(np.sum(np.exp(big))))  # inf
print('stable:', logsumexp(big))

def safe_ratio(a, b, eps=1e-12):
    return a / (b + eps)
print(safe_ratio(1.0, 0.0))
```

**Remember:** Compare floats with a tolerance (`np.isclose`), never with `==`.

**Common mistake:** Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

---

## What you should be able to do after Day 29

- Explain **Floating point representation** to someone else without notes.
- Explain **Catastrophic cancellation** to someone else without notes.
- Explain **Overflow and underflow** to someone else without notes.
- Explain **The log-sum-exp trick** to someone else without notes.
- Explain **Epsilon in denominators** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
