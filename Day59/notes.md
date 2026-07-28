# Day 59 — Unsupervised learning: clustering

Today's goal: work through **Unsupervised learning: clustering** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | What clustering can and cannot tell you |
| 2 | K-means and Lloyd's algorithm |
| 3 | Choosing k: elbow and silhouette |
| 4 | K-means++ initialisation |
| 5 | Limitations: shape and scale assumptions |
| 6 | DBSCAN and density clustering |
| 7 | Hierarchical clustering and dendrograms |
| 8 | Gaussian mixture models |
| 9 | Evaluating clusters without labels |
| 10 | Customer segmentation walkthrough |

---

## 1. What clustering can and cannot tell you

Clustering groups points with no labels. K-means needs you to pick k and assumes round, similar-sized blobs. DBSCAN finds arbitrary shapes and marks noise but needs a density radius. Always validate clusters against something you understand — clustering will happily invent structure in noise.

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

**Remember:** Silhouette near 1 means tight, well-separated clusters; near 0 means the boundaries are arbitrary.

**Common mistake:** Reading cluster IDs as meaningful labels — they are arbitrary and change between runs.

Practice: open `examples/01_what_clustering_can_and_cannot_tell_you.py`, predict the output, change one line, predict again.

## 2. K-means and Lloyd's algorithm

The mean is pulled around by outliers; the median is not. Report both, plus a spread measure. When mean and median disagree sharply, the distribution is skewed and averages are lying to you.

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Remember:** Quote median + IQR for skewed data, mean + std only for roughly symmetric data.

**Common mistake:** Removing 'outliers' automatically when they are the exact events you were hired to predict.

Practice: open `examples/02_k_means_and_lloyd_s_algorithm.py`, predict the output, change one line, predict again.

## 3. Choosing k: elbow and silhouette

Clustering groups points with no labels. K-means needs you to pick k and assumes round, similar-sized blobs. DBSCAN finds arbitrary shapes and marks noise but needs a density radius. Always validate clusters against something you understand — clustering will happily invent structure in noise.

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

**Remember:** Silhouette near 1 means tight, well-separated clusters; near 0 means the boundaries are arbitrary.

**Common mistake:** Reading cluster IDs as meaningful labels — they are arbitrary and change between runs.

Practice: open `examples/03_choosing_k_elbow_and_silhouette.py`, predict the output, change one line, predict again.

## 4. K-means++ initialisation

The mean is pulled around by outliers; the median is not. Report both, plus a spread measure. When mean and median disagree sharply, the distribution is skewed and averages are lying to you.

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Remember:** Quote median + IQR for skewed data, mean + std only for roughly symmetric data.

**Common mistake:** Removing 'outliers' automatically when they are the exact events you were hired to predict.

Practice: open `examples/04_k_means_initialisation.py`, predict the output, change one line, predict again.

## 5. Limitations: shape and scale assumptions

Clustering groups points with no labels. K-means needs you to pick k and assumes round, similar-sized blobs. DBSCAN finds arbitrary shapes and marks noise but needs a density radius. Always validate clusters against something you understand — clustering will happily invent structure in noise.

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

**Remember:** Silhouette near 1 means tight, well-separated clusters; near 0 means the boundaries are arbitrary.

**Common mistake:** Reading cluster IDs as meaningful labels — they are arbitrary and change between runs.

Practice: open `examples/05_limitations_shape_and_scale_assumptions.py`, predict the output, change one line, predict again.

## 6. DBSCAN and density clustering

Clustering groups points with no labels. K-means needs you to pick k and assumes round, similar-sized blobs. DBSCAN finds arbitrary shapes and marks noise but needs a density radius. Always validate clusters against something you understand — clustering will happily invent structure in noise.

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

**Remember:** Silhouette near 1 means tight, well-separated clusters; near 0 means the boundaries are arbitrary.

**Common mistake:** Reading cluster IDs as meaningful labels — they are arbitrary and change between runs.

Practice: open `examples/06_dbscan_and_density_clustering.py`, predict the output, change one line, predict again.

## 7. Hierarchical clustering and dendrograms

Clustering groups points with no labels. K-means needs you to pick k and assumes round, similar-sized blobs. DBSCAN finds arbitrary shapes and marks noise but needs a density radius. Always validate clusters against something you understand — clustering will happily invent structure in noise.

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

**Remember:** Silhouette near 1 means tight, well-separated clusters; near 0 means the boundaries are arbitrary.

**Common mistake:** Reading cluster IDs as meaningful labels — they are arbitrary and change between runs.

Practice: open `examples/07_hierarchical_clustering_and_dendrograms.py`, predict the output, change one line, predict again.

## 8. Gaussian mixture models

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

Practice: open `examples/08_gaussian_mixture_models.py`, predict the output, change one line, predict again.

## 9. Evaluating clusters without labels

Clustering groups points with no labels. K-means needs you to pick k and assumes round, similar-sized blobs. DBSCAN finds arbitrary shapes and marks noise but needs a density radius. Always validate clusters against something you understand — clustering will happily invent structure in noise.

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

**Remember:** Silhouette near 1 means tight, well-separated clusters; near 0 means the boundaries are arbitrary.

**Common mistake:** Reading cluster IDs as meaningful labels — they are arbitrary and change between runs.

Practice: open `examples/09_evaluating_clusters_without_labels.py`, predict the output, change one line, predict again.

## 10. Customer segmentation walkthrough

Clustering groups points with no labels. K-means needs you to pick k and assumes round, similar-sized blobs. DBSCAN finds arbitrary shapes and marks noise but needs a density radius. Always validate clusters against something you understand — clustering will happily invent structure in noise.

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

**Remember:** Silhouette near 1 means tight, well-separated clusters; near 0 means the boundaries are arbitrary.

**Common mistake:** Reading cluster IDs as meaningful labels — they are arbitrary and change between runs.

Practice: open `examples/10_customer_segmentation_walkthrough.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 59

- Explain **What clustering can and cannot tell you** to someone else without notes.
- Explain **K-means and Lloyd's algorithm** to someone else without notes.
- Explain **Choosing k: elbow and silhouette** to someone else without notes.
- Explain **K-means++ initialisation** to someone else without notes.
- Explain **Limitations: shape and scale assumptions** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
