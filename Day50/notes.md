# Day 50 — k-nearest neighbours

Today's goal: work through **k-nearest neighbours** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | The idea: similarity is prediction |
| 2 | Choosing k |
| 3 | Distance metrics and weighting |
| 4 | Why scaling is mandatory |
| 5 | kNN for regression |
| 6 | Computational cost at prediction time |
| 7 | KD-trees and ball trees |
| 8 | The curse of dimensionality |
| 9 | kNN as the ancestor of vector search |
| 10 | Implementing kNN from scratch |

---

## 1. The idea: similarity is prediction

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

## 2. Choosing k

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

## 3. Distance metrics and weighting

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

## 4. Why scaling is mandatory

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

## 5. kNN for regression

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

## 6. Computational cost at prediction time

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

## 7. KD-trees and ball trees

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

## 8. The curse of dimensionality

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

## 9. kNN as the ancestor of vector search

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

## 10. Implementing kNN from scratch

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

---

## What you should be able to do after Day 50

- Explain **The idea: similarity is prediction** to someone else without notes.
- Explain **Choosing k** to someone else without notes.
- Explain **Distance metrics and weighting** to someone else without notes.
- Explain **Why scaling is mandatory** to someone else without notes.
- Explain **kNN for regression** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
