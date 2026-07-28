# Day 86 — Training loop engineering

Aaj ka goal: **Training loop engineering** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_train_and_validation_phases.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. model.train() vs model.eval()

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

Practice: `examples/02_model_train_vs_model_eval.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. torch.no_grad() for inference

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

Practice: `examples/03_torch_no_grad_for_inference.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Tracking metrics per epoch

### Aasaan Bhasha

Gradient descent baar-baar gradient ke ulte kadam rakhta hai. Full-batch stable par dheema; stochastic shor wala par chhote gaddhon se nikal jaata hai; mini-batch practical beech ka raasta hai. Learning rate wo ek knob hai jise aap sabse zyada ghumaoge.

### Chhota code

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

**Yaad rakho:** Har epoch shuffle karo, warna model aapki file ka order seekh lega.

**Aam galti:** Learning rate ko hamesha fix rakhna, loss plateau hone par use decay na karna.

Practice: `examples/04_tracking_metrics_per_epoch.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Checkpointing and resuming

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

Practice: `examples/05_checkpointing_and_resuming.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Saving the best model by validation score

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

Practice: `examples/06_saving_the_best_model_by_validation_scor.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Gradient clipping

### Aasaan Bhasha

Derivative batata hai: input ko thoda hilaun to output kitna hilega? Gradient ye jawab ek saath har input ke liye deta hai, isliye wo chadhaai ki taraf point karta hai. Training gradient ke ulte chal kar neeche utarti hai. Chain rule hi wo cheez hai jo ye jawab layers ke poore stack me pahuchata hai.

### Chhota code

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

**Yaad rakho:** Central difference `(f(x+h)-f(x-h))/2h` haath se likhe gradient ko check karne ka sabse sasta tarika hai.

**Aam galti:** Aise derivation par bharosa karna jise aapne kabhi gradient-check nahi kiya; sign ki galti train dheere karti hai, saaf fail nahi hoti.

Practice: `examples/07_gradient_clipping.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Gradient accumulation

### Aasaan Bhasha

Derivative batata hai: input ko thoda hilaun to output kitna hilega? Gradient ye jawab ek saath har input ke liye deta hai, isliye wo chadhaai ki taraf point karta hai. Training gradient ke ulte chal kar neeche utarti hai. Chain rule hi wo cheez hai jo ye jawab layers ke poore stack me pahuchata hai.

### Chhota code

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

**Yaad rakho:** Central difference `(f(x+h)-f(x-h))/2h` haath se likhe gradient ko check karne ka sabse sasta tarika hai.

**Aam galti:** Aise derivation par bharosa karna jise aapne kabhi gradient-check nahi kiya; sign ki galti train dheere karti hai, saaf fail nahi hoti.

Practice: `examples/08_gradient_accumulation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Mixed precision training

### Aasaan Bhasha

Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.

### Chhota code

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

**Yaad rakho:** Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.

**Aam galti:** Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.

Practice: `examples/09_mixed_precision_training.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A reusable Trainer you actually own

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

Practice: `examples/10_a_reusable_trainer_you_actually_own.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 86 ke baad aapko ye aana chahiye

- **Train and validation phases** ko bina notes dekhe kisi dost ko samjha sakna.
- **model.train() vs model.eval()** ko bina notes dekhe kisi dost ko samjha sakna.
- **torch.no_grad() for inference** ko bina notes dekhe kisi dost ko samjha sakna.
- **Tracking metrics per epoch** ko bina notes dekhe kisi dost ko samjha sakna.
- **Checkpointing and resuming** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
