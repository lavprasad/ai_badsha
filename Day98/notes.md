# Day 98 — Graph neural networks

Today's goal: work through **graph neural networks** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Data that is naturally a graph |
| 2 | Adjacency and node features |
| 3 | Message passing |
| 4 | Graph convolution |
| 5 | GraphSAGE and sampling |
| 6 | Graph attention networks |
| 7 | Node, edge and graph-level tasks |
| 8 | Over-smoothing |
| 9 | Splitting graph data without leakage |
| 10 | Fraud rings as a GNN problem |

---

## 1. Data that is naturally a graph

A GNN passes messages along edges: each node updates itself from its neighbours, repeated k times so information travels k hops. Good for fraud rings, molecules and social graphs — anywhere the relationships carry more signal than the nodes.

```python
import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))
```

**Remember:** Too many message-passing layers causes over-smoothing — every node converges to the same vector.

**Common mistake:** Splitting graph data randomly so a node's own neighbours end up in both train and test.

## 2. Adjacency and node features

A GNN passes messages along edges: each node updates itself from its neighbours, repeated k times so information travels k hops. Good for fraud rings, molecules and social graphs — anywhere the relationships carry more signal than the nodes.

```python
import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))
```

**Remember:** Too many message-passing layers causes over-smoothing — every node converges to the same vector.

**Common mistake:** Splitting graph data randomly so a node's own neighbours end up in both train and test.

## 3. Message passing

A GNN passes messages along edges: each node updates itself from its neighbours, repeated k times so information travels k hops. Good for fraud rings, molecules and social graphs — anywhere the relationships carry more signal than the nodes.

```python
import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))
```

**Remember:** Too many message-passing layers causes over-smoothing — every node converges to the same vector.

**Common mistake:** Splitting graph data randomly so a node's own neighbours end up in both train and test.

## 4. Graph convolution

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

## 5. GraphSAGE and sampling

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

## 6. Graph attention networks

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

## 7. Node, edge and graph-level tasks

A GNN passes messages along edges: each node updates itself from its neighbours, repeated k times so information travels k hops. Good for fraud rings, molecules and social graphs — anywhere the relationships carry more signal than the nodes.

```python
import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))
```

**Remember:** Too many message-passing layers causes over-smoothing — every node converges to the same vector.

**Common mistake:** Splitting graph data randomly so a node's own neighbours end up in both train and test.

## 8. Over-smoothing

A GNN passes messages along edges: each node updates itself from its neighbours, repeated k times so information travels k hops. Good for fraud rings, molecules and social graphs — anywhere the relationships carry more signal than the nodes.

```python
import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))
```

**Remember:** Too many message-passing layers causes over-smoothing — every node converges to the same vector.

**Common mistake:** Splitting graph data randomly so a node's own neighbours end up in both train and test.

## 9. Splitting graph data without leakage

Leakage is information in training that will not exist at prediction time. It produces impossible validation scores and a model that collapses in production. If your accuracy jumps suspiciously, hunt for a leak before you celebrate.

```python
# Three classic leaks, all silent:
# 1. Scaling/imputing before the train/test split
# 2. A column filled in only after the outcome ('refund_amount' when predicting refunds)
# 3. Random split on time-series so the model sees the future

import pandas as pd
df = pd.DataFrame({'ts': pd.date_range('2024-01-01', periods=100, freq='D')})
cut = int(len(df) * 0.8)
train, test = df.iloc[:cut], df.iloc[cut:]     # time-ordered split, no look-ahead
print(train['ts'].max(), '<', test['ts'].min())
```

**Remember:** 0.999 AUC on a hard business problem is a bug report, not a result.

**Common mistake:** Shipping a leaked model and discovering the real accuracy from angry users.

## 10. Fraud rings as a GNN problem

A GNN passes messages along edges: each node updates itself from its neighbours, repeated k times so information travels k hops. Good for fraud rings, molecules and social graphs — anywhere the relationships carry more signal than the nodes.

```python
import numpy as np

# One round of mean-aggregation message passing
A = np.array([[0, 1, 1, 0],
              [1, 0, 1, 0],
              [1, 1, 0, 1],
              [0, 0, 1, 0]], dtype=float)
H = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])

deg = A.sum(axis=1, keepdims=True)
H_next = np.tanh((A @ H) / np.maximum(deg, 1))
print(H_next.round(3))
```

**Remember:** Too many message-passing layers causes over-smoothing — every node converges to the same vector.

**Common mistake:** Splitting graph data randomly so a node's own neighbours end up in both train and test.

---

## What you should be able to do after Day 98

- Explain **Data that is naturally a graph** to someone else without notes.
- Explain **Adjacency and node features** to someone else without notes.
- Explain **Message passing** to someone else without notes.
- Explain **Graph convolution** to someone else without notes.
- Explain **GraphSAGE and sampling** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
