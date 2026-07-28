# Day 80 — Optimisers

Today's goal: work through **Optimisers** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Batch, stochastic and mini-batch descent |
| 2 | Learning rate: the master knob |
| 3 | Momentum |
| 4 | Nesterov accelerated gradient |
| 5 | AdaGrad and RMSProp |
| 6 | Adam |
| 7 | AdamW and decoupled weight decay |
| 8 | Choosing an optimiser in practice |
| 9 | Optimiser state and memory cost |
| 10 | Implementing Adam from scratch |

---

## 1. Batch, stochastic and mini-batch descent

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

Practice: open `examples/01_batch_stochastic_and_mini_batch_descent.py`, predict the output, change one line, predict again.

## 2. Learning rate: the master knob

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

Practice: open `examples/02_learning_rate_the_master_knob.py`, predict the output, change one line, predict again.

## 3. Momentum

SGD with momentum smooths the path downhill. Adam adapts a per-parameter step size and is the safe default. AdamW decouples weight decay from the adaptive step, which is why every modern transformer uses it. A warmup then cosine decay schedule is the standard recipe.

```python
import numpy as np

# Adam on a 1-D bowl, from scratch
w, m, v = 5.0, 0.0, 0.0
lr, b1, b2, eps = 0.1, 0.9, 0.999, 1e-8
for t in range(1, 101):
    g = 2 * (w - 3)                       # gradient of (w-3)^2
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    mhat = m / (1 - b1 ** t)
    vhat = v / (1 - b2 ** t)
    w -= lr * mhat / (np.sqrt(vhat) + eps)
print(f'w = {w:.4f} (target 3.0)')
```

**Remember:** Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

**Common mistake:** Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.

Practice: open `examples/03_momentum.py`, predict the output, change one line, predict again.

## 4. Nesterov accelerated gradient

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

Practice: open `examples/04_nesterov_accelerated_gradient.py`, predict the output, change one line, predict again.

## 5. AdaGrad and RMSProp

SGD with momentum smooths the path downhill. Adam adapts a per-parameter step size and is the safe default. AdamW decouples weight decay from the adaptive step, which is why every modern transformer uses it. A warmup then cosine decay schedule is the standard recipe.

```python
import numpy as np

# Adam on a 1-D bowl, from scratch
w, m, v = 5.0, 0.0, 0.0
lr, b1, b2, eps = 0.1, 0.9, 0.999, 1e-8
for t in range(1, 101):
    g = 2 * (w - 3)                       # gradient of (w-3)^2
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    mhat = m / (1 - b1 ** t)
    vhat = v / (1 - b2 ** t)
    w -= lr * mhat / (np.sqrt(vhat) + eps)
print(f'w = {w:.4f} (target 3.0)')
```

**Remember:** Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

**Common mistake:** Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.

Practice: open `examples/05_adagrad_and_rmsprop.py`, predict the output, change one line, predict again.

## 6. Adam

SGD with momentum smooths the path downhill. Adam adapts a per-parameter step size and is the safe default. AdamW decouples weight decay from the adaptive step, which is why every modern transformer uses it. A warmup then cosine decay schedule is the standard recipe.

```python
import numpy as np

# Adam on a 1-D bowl, from scratch
w, m, v = 5.0, 0.0, 0.0
lr, b1, b2, eps = 0.1, 0.9, 0.999, 1e-8
for t in range(1, 101):
    g = 2 * (w - 3)                       # gradient of (w-3)^2
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    mhat = m / (1 - b1 ** t)
    vhat = v / (1 - b2 ** t)
    w -= lr * mhat / (np.sqrt(vhat) + eps)
print(f'w = {w:.4f} (target 3.0)')
```

**Remember:** Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

**Common mistake:** Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.

Practice: open `examples/06_adam.py`, predict the output, change one line, predict again.

## 7. AdamW and decoupled weight decay

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

Practice: open `examples/07_adamw_and_decoupled_weight_decay.py`, predict the output, change one line, predict again.

## 8. Choosing an optimiser in practice

SGD with momentum smooths the path downhill. Adam adapts a per-parameter step size and is the safe default. AdamW decouples weight decay from the adaptive step, which is why every modern transformer uses it. A warmup then cosine decay schedule is the standard recipe.

```python
import numpy as np

# Adam on a 1-D bowl, from scratch
w, m, v = 5.0, 0.0, 0.0
lr, b1, b2, eps = 0.1, 0.9, 0.999, 1e-8
for t in range(1, 101):
    g = 2 * (w - 3)                       # gradient of (w-3)^2
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    mhat = m / (1 - b1 ** t)
    vhat = v / (1 - b2 ** t)
    w -= lr * mhat / (np.sqrt(vhat) + eps)
print(f'w = {w:.4f} (target 3.0)')
```

**Remember:** Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

**Common mistake:** Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.

Practice: open `examples/08_choosing_an_optimiser_in_practice.py`, predict the output, change one line, predict again.

## 9. Optimiser state and memory cost

SGD with momentum smooths the path downhill. Adam adapts a per-parameter step size and is the safe default. AdamW decouples weight decay from the adaptive step, which is why every modern transformer uses it. A warmup then cosine decay schedule is the standard recipe.

```python
import numpy as np

# Adam on a 1-D bowl, from scratch
w, m, v = 5.0, 0.0, 0.0
lr, b1, b2, eps = 0.1, 0.9, 0.999, 1e-8
for t in range(1, 101):
    g = 2 * (w - 3)                       # gradient of (w-3)^2
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    mhat = m / (1 - b1 ** t)
    vhat = v / (1 - b2 ** t)
    w -= lr * mhat / (np.sqrt(vhat) + eps)
print(f'w = {w:.4f} (target 3.0)')
```

**Remember:** Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

**Common mistake:** Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.

Practice: open `examples/09_optimiser_state_and_memory_cost.py`, predict the output, change one line, predict again.

## 10. Implementing Adam from scratch

SGD with momentum smooths the path downhill. Adam adapts a per-parameter step size and is the safe default. AdamW decouples weight decay from the adaptive step, which is why every modern transformer uses it. A warmup then cosine decay schedule is the standard recipe.

```python
import numpy as np

# Adam on a 1-D bowl, from scratch
w, m, v = 5.0, 0.0, 0.0
lr, b1, b2, eps = 0.1, 0.9, 0.999, 1e-8
for t in range(1, 101):
    g = 2 * (w - 3)                       # gradient of (w-3)^2
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * g ** 2
    mhat = m / (1 - b1 ** t)
    vhat = v / (1 - b2 ** t)
    w -= lr * mhat / (np.sqrt(vhat) + eps)
print(f'w = {w:.4f} (target 3.0)')
```

**Remember:** Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

**Common mistake:** Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.

Practice: open `examples/10_implementing_adam_from_scratch.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 80

- Explain **Batch, stochastic and mini-batch descent** to someone else without notes.
- Explain **Learning rate: the master knob** to someone else without notes.
- Explain **Momentum** to someone else without notes.
- Explain **Nesterov accelerated gradient** to someone else without notes.
- Explain **AdaGrad and RMSProp** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
