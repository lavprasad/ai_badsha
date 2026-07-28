# Day 77 — Activation functions

Aaj ka goal: **Activation functions** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

ReLU default hai: sasta, aur positive inputs par saturate nahi hota. Sigmoid aur tanh fixed range me dabate hain aur extremes par gradients maar dete hain. GELU/SiLU smooth ReLU hain jo transformers me use hote hain. Softmax scores ke vector ko probability distribution bana deta hai.

### Chhota code

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

**Yaad rakho:** Softmax me `exp` se pehle hamesha max ghatao, warna bade logits inf/NaN me overflow kar jaate hain.

**Aam galti:** Aakhri layer par softmax lagana AUR aisa loss use karna jo andar khud softmax lagata hai.

Practice: `examples/01_why_non_linearity_is_mandatory.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Sigmoid and saturation

### Aasaan Bhasha

Logistic regression linear score ko sigmoid se dabaa kar probability banata hai. Coefficients log-odds hain: +0.7 matlab odds lagbhag double. Jahan decision regulator ko samjhana pade, wahan aaj bhi yahi default hai.

### Chhota code

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

**Yaad rakho:** Sigmoid ka input clip karo — bade negative number ka `exp` overflow hokar NaN de deta hai.

**Aam galti:** Raw output ko calibrated probability maan lena bina kabhi calibration curve dekhe.

Practice: `examples/02_sigmoid_and_saturation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Tanh

### Aasaan Bhasha

ReLU default hai: sasta, aur positive inputs par saturate nahi hota. Sigmoid aur tanh fixed range me dabate hain aur extremes par gradients maar dete hain. GELU/SiLU smooth ReLU hain jo transformers me use hote hain. Softmax scores ke vector ko probability distribution bana deta hai.

### Chhota code

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

**Yaad rakho:** Softmax me `exp` se pehle hamesha max ghatao, warna bade logits inf/NaN me overflow kar jaate hain.

**Aam galti:** Aakhri layer par softmax lagana AUR aisa loss use karna jo andar khud softmax lagata hai.

Practice: `examples/03_tanh.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. ReLU and dying neurons

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

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

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/04_relu_and_dying_neurons.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Leaky ReLU and PReLU

### Aasaan Bhasha

ReLU default hai: sasta, aur positive inputs par saturate nahi hota. Sigmoid aur tanh fixed range me dabate hain aur extremes par gradients maar dete hain. GELU/SiLU smooth ReLU hain jo transformers me use hote hain. Softmax scores ke vector ko probability distribution bana deta hai.

### Chhota code

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

**Yaad rakho:** Softmax me `exp` se pehle hamesha max ghatao, warna bade logits inf/NaN me overflow kar jaate hain.

**Aam galti:** Aakhri layer par softmax lagana AUR aisa loss use karna jo andar khud softmax lagata hai.

Practice: `examples/05_leaky_relu_and_prelu.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. GELU and SiLU/Swish

### Aasaan Bhasha

ReLU default hai: sasta, aur positive inputs par saturate nahi hota. Sigmoid aur tanh fixed range me dabate hain aur extremes par gradients maar dete hain. GELU/SiLU smooth ReLU hain jo transformers me use hote hain. Softmax scores ke vector ko probability distribution bana deta hai.

### Chhota code

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

**Yaad rakho:** Softmax me `exp` se pehle hamesha max ghatao, warna bade logits inf/NaN me overflow kar jaate hain.

**Aam galti:** Aakhri layer par softmax lagana AUR aisa loss use karna jo andar khud softmax lagata hai.

Practice: `examples/06_gelu_and_silu_swish.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Softmax for output distributions

### Aasaan Bhasha

Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Yaad rakho:** Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).

**Aam galti:** Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.

Practice: `examples/07_softmax_for_output_distributions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Numerical stability of softmax

### Aasaan Bhasha

ReLU default hai: sasta, aur positive inputs par saturate nahi hota. Sigmoid aur tanh fixed range me dabate hain aur extremes par gradients maar dete hain. GELU/SiLU smooth ReLU hain jo transformers me use hote hain. Softmax scores ke vector ko probability distribution bana deta hai.

### Chhota code

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

**Yaad rakho:** Softmax me `exp` se pehle hamesha max ghatao, warna bade logits inf/NaN me overflow kar jaate hain.

**Aam galti:** Aakhri layer par softmax lagana AUR aisa loss use karna jo andar khud softmax lagata hai.

Practice: `examples/08_numerical_stability_of_softmax.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Choosing activations per layer

### Aasaan Bhasha

ReLU default hai: sasta, aur positive inputs par saturate nahi hota. Sigmoid aur tanh fixed range me dabate hain aur extremes par gradients maar dete hain. GELU/SiLU smooth ReLU hain jo transformers me use hote hain. Softmax scores ke vector ko probability distribution bana deta hai.

### Chhota code

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

**Yaad rakho:** Softmax me `exp` se pehle hamesha max ghatao, warna bade logits inf/NaN me overflow kar jaate hain.

**Aam galti:** Aakhri layer par softmax lagana AUR aisa loss use karna jo andar khud softmax lagata hai.

Practice: `examples/09_choosing_activations_per_layer.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Plotting them all and their gradients

### Aasaan Bhasha

Model se pehle plot karo. Histogram skew aur outliers dikhata hai, scatter non-linearity, aur residuals ka plot batata hai ki model systematically galat kahan hai. Paanch minute ka plotting ghanton ki confused tuning bacha deta hai.

### Chhota code

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

**Yaad rakho:** Axes par label lagao. Bina label ka plot sajावat hai, evidence nahi.

**Aam galti:** Sirf accuracy number dekh kar model judge karna, data ko kabhi dekhe bina.

Practice: `examples/10_plotting_them_all_and_their_gradients.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 77 ke baad aapko ye aana chahiye

- **Why non-linearity is mandatory** ko bina notes dekhe kisi dost ko samjha sakna.
- **Sigmoid and saturation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Tanh** ko bina notes dekhe kisi dost ko samjha sakna.
- **ReLU and dying neurons** ko bina notes dekhe kisi dost ko samjha sakna.
- **Leaky ReLU and PReLU** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
