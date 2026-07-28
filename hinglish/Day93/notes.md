# Day 93 — Attention mechanisms

Aaj ka goal: **Attention mechanisms** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | The bottleneck problem in seq2seq |
| 2 | Attention as weighted lookup |
| 3 | Query, key and value |
| 4 | Scaled dot-product attention |
| 5 | The scaling factor and why it matters |
| 6 | Attention masks |
| 7 | Self-attention vs cross-attention |
| 8 | Multi-head attention |
| 9 | Attention weight visualisation |
| 10 | Implementing attention in NumPy |

---

## 1. The bottleneck problem in seq2seq

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/01_the_bottleneck_problem_in_seq2seq.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Attention as weighted lookup

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/02_attention_as_weighted_lookup.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Query, key and value

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/03_query_key_and_value.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Scaled dot-product attention

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/04_scaled_dot_product_attention.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. The scaling factor and why it matters

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/05_the_scaling_factor_and_why_it_matters.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Attention masks

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/06_attention_masks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Self-attention vs cross-attention

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/07_self_attention_vs_cross_attention.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Multi-head attention

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/08_multi_head_attention.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Attention weight visualisation

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

Practice: `examples/09_attention_weight_visualisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Implementing attention in NumPy

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/10_implementing_attention_in_numpy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 93 ke baad aapko ye aana chahiye

- **The bottleneck problem in seq2seq** ko bina notes dekhe kisi dost ko samjha sakna.
- **Attention as weighted lookup** ko bina notes dekhe kisi dost ko samjha sakna.
- **Query, key and value** ko bina notes dekhe kisi dost ko samjha sakna.
- **Scaled dot-product attention** ko bina notes dekhe kisi dost ko samjha sakna.
- **The scaling factor and why it matters** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
