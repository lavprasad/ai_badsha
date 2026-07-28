# Day 33 — Distance, similarity and geometry

Today's goal: work through **Distance, similarity and geometry** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Euclidean and Manhattan distance |
| 2 | Minkowski family |
| 3 | Cosine distance vs Euclidean |
| 4 | Mahalanobis distance |
| 5 | Jaccard and set similarity |
| 6 | Edit distance for strings |
| 7 | The curse of dimensionality |
| 8 | Metric vs non-metric similarity |
| 9 | Choosing a distance for your data |
| 10 | Distances that power vector search |

---

## 1. Euclidean and Manhattan distance

The distance function *is* your definition of similarity. Euclidean assumes all dimensions are comparable, Manhattan is robust to outliers in single dimensions, Mahalanobis accounts for correlation, Jaccard compares sets, edit distance compares strings. In high dimensions all Euclidean distances converge — that is the curse.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')
```

**Remember:** As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.

**Common mistake:** Using Euclidean distance on features with wildly different units and calling the result similarity.

Practice: open `examples/01_euclidean_and_manhattan_distance.py`, predict the output, change one line, predict again.

## 2. Minkowski family

The distance function *is* your definition of similarity. Euclidean assumes all dimensions are comparable, Manhattan is robust to outliers in single dimensions, Mahalanobis accounts for correlation, Jaccard compares sets, edit distance compares strings. In high dimensions all Euclidean distances converge — that is the curse.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')
```

**Remember:** As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.

**Common mistake:** Using Euclidean distance on features with wildly different units and calling the result similarity.

Practice: open `examples/02_minkowski_family.py`, predict the output, change one line, predict again.

## 3. Cosine distance vs Euclidean

Today's idea — **Cosine distance vs Euclidean** — sits inside the theme of Distance, similarity and geometry. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Cosine distance vs Euclidean
print("practice: Cosine distance vs Euclidean")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Cosine distance vs Euclidean` makes about your data before you use it.

**Common mistake:** Copy-pasting `Cosine distance vs Euclidean` from a tutorial without knowing what it assumes or when it fails.

Practice: open `examples/03_cosine_distance_vs_euclidean.py`, predict the output, change one line, predict again.

## 4. Mahalanobis distance

The distance function *is* your definition of similarity. Euclidean assumes all dimensions are comparable, Manhattan is robust to outliers in single dimensions, Mahalanobis accounts for correlation, Jaccard compares sets, edit distance compares strings. In high dimensions all Euclidean distances converge — that is the curse.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')
```

**Remember:** As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.

**Common mistake:** Using Euclidean distance on features with wildly different units and calling the result similarity.

Practice: open `examples/04_mahalanobis_distance.py`, predict the output, change one line, predict again.

## 5. Jaccard and set similarity

The distance function *is* your definition of similarity. Euclidean assumes all dimensions are comparable, Manhattan is robust to outliers in single dimensions, Mahalanobis accounts for correlation, Jaccard compares sets, edit distance compares strings. In high dimensions all Euclidean distances converge — that is the curse.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')
```

**Remember:** As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.

**Common mistake:** Using Euclidean distance on features with wildly different units and calling the result similarity.

Practice: open `examples/05_jaccard_and_set_similarity.py`, predict the output, change one line, predict again.

## 6. Edit distance for strings

The distance function *is* your definition of similarity. Euclidean assumes all dimensions are comparable, Manhattan is robust to outliers in single dimensions, Mahalanobis accounts for correlation, Jaccard compares sets, edit distance compares strings. In high dimensions all Euclidean distances converge — that is the curse.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')
```

**Remember:** As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.

**Common mistake:** Using Euclidean distance on features with wildly different units and calling the result similarity.

Practice: open `examples/06_edit_distance_for_strings.py`, predict the output, change one line, predict again.

## 7. The curse of dimensionality

The distance function *is* your definition of similarity. Euclidean assumes all dimensions are comparable, Manhattan is robust to outliers in single dimensions, Mahalanobis accounts for correlation, Jaccard compares sets, edit distance compares strings. In high dimensions all Euclidean distances converge — that is the curse.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')
```

**Remember:** As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.

**Common mistake:** Using Euclidean distance on features with wildly different units and calling the result similarity.

Practice: open `examples/07_the_curse_of_dimensionality.py`, predict the output, change one line, predict again.

## 8. Metric vs non-metric similarity

The distance function *is* your definition of similarity. Euclidean assumes all dimensions are comparable, Manhattan is robust to outliers in single dimensions, Mahalanobis accounts for correlation, Jaccard compares sets, edit distance compares strings. In high dimensions all Euclidean distances converge — that is the curse.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')
```

**Remember:** As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.

**Common mistake:** Using Euclidean distance on features with wildly different units and calling the result similarity.

Practice: open `examples/08_metric_vs_non_metric_similarity.py`, predict the output, change one line, predict again.

## 9. Choosing a distance for your data

The distance function *is* your definition of similarity. Euclidean assumes all dimensions are comparable, Manhattan is robust to outliers in single dimensions, Mahalanobis accounts for correlation, Jaccard compares sets, edit distance compares strings. In high dimensions all Euclidean distances converge — that is the curse.

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 0.0, 3.0])
print('euclidean', round(float(np.linalg.norm(a - b)), 3))
print('manhattan', round(float(np.abs(a - b).sum()), 3))

s1, s2 = {'ml', 'ai', 'data'}, {'ai', 'data', 'stats'}
print('jaccard  ', round(len(s1 & s2) / len(s1 | s2), 3))

rng = np.random.default_rng(0)
for d in (2, 10, 100, 1000):
    pts = rng.normal(size=(200, d))
    dists = np.linalg.norm(pts[:100] - pts[100:], axis=1)
    print(f'dim {d:>4}: spread/mean = {dists.std() / dists.mean():.3f}')
```

**Remember:** As dimensions grow, the ratio of distance spread to mean shrinks — nearest neighbour stops meaning much.

**Common mistake:** Using Euclidean distance on features with wildly different units and calling the result similarity.

Practice: open `examples/09_choosing_a_distance_for_your_data.py`, predict the output, change one line, predict again.

## 10. Distances that power vector search

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

Practice: open `examples/10_distances_that_power_vector_search.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 33

- Explain **Euclidean and Manhattan distance** to someone else without notes.
- Explain **Minkowski family** to someone else without notes.
- Explain **Cosine distance vs Euclidean** to someone else without notes.
- Explain **Mahalanobis distance** to someone else without notes.
- Explain **Jaccard and set similarity** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
