# Day 126 — Attention deep dive

Today's goal: work through **attention deep dive** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Query, key, value projections |
| 2 | Scaled dot-product attention |
| 3 | Causal and padding masks |
| 4 | Cross-attention in encoder-decoder |
| 5 | Attention complexity in sequence length |
| 6 | Flash attention and memory-efficient kernels |
| 7 | Sliding window and sparse attention |
| 8 | Grouped-query and multi-query attention |
| 9 | KV cache during generation |
| 10 | Implementing multi-head attention |

---

## 1. Query, key, value projections

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

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

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 2. Scaled dot-product attention

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

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

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 3. Causal and padding masks

A convolution slides a small learned filter over the image, so the same edge detector works anywhere in the frame. That weight sharing is why a CNN needs far fewer parameters than a dense net. Pooling shrinks the map and adds a little translation tolerance.

```python
import numpy as np

image = np.array([
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
], dtype=float)
kernel = np.array([[-1, 1], [-1, 1]], dtype=float)   # vertical edge detector

h, w = image.shape[0] - 1, image.shape[1] - 1
out = np.zeros((h, w))
for i in range(h):
    for j in range(w):
        out[i, j] = float((image[i:i + 2, j:j + 2] * kernel).sum())
print(out)   # the edge column lights up
```

**Remember:** Output size = (in - kernel + 2*pad)/stride + 1. Print shapes when a layer refuses to connect.

**Common mistake:** Forgetting the channel dimension and feeding (H,W) where the layer expects (N,C,H,W).

## 4. Cross-attention in encoder-decoder

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

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

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 5. Attention complexity in sequence length

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

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

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 6. Flash attention and memory-efficient kernels

Notebooks keep state between cells, which is great for exploring and terrible for reproducibility. Treat the notebook as a scratchpad; once logic settles, move it into a `.py` module you can import and test.

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Remember:** 'Restart kernel and run all' is the only honest test that a notebook works.

**Common mistake:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

## 7. Sliding window and sparse attention

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

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

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 8. Grouped-query and multi-query attention

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

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

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 9. KV cache during generation

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

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

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 10. Implementing multi-head attention

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

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

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

---

## What you should be able to do after Day 126

- Explain **Query, key, value projections** to someone else without notes.
- Explain **Scaled dot-product attention** to someone else without notes.
- Explain **Causal and padding masks** to someone else without notes.
- Explain **Cross-attention in encoder-decoder** to someone else without notes.
- Explain **Attention complexity in sequence length** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
