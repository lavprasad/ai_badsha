# Day 111 — Vision transformers

Aaj ka goal: **Vision transformers** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Images as patch sequences |
| 2 | Patch embedding |
| 3 | Positional embeddings for images |
| 4 | ViT architecture |
| 5 | Data hunger of ViTs |
| 6 | DeiT and distillation |
| 7 | Swin and hierarchical attention |
| 8 | ViT vs CNN trade-offs |
| 9 | Fine-tuning a ViT |
| 10 | Attention maps as explanation |

---

## 1. Images as patch sequences

### Aasaan Bhasha

Transformer block = attention + feed-forward, dono residual connection aur LayerNorm me lipte hue. Akeli attention order-blind hai, isliye positions alag se daali jaati hain. Encoder-only (BERT) samajhne ke liye, decoder-only (GPT) generation ke liye, encoder-decoder (T5) translation jaise tasks ke liye.

### Chhota code

```python
import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / np.power(10_000, (2 * (i // 2)) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe

pe = positional_encoding(6, 8)
print(pe.round(2))
print('shape', pe.shape)
```

**Yaad rakho:** Block = LayerNorm -> Attention -> residual add -> LayerNorm -> MLP -> residual add. Ise ratt lo.

**Aam galti:** Yeh maan lena ki bada context window muft hai — attention ka cost sequence length ke square se badhta hai.

Practice: `examples/01_images_as_patch_sequences.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Patch embedding

### Aasaan Bhasha

Embedding text ko dense vector me badalta hai jahan paas hona matlab matlab me paas hona. Keyword search ke ulat, 'car trouble' 'engine won't start' se match ho jaata hai. Har RAG system embeddings + nearest-neighbour lookup hi hai.

### Chhota code

```python
import numpy as np

# Toy 3-D 'embeddings' to show the mechanics
vecs = {
    'king':  np.array([0.9, 0.8, 0.1]),
    'queen': np.array([0.9, 0.1, 0.8]),
    'man':   np.array([0.4, 0.9, 0.1]),
    'woman': np.array([0.4, 0.1, 0.9]),
}

def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

analogy = vecs['king'] - vecs['man'] + vecs['woman']
best = max(vecs, key=lambda w: cos(analogy, vecs[w]) if w != 'king' else -1)
print('king - man + woman ~', best)
```

**Yaad rakho:** Embeddings normalise kar do, phir cosine similarity sirf dot product hai — scale par bahut tez.

**Aam galti:** Ek hi index me do alag embedding models ke vectors mila dena; wo spaces aapas me bilkul unrelated hain.

Practice: `examples/02_patch_embedding.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Positional embeddings for images

### Aasaan Bhasha

Embedding text ko dense vector me badalta hai jahan paas hona matlab matlab me paas hona. Keyword search ke ulat, 'car trouble' 'engine won't start' se match ho jaata hai. Har RAG system embeddings + nearest-neighbour lookup hi hai.

### Chhota code

```python
import numpy as np

# Toy 3-D 'embeddings' to show the mechanics
vecs = {
    'king':  np.array([0.9, 0.8, 0.1]),
    'queen': np.array([0.9, 0.1, 0.8]),
    'man':   np.array([0.4, 0.9, 0.1]),
    'woman': np.array([0.4, 0.1, 0.9]),
}

def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

analogy = vecs['king'] - vecs['man'] + vecs['woman']
best = max(vecs, key=lambda w: cos(analogy, vecs[w]) if w != 'king' else -1)
print('king - man + woman ~', best)
```

**Yaad rakho:** Embeddings normalise kar do, phir cosine similarity sirf dot product hai — scale par bahut tez.

**Aam galti:** Ek hi index me do alag embedding models ke vectors mila dena; wo spaces aapas me bilkul unrelated hain.

