# Day 86 — Training loop engineering

Today's goal: work through **Training loop engineering** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Train and validation phases |
| 2 | model.train() vs model.eval() |
| 3 | torch.no_grad() for inference |
| 4 | Tracking metrics per epoch |
| 5 | Checkpointing and resuming |
| 6 | Saving the best model by validation score |
| 7 | Gradient clipping |
| 8 | Gradient accumulation |
| 9 | Mixed precision training |
| 10 | A reusable Trainer you actually own |

---

## 1. Train and validation phases

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Practice: open `examples/01_train_and_validation_phases.py`, predict the output, change one line, predict again.

## 2. model.train() vs model.eval()

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Practice: open `examples/02_model_train_vs_model_eval.py`, predict the output, change one line, predict again.

## 3. torch.no_grad() for inference

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Practice: open `examples/03_torch_no_grad_for_inference.py`, predict the output, change one line, predict again.

## 4. Tracking metrics per epoch

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

Practice: open `examples/04_tracking_metrics_per_epoch.py`, predict the output, change one line, predict again.

## 5. Checkpointing and resuming

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Practice: open `examples/05_checkpointing_and_resuming.py`, predict the output, change one line, predict again.

## 6. Saving the best model by validation score

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Practice: open `examples/06_saving_the_best_model_by_validation_scor.py`, predict the output, change one line, predict again.

## 7. Gradient clipping

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

Practice: open `examples/07_gradient_clipping.py`, predict the output, change one line, predict again.

## 8. Gradient accumulation

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

Practice: open `examples/08_gradient_accumulation.py`, predict the output, change one line, predict again.

## 9. Mixed precision training

Accuracy hides everything on imbalanced data. Precision asks 'of the ones I flagged, how many were real'; recall asks 'of the real ones, how many did I catch'. You trade one for the other with the threshold, and the business decides which error hurts more.

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Remember:** Tune the decision threshold on validation data; 0.5 is a default, not a decision.

**Common mistake:** Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

Practice: open `examples/09_mixed_precision_training.py`, predict the output, change one line, predict again.

## 10. A reusable Trainer you actually own

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Practice: open `examples/10_a_reusable_trainer_you_actually_own.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 86

- Explain **Train and validation phases** to someone else without notes.
- Explain **model.train() vs model.eval()** to someone else without notes.
- Explain **torch.no_grad() for inference** to someone else without notes.
- Explain **Tracking metrics per epoch** to someone else without notes.
- Explain **Checkpointing and resuming** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
