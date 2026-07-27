# Day 77 — Activation functions

Today's goal: work through **activation functions** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why non-linearity is mandatory |
| 2 | Sigmoid and saturation |
| 3 | Tanh |
| 4 | ReLU and dying neurons |
| 5 | Leaky ReLU and PReLU |
| 6 | GELU and SiLU/Swish |
| 7 | Softmax for output distributions |
| 8 | Numerical stability of softmax |
| 9 | Choosing activations per layer |
| 10 | Plotting them all and their gradients |

---

## 1. Why non-linearity is mandatory

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

## 2. Sigmoid and saturation

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

## 3. Tanh

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

## 4. ReLU and dying neurons

A neuron computes `activation(w·x + b)`. Stack them in layers and you can approximate any continuous function. Without the non-linear activation, ten stacked layers collapse algebraically into one linear layer — the non-linearity is the whole point.

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Remember:** Depth without non-linearity is width. Check that every hidden layer has an activation.

**Common mistake:** Initialising all weights to zero, so every neuron gets the same gradient and learns the same thing.

## 5. Leaky ReLU and PReLU

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

## 6. GELU and SiLU/Swish

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

## 7. Softmax for output distributions

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

## 8. Numerical stability of softmax

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

## 9. Choosing activations per layer

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

## 10. Plotting them all and their gradients

Plot before you model. A histogram exposes skew and outliers, a scatter exposes non-linearity, and a line of residuals exposes a model that is systematically wrong. Five minutes of plotting saves hours of confused tuning.

```python
import matplotlib
matplotlib.use('Agg')          # headless-safe for scripts/CI
import matplotlib.pyplot as plt
import numpy as np

x = np.random.default_rng(0).normal(size=500)
fig, ax = plt.subplots()
ax.hist(x, bins=30)
ax.set_title('sample distribution')
fig.savefig('hist.png', dpi=120)
print('wrote hist.png')
```

**Remember:** Label the axes. An unlabelled plot is a decoration, not evidence.

**Common mistake:** Judging a model by its accuracy number alone without ever looking at the data.

---

## What you should be able to do after Day 77

- Explain **Why non-linearity is mandatory** to someone else without notes.
- Explain **Sigmoid and saturation** to someone else without notes.
- Explain **Tanh** to someone else without notes.
- Explain **ReLU and dying neurons** to someone else without notes.
- Explain **Leaky ReLU and PReLU** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
