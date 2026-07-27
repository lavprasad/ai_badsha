# Day 84 — PyTorch fundamentals

Today's goal: work through **pytorch fundamentals** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Tensors and dtypes |
| 2 | Tensor operations mirror NumPy |
| 3 | CPU and GPU devices |
| 4 | requires_grad and autograd |
| 5 | backward() and .grad |
| 6 | Detaching from the graph |
| 7 | nn.Module and parameters |
| 8 | nn.Sequential |
| 9 | The canonical training loop |
| 10 | Common PyTorch error messages |

---

## 1. Tensors and dtypes

NumPy stores numbers in one contiguous typed block and runs loops in C. Vectorised code (whole-array operations) is often 50-100x faster than a Python `for` loop and reads closer to the maths. Broadcasting stretches smaller shapes to match without copying data.

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
print(a.shape, a.dtype)

b = np.array([10, 20, 30])       # shape (3,)
print(a + b)                     # broadcast over rows

print(a.sum(axis=0))             # column sums
print(a.sum(axis=1))             # row sums
```

**Remember:** `axis=0` collapses rows (down the columns); `axis=1` collapses columns (across a row).

**Common mistake:** Looping over array elements in Python instead of using a vectorised operation.

## 2. Tensor operations mirror NumPy

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

## 3. CPU and GPU devices

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

## 4. requires_grad and autograd

Backpropagation is the chain rule applied backwards through the computation graph, reusing intermediate results so the cost is roughly one extra forward pass. Every framework does it for you — but writing it once by hand is what makes the failure modes readable.

```python
import numpy as np

# y = (w*x + b)^2 ; d y/d w by hand
x, w, b = 2.0, 3.0, 1.0
z = w * x + b        # forward
y = z ** 2

dy_dz = 2 * z        # backward
dz_dw = x
dz_db = 1.0
print('dy/dw', dy_dz * dz_dw)   # 28.0
print('dy/db', dy_dz * dz_db)   # 14.0

h = 1e-6
print('numeric dy/dw', (((w + h) * x + b) ** 2 - ((w - h) * x + b) ** 2) / (2 * h))
```

**Remember:** Gradient-check any hand-written backward pass against a numeric estimate before trusting it.

**Common mistake:** Forgetting to zero gradients between steps, so they accumulate and the model diverges.

## 5. backward() and .grad

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

## 6. Detaching from the graph

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

## 7. nn.Module and parameters

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

## 8. nn.Sequential

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

## 9. The canonical training loop

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

## 10. Common PyTorch error messages

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

---

## What you should be able to do after Day 84

- Explain **Tensors and dtypes** to someone else without notes.
- Explain **Tensor operations mirror NumPy** to someone else without notes.
- Explain **CPU and GPU devices** to someone else without notes.
- Explain **requires_grad and autograd** to someone else without notes.
- Explain **backward() and .grad** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