Practice: `examples/03_positional_embeddings_for_images.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. ViT architecture

### Aasaan Bhasha

Transformer block = attention + feed-forward, dono residual connection aur LayerNorm me lipte hue. Akeli attention order-blind hai, isliye positions alag se daali jaati hain. Encoder-only (BERT) samajhne ke liye, decoder-only (GPT) generation ke liye, encoder-decoder (T5) translation jaise tasks ke liye.

### Chhota code

```python
import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / np.power(10_000, (2 * (i // 2)) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe

pe = positional_encoding(6, 8)
print(pe.round(2))
print('shape', pe.shape)
```

**Yaad rakho:** Block = LayerNorm -> Attention -> residual add -> LayerNorm -> MLP -> residual add. Ise ratt lo.

**Aam galti:** Yeh maan lena ki bada context window muft hai — attention ka cost sequence length ke square se badhta hai.

Practice: `examples/04_vit_architecture.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Data hunger of ViTs

### Aasaan Bhasha

Transformer block = attention + feed-forward, dono residual connection aur LayerNorm me lipte hue. Akeli attention order-blind hai, isliye positions alag se daali jaati hain. Encoder-only (BERT) samajhne ke liye, decoder-only (GPT) generation ke liye, encoder-decoder (T5) translation jaise tasks ke liye.

### Chhota code

```python
import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / np.power(10_000, (2 * (i // 2)) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe

pe = positional_encoding(6, 8)
print(pe.round(2))
print('shape', pe.shape)
```

**Yaad rakho:** Block = LayerNorm -> Attention -> residual add -> LayerNorm -> MLP -> residual add. Ise ratt lo.

**Aam galti:** Yeh maan lena ki bada context window muft hai — attention ka cost sequence length ke square se badhta hai.

Practice: `examples/05_data_hunger_of_vits.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. DeiT and distillation

### Aasaan Bhasha

Transformer block = attention + feed-forward, dono residual connection aur LayerNorm me lipte hue. Akeli attention order-blind hai, isliye positions alag se daali jaati hain. Encoder-only (BERT) samajhne ke liye, decoder-only (GPT) generation ke liye, encoder-decoder (T5) translation jaise tasks ke liye.

### Chhota code

```python
import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / np.power(10_000, (2 * (i // 2)) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe

pe = positional_encoding(6, 8)
print(pe.round(2))
print('shape', pe.shape)
```

**Yaad rakho:** Block = LayerNorm -> Attention -> residual add -> LayerNorm -> MLP -> residual add. Ise ratt lo.

**Aam galti:** Yeh maan lena ki bada context window muft hai — attention ka cost sequence length ke square se badhta hai.

Practice: `examples/06_deit_and_distillation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Swin and hierarchical attention

### Aasaan Bhasha

Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.

### Chhota code

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')
```

**Yaad rakho:** Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.

**Aam galti:** Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.

Practice: `examples/07_swin_and_hierarchical_attention.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. ViT vs CNN trade-offs

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

Practice: `examples/08_vit_vs_cnn_trade_offs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Fine-tuning a ViT

### Aasaan Bhasha

Hyperparameters wo settings hain jo aap chunte ho, seekhi nahi jaatin. Grid search poora chhaanta hai aur barbaad karta hai; random search high dimensions me acche ilaake jaldi dhoondta hai; Bayesian search pichhle trials se seekhta hai. Search hamesha cross-validation ke andar karo.

### Chhota code

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Yaad rakho:** Random seed fix karo aur har trial log karo, warna aap apna hi best model dobara nahi bana paoge.

**Aam galti:** 400 rows par 40 hyperparameters tune karna — ab aap validation set hi fit kar rahe ho.

Practice: `examples/09_fine_tuning_a_vit.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Attention maps as explanation

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

Practice: `examples/10_attention_maps_as_explanation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 111 ke baad aapko ye aana chahiye

- **Images as patch sequences** ko bina notes dekhe kisi dost ko samjha sakna.
- **Patch embedding** ko bina notes dekhe kisi dost ko samjha sakna.
- **Positional embeddings for images** ko bina notes dekhe kisi dost ko samjha sakna.
- **ViT architecture** ko bina notes dekhe kisi dost ko samjha sakna.
- **Data hunger of ViTs** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
