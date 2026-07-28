# Day 97 — Embeddings and representation learning

Today's goal: work through **Embeddings and representation learning** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | What an embedding space is |
| 2 | Learned vs engineered features |
| 3 | Word2vec: skip-gram and CBOW |
| 4 | Negative sampling |
| 5 | Sentence and document embeddings |
| 6 | Image embeddings |
| 7 | Contrastive learning |
| 8 | Self-supervised pretext tasks |
| 9 | Evaluating an embedding space |
| 10 | Embeddings as the interface between models |

---

## 1. What an embedding space is

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

## 2. Learned vs engineered features

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

## 3. Word2vec: skip-gram and CBOW

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

## 4. Negative sampling

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

## 5. Sentence and document embeddings

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

## 6. Image embeddings

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

## 7. Contrastive learning

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

## 8. Self-supervised pretext tasks

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

## 9. Evaluating an embedding space

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

## 10. Embeddings as the interface between models

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

---

## What you should be able to do after Day 97

- Explain **What an embedding space is** to someone else without notes.
- Explain **Learned vs engineered features** to someone else without notes.
- Explain **Word2vec: skip-gram and CBOW** to someone else without notes.
- Explain **Negative sampling** to someone else without notes.
- Explain **Sentence and document embeddings** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
