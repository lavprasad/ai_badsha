# Day 135 — Embeddings and semantic search

Aaj ka goal: **Embeddings and semantic search** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Embedding models today |
| 2 | Symmetric vs asymmetric search |
| 3 | Normalisation and cosine similarity |
| 4 | Approximate nearest neighbour algorithms |
| 5 | HNSW indexes |
| 6 | Vector databases compared |
| 7 | Metadata filtering |
| 8 | Hybrid search with BM25 |
| 9 | Evaluating retrieval quality |
| 10 | Building a semantic search over your notes |

---

## 1. Embedding models today

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

Practice: `examples/01_embedding_models_today.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Symmetric vs asymmetric search

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

Practice: `examples/02_symmetric_vs_asymmetric_search.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Normalisation and cosine similarity

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/03_normalisation_and_cosine_similarity.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Approximate nearest neighbour algorithms

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/04_approximate_nearest_neighbour_algorithms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. HNSW indexes

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

Practice: `examples/05_hnsw_indexes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Vector databases compared

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/06_vector_databases_compared.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Metadata filtering

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

Practice: `examples/07_metadata_filtering.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Hybrid search with BM25

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

Practice: `examples/08_hybrid_search_with_bm25.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Evaluating retrieval quality

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

Practice: `examples/09_evaluating_retrieval_quality.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Building a semantic search over your notes

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

Practice: `examples/10_building_a_semantic_search_over_your_not.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 135 ke baad aapko ye aana chahiye

- **Embedding models today** ko bina notes dekhe kisi dost ko samjha sakna.
- **Symmetric vs asymmetric search** ko bina notes dekhe kisi dost ko samjha sakna.
- **Normalisation and cosine similarity** ko bina notes dekhe kisi dost ko samjha sakna.
- **Approximate nearest neighbour algorithms** ko bina notes dekhe kisi dost ko samjha sakna.
- **HNSW indexes** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
