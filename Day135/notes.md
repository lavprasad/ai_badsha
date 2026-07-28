# Day 135 — Embeddings and semantic search

Today's goal: work through **Embeddings and semantic search** — ten concepts, ten runnable examples, five questions.

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

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

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

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

Practice: open `examples/01_embedding_models_today.py`, predict the output, change one line, predict again.

## 2. Symmetric vs asymmetric search

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

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

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

Practice: open `examples/02_symmetric_vs_asymmetric_search.py`, predict the output, change one line, predict again.

## 3. Normalisation and cosine similarity

A vector is a list of numbers with a direction and length. The dot product measures alignment: large and positive when two vectors point the same way, zero when perpendicular. Cosine similarity is the dot product with length divided out, which is why it compares embeddings of different magnitudes fairly.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Remember:** Cosine similarity ignores magnitude; Euclidean distance does not. Pick the one that matches your question.

**Common mistake:** Comparing raw embeddings with Euclidean distance when only direction carries meaning.

Practice: open `examples/03_normalisation_and_cosine_similarity.py`, predict the output, change one line, predict again.

## 4. Approximate nearest neighbour algorithms

kNN has no training step: it stores the data and, at prediction time, votes among the k closest points. It is a great sanity baseline, and it is also literally what a vector database does for retrieval — so understanding it pays off twice.

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

**Remember:** Scale your features first — kNN is pure distance, so units decide the answer.

**Common mistake:** Using kNN on high-dimensional data where every point is roughly equidistant from every other.

Practice: open `examples/04_approximate_nearest_neighbour_algorithms.py`, predict the output, change one line, predict again.

## 5. HNSW indexes

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

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

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

Practice: open `examples/05_hnsw_indexes.py`, predict the output, change one line, predict again.

## 6. Vector databases compared

A vector is a list of numbers with a direction and length. The dot product measures alignment: large and positive when two vectors point the same way, zero when perpendicular. Cosine similarity is the dot product with length divided out, which is why it compares embeddings of different magnitudes fairly.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Remember:** Cosine similarity ignores magnitude; Euclidean distance does not. Pick the one that matches your question.

**Common mistake:** Comparing raw embeddings with Euclidean distance when only direction carries meaning.

Practice: open `examples/06_vector_databases_compared.py`, predict the output, change one line, predict again.

## 7. Metadata filtering

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

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

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

Practice: open `examples/07_metadata_filtering.py`, predict the output, change one line, predict again.

## 8. Hybrid search with BM25

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

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

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

Practice: open `examples/08_hybrid_search_with_bm25.py`, predict the output, change one line, predict again.

## 9. Evaluating retrieval quality

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

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

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

Practice: open `examples/09_evaluating_retrieval_quality.py`, predict the output, change one line, predict again.

## 10. Building a semantic search over your notes

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

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

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

Practice: open `examples/10_building_a_semantic_search_over_your_not.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 135

- Explain **Embedding models today** to someone else without notes.
- Explain **Symmetric vs asymmetric search** to someone else without notes.
- Explain **Normalisation and cosine similarity** to someone else without notes.
- Explain **Approximate nearest neighbour algorithms** to someone else without notes.
- Explain **HNSW indexes** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
