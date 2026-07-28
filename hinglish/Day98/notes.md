# Day 98 — Graph neural networks

Aaj ka goal: **Graph neural networks** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

GNN edges ke saath messages bhejta hai: har node apne padosiyon se khud ko update karta hai, k baar, taaki information k hops tak safar kare. Fraud rings, molecules aur social graphs ke liye badhiya — jahan bhi rishte nodes se zyada signal rakhte hain.

### Chhota code

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

**Yaad rakho:** Bahut zyada message-passing layers over-smoothing kar deti hain — har node ek jaisa vector ban jaata hai.

**Aam galti:** Graph data ko randomly split karna, jisse ek node ke apne padosi train aur test dono me aa jaate hain.

Practice: `examples/01_data_that_is_naturally_a_graph.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Adjacency and node features

### Aasaan Bhasha

GNN edges ke saath messages bhejta hai: har node apne padosiyon se khud ko update karta hai, k baar, taaki information k hops tak safar kare. Fraud rings, molecules aur social graphs ke liye badhiya — jahan bhi rishte nodes se zyada signal rakhte hain.

### Chhota code

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

**Yaad rakho:** Bahut zyada message-passing layers over-smoothing kar deti hain — har node ek jaisa vector ban jaata hai.

**Aam galti:** Graph data ko randomly split karna, jisse ek node ke apne padosi train aur test dono me aa jaate hain.

Practice: `examples/02_adjacency_and_node_features.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Message passing

### Aasaan Bhasha

GNN edges ke saath messages bhejta hai: har node apne padosiyon se khud ko update karta hai, k baar, taaki information k hops tak safar kare. Fraud rings, molecules aur social graphs ke liye badhiya — jahan bhi rishte nodes se zyada signal rakhte hain.

### Chhota code

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

**Yaad rakho:** Bahut zyada message-passing layers over-smoothing kar deti hain — har node ek jaisa vector ban jaata hai.

**Aam galti:** Graph data ko randomly split karna, jisse ek node ke apne padosi train aur test dono me aa jaate hain.

Practice: `examples/03_message_passing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Graph convolution

### Aasaan Bhasha

Convolution ek chhota seekha hua filter image par sarkata hai, isliye wahi edge detector frame me kahin bhi kaam karta hai. Yahi weight sharing wajah hai ki CNN ko dense net se kahin kam parameters chahiye. Pooling map chhota karta hai aur thodi translation tolerance deta hai.

### Chhota code

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

**Yaad rakho:** Output size = (in - kernel + 2*pad)/stride + 1. Jab layer jud na rahi ho to shapes print karo.

**Aam galti:** Channel dimension bhool jaana aur (H,W) dena jahan layer (N,C,H,W) maang rahi hai.

Practice: `examples/04_graph_convolution.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. GraphSAGE and sampling

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

Practice: `examples/05_graphsage_and_sampling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Graph attention networks

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

Practice: `examples/06_graph_attention_networks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Node, edge and graph-level tasks

### Aasaan Bhasha

GNN edges ke saath messages bhejta hai: har node apne padosiyon se khud ko update karta hai, k baar, taaki information k hops tak safar kare. Fraud rings, molecules aur social graphs ke liye badhiya — jahan bhi rishte nodes se zyada signal rakhte hain.

### Chhota code

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

**Yaad rakho:** Bahut zyada message-passing layers over-smoothing kar deti hain — har node ek jaisa vector ban jaata hai.

**Aam galti:** Graph data ko randomly split karna, jisse ek node ke apne padosi train aur test dono me aa jaate hain.

Practice: `examples/07_node_edge_and_graph_level_tasks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Over-smoothing

### Aasaan Bhasha

GNN edges ke saath messages bhejta hai: har node apne padosiyon se khud ko update karta hai, k baar, taaki information k hops tak safar kare. Fraud rings, molecules aur social graphs ke liye badhiya — jahan bhi rishte nodes se zyada signal rakhte hain.

### Chhota code

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

**Yaad rakho:** Bahut zyada message-passing layers over-smoothing kar deti hain — har node ek jaisa vector ban jaata hai.

**Aam galti:** Graph data ko randomly split karna, jisse ek node ke apne padosi train aur test dono me aa jaate hain.

Practice: `examples/08_over_smoothing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Splitting graph data without leakage

### Aasaan Bhasha

Leakage matlab training me aisi information jo prediction ke waqt hogi hi nahi. Isse namumkin validation scores aate hain aur model production me dhah jaata hai. Agar accuracy shak ke laayak chhalaang lagaye, to jashn se pehle leak dhoondho.

### Chhota code

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

**Yaad rakho:** Mushkil business problem par 0.999 AUC ek bug report hai, result nahi.

**Aam galti:** Leaked model ship karke asli accuracy gusse wale users se pata chalna.

Practice: `examples/09_splitting_graph_data_without_leakage.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Fraud rings as a GNN problem

### Aasaan Bhasha

GNN edges ke saath messages bhejta hai: har node apne padosiyon se khud ko update karta hai, k baar, taaki information k hops tak safar kare. Fraud rings, molecules aur social graphs ke liye badhiya — jahan bhi rishte nodes se zyada signal rakhte hain.

### Chhota code

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

**Yaad rakho:** Bahut zyada message-passing layers over-smoothing kar deti hain — har node ek jaisa vector ban jaata hai.

**Aam galti:** Graph data ko randomly split karna, jisse ek node ke apne padosi train aur test dono me aa jaate hain.

Practice: `examples/10_fraud_rings_as_a_gnn_problem.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 98 ke baad aapko ye aana chahiye

- **Data that is naturally a graph** ko bina notes dekhe kisi dost ko samjha sakna.
- **Adjacency and node features** ko bina notes dekhe kisi dost ko samjha sakna.
- **Message passing** ko bina notes dekhe kisi dost ko samjha sakna.
- **Graph convolution** ko bina notes dekhe kisi dost ko samjha sakna.
- **GraphSAGE and sampling** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
