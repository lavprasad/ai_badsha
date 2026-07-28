# Day 80 — Optimisers

Aaj ka goal: **Optimisers** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_batch_stochastic_and_mini_batch_descent.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Learning rate: the master knob

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

Practice: `examples/02_learning_rate_the_master_knob.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Momentum

### Aasaan Bhasha

SGD with momentum dhalaan ka raasta smooth karta hai. Adam har parameter ka step size adapt karta hai aur safe default hai. AdamW weight decay ko adaptive step se alag kar deta hai, isiliye har modern transformer wahi use karta hai. Warmup phir cosine decay standard recipe hai.

### Chhota code

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

**Yaad rakho:** Scratch training ke liye Adam ka default lr 1e-3 accha start hai; fine-tuning ke liye 1e-5 se 5e-5.

**Aam galti:** Pretraining aur fine-tuning me ek hi learning rate use karke pretrained weights barbaad kar dena.

Practice: `examples/03_momentum.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Nesterov accelerated gradient

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

Practice: `examples/04_nesterov_accelerated_gradient.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. AdaGrad and RMSProp

### Aasaan Bhasha

SGD with momentum dhalaan ka raasta smooth karta hai. Adam har parameter ka step size adapt karta hai aur safe default hai. AdamW weight decay ko adaptive step se alag kar deta hai, isiliye har modern transformer wahi use karta hai. Warmup phir cosine decay standard recipe hai.

### Chhota code

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

**Yaad rakho:** Scratch training ke liye Adam ka default lr 1e-3 accha start hai; fine-tuning ke liye 1e-5 se 5e-5.

**Aam galti:** Pretraining aur fine-tuning me ek hi learning rate use karke pretrained weights barbaad kar dena.

Practice: `examples/05_adagrad_and_rmsprop.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Adam

### Aasaan Bhasha

SGD with momentum dhalaan ka raasta smooth karta hai. Adam har parameter ka step size adapt karta hai aur safe default hai. AdamW weight decay ko adaptive step se alag kar deta hai, isiliye har modern transformer wahi use karta hai. Warmup phir cosine decay standard recipe hai.

### Chhota code

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

**Yaad rakho:** Scratch training ke liye Adam ka default lr 1e-3 accha start hai; fine-tuning ke liye 1e-5 se 5e-5.

**Aam galti:** Pretraining aur fine-tuning me ek hi learning rate use karke pretrained weights barbaad kar dena.

Practice: `examples/06_adam.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. AdamW and decoupled weight decay

### Aasaan Bhasha

Regularisation bade weights par penalty lagata hai taaki model simple explanation pasand kare. L2 (ridge) sab kuch smoothly chhota karta hai; L1 (lasso) kuch weights ko bilkul zero kar deta hai aur isi tarah features chunta hai. Elastic net dono milata hai.

### Chhota code

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

**Yaad rakho:** Regularise karne se pehle features scale karo, warna penalty usi column ko sazaa deta hai jiski units chhoti hain.

**Aam galti:** Test set par `alpha` tune karna — use sirf train par cross-validation se chuno.

Practice: `examples/07_adamw_and_decoupled_weight_decay.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Choosing an optimiser in practice

### Aasaan Bhasha

SGD with momentum dhalaan ka raasta smooth karta hai. Adam har parameter ka step size adapt karta hai aur safe default hai. AdamW weight decay ko adaptive step se alag kar deta hai, isiliye har modern transformer wahi use karta hai. Warmup phir cosine decay standard recipe hai.

### Chhota code

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

**Yaad rakho:** Scratch training ke liye Adam ka default lr 1e-3 accha start hai; fine-tuning ke liye 1e-5 se 5e-5.

**Aam galti:** Pretraining aur fine-tuning me ek hi learning rate use karke pretrained weights barbaad kar dena.

Practice: `examples/08_choosing_an_optimiser_in_practice.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Optimiser state and memory cost

### Aasaan Bhasha

SGD with momentum dhalaan ka raasta smooth karta hai. Adam har parameter ka step size adapt karta hai aur safe default hai. AdamW weight decay ko adaptive step se alag kar deta hai, isiliye har modern transformer wahi use karta hai. Warmup phir cosine decay standard recipe hai.

### Chhota code

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

**Yaad rakho:** Scratch training ke liye Adam ka default lr 1e-3 accha start hai; fine-tuning ke liye 1e-5 se 5e-5.

**Aam galti:** Pretraining aur fine-tuning me ek hi learning rate use karke pretrained weights barbaad kar dena.

Practice: `examples/09_optimiser_state_and_memory_cost.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Implementing Adam from scratch

### Aasaan Bhasha

SGD with momentum dhalaan ka raasta smooth karta hai. Adam har parameter ka step size adapt karta hai aur safe default hai. AdamW weight decay ko adaptive step se alag kar deta hai, isiliye har modern transformer wahi use karta hai. Warmup phir cosine decay standard recipe hai.

### Chhota code

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

**Yaad rakho:** Scratch training ke liye Adam ka default lr 1e-3 accha start hai; fine-tuning ke liye 1e-5 se 5e-5.

**Aam galti:** Pretraining aur fine-tuning me ek hi learning rate use karke pretrained weights barbaad kar dena.

Practice: `examples/10_implementing_adam_from_scratch.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 80 ke baad aapko ye aana chahiye

- **Batch, stochastic and mini-batch descent** ko bina notes dekhe kisi dost ko samjha sakna.
- **Learning rate: the master knob** ko bina notes dekhe kisi dost ko samjha sakna.
- **Momentum** ko bina notes dekhe kisi dost ko samjha sakna.
- **Nesterov accelerated gradient** ko bina notes dekhe kisi dost ko samjha sakna.
- **AdaGrad and RMSProp** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
