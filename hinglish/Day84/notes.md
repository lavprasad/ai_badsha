# Day 84 — PyTorch fundamentals

Aaj ka goal: **PyTorch fundamentals** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

NumPy numbers ko ek continuous typed block me rakhta hai aur loops C me chalata hai. Vectorised code (poore array par operation) aksar Python loop se 50-100x tez hota hai aur maths jaisa padhta hai. Broadcasting chhoti shapes ko bina copy kiye stretch kar deta hai.

### Chhota code

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
print(a.shape, a.dtype)

b = np.array([10, 20, 30])       # shape (3,)
print(a + b)                     # broadcast over rows

print(a.sum(axis=0))             # column sums
print(a.sum(axis=1))             # row sums
```

**Yaad rakho:** `axis=0` rows ko collapse karta hai (columns ke neeche); `axis=1` columns ko (ek row ke aar-paar).

**Aam galti:** Python loop me array elements ghumana, vectorised operation use karne ke bajaye.

Practice: `examples/01_tensors_and_dtypes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Tensor operations mirror NumPy

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

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

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/02_tensor_operations_mirror_numpy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. CPU and GPU devices

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

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

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/03_cpu_and_gpu_devices.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. requires_grad and autograd

### Aasaan Bhasha

Backpropagation computation graph me ulta chain rule hai, jo intermediate results dobara use karta hai isliye cost lagbhag ek extra forward pass jitna hi hai. Har framework ye aapke liye karta hai — par ek baar haath se likhna hi failure modes ko padhne layak banata hai.

### Chhota code

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

**Yaad rakho:** Haath se likhe backward pass ko bharosa karne se pehle numeric estimate se gradient-check karo.

**Aam galti:** Steps ke beech gradients zero karna bhool jaana, jisse wo jud kar model ko diverge kar dete hain.

Practice: `examples/04_requires_grad_and_autograd.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. backward() and .grad

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

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

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/05_backward_and_grad.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Detaching from the graph

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

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

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/06_detaching_from_the_graph.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. nn.Module and parameters

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

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

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/07_nn_module_and_parameters.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. nn.Sequential

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

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

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/08_nn_sequential.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. The canonical training loop

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

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

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/09_the_canonical_training_loop.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Common PyTorch error messages

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

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

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/10_common_pytorch_error_messages.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 84 ke baad aapko ye aana chahiye

- **Tensors and dtypes** ko bina notes dekhe kisi dost ko samjha sakna.
- **Tensor operations mirror NumPy** ko bina notes dekhe kisi dost ko samjha sakna.
- **CPU and GPU devices** ko bina notes dekhe kisi dost ko samjha sakna.
- **requires_grad and autograd** ko bina notes dekhe kisi dost ko samjha sakna.
- **backward() and .grad** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
