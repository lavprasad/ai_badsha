# Day 60 — Dimensionality reduction

Today's goal: work through **Dimensionality reduction** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why high dimensions hurt |
| 2 | PCA step by step |
| 3 | Explained variance and choosing components |
| 4 | PCA for visualisation vs for modelling |
| 5 | Kernel PCA |
| 6 | t-SNE and its pitfalls |
| 7 | UMAP |
| 8 | Truncated SVD for sparse text |
| 9 | Feature selection vs feature extraction |
| 10 | Compressing a dataset without losing signal |

---

## 1. Why high dimensions hurt

PCA rotates the data onto axes of maximum variance and lets you drop the rest. It is linear, fast, and reversible. t-SNE and UMAP are for visualisation only — distances between clusters in a t-SNE plot are not meaningful, so never feed t-SNE output into a model.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Remember:** `n_components=0.95` lets PCA pick the count for you by variance target.

**Common mistake:** Running PCA before scaling, so one wide-range column becomes component 1 all by itself.

Practice: open `examples/01_why_high_dimensions_hurt.py`, predict the output, change one line, predict again.

## 2. PCA step by step

PCA rotates the data onto axes of maximum variance and lets you drop the rest. It is linear, fast, and reversible. t-SNE and UMAP are for visualisation only — distances between clusters in a t-SNE plot are not meaningful, so never feed t-SNE output into a model.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Remember:** `n_components=0.95` lets PCA pick the count for you by variance target.

**Common mistake:** Running PCA before scaling, so one wide-range column becomes component 1 all by itself.

Practice: open `examples/02_pca_step_by_step.py`, predict the output, change one line, predict again.

## 3. Explained variance and choosing components

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

Practice: open `examples/03_explained_variance_and_choosing_componen.py`, predict the output, change one line, predict again.

## 4. PCA for visualisation vs for modelling

Plot before you model. A histogram exposes skew and outliers, a scatter exposes non-linearity, and a line of residuals exposes a model that is systematically wrong. Five minutes of plotting saves hours of confused tuning.

```python
import matplotlib
matplotlib.use('Agg')          # headless-safe for scripts/CI
import matplotlib.pyplot as plt
import numpy as np

x = np.random.default_rng(0).normal(size=500)
fig, ax = plt.subplots()
ax.hist(x, bins=30)
ax.set_title('sample distribution')
fig.savefig('hist.png', dpi=120)
print('wrote hist.png')
```

**Remember:** Label the axes. An unlabelled plot is a decoration, not evidence.

**Common mistake:** Judging a model by its accuracy number alone without ever looking at the data.

Practice: open `examples/04_pca_for_visualisation_vs_for_modelling.py`, predict the output, change one line, predict again.

## 5. Kernel PCA

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

Practice: open `examples/05_kernel_pca.py`, predict the output, change one line, predict again.

## 6. t-SNE and its pitfalls

PCA rotates the data onto axes of maximum variance and lets you drop the rest. It is linear, fast, and reversible. t-SNE and UMAP are for visualisation only — distances between clusters in a t-SNE plot are not meaningful, so never feed t-SNE output into a model.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Remember:** `n_components=0.95` lets PCA pick the count for you by variance target.

**Common mistake:** Running PCA before scaling, so one wide-range column becomes component 1 all by itself.

Practice: open `examples/06_t_sne_and_its_pitfalls.py`, predict the output, change one line, predict again.

## 7. UMAP

PCA rotates the data onto axes of maximum variance and lets you drop the rest. It is linear, fast, and reversible. t-SNE and UMAP are for visualisation only — distances between clusters in a t-SNE plot are not meaningful, so never feed t-SNE output into a model.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Remember:** `n_components=0.95` lets PCA pick the count for you by variance target.

**Common mistake:** Running PCA before scaling, so one wide-range column becomes component 1 all by itself.

Practice: open `examples/07_umap.py`, predict the output, change one line, predict again.

## 8. Truncated SVD for sparse text

Eigenvectors are the directions a matrix only stretches, never rotates; the eigenvalue is the stretch factor. SVD generalises this to any matrix and is the engine under PCA, low-rank compression, and LoRA adapters.

```python
import numpy as np

X = np.random.default_rng(0).normal(size=(100, 5))
U, S, Vt = np.linalg.svd(X, full_matrices=False)
print('singular values', np.round(S, 2))

energy = np.cumsum(S ** 2) / np.sum(S ** 2)
print('variance kept by first 2 dims:', round(float(energy[1]), 3))
```

**Remember:** Singular values sorted descending tell you how many dimensions actually carry information.

**Common mistake:** Running PCA/SVD on unscaled features so the largest-unit column dominates every component.

Practice: open `examples/08_truncated_svd_for_sparse_text.py`, predict the output, change one line, predict again.

## 9. Feature selection vs feature extraction

Feature engineering is where domain knowledge beats compute. A ratio, a lag, a time-since-last-event, or a count over a window often adds more than switching algorithms. Selection then removes features that add variance without signal.

```python
import pandas as pd

df = pd.DataFrame({
    'clicks': [10, 5, 0, 30],
    'impressions': [100, 200, 50, 300],
    'ts': pd.to_datetime(['2024-01-01', '2024-01-05', '2024-02-01', '2024-02-10']),
})
df['ctr'] = df['clicks'] / df['impressions'].clip(lower=1)   # ratio beats raw counts
df['days_since_prev'] = df['ts'].diff().dt.days.fillna(0)
df['is_weekend'] = df['ts'].dt.dayofweek.isin([5, 6]).astype(int)
print(df)
```

**Remember:** Every engineered feature must be computable at prediction time with data you will actually have.

**Common mistake:** Building a feature from a column that is only filled in AFTER the event you are predicting.

Practice: open `examples/09_feature_selection_vs_feature_extraction.py`, predict the output, change one line, predict again.

## 10. Compressing a dataset without losing signal

PCA rotates the data onto axes of maximum variance and lets you drop the rest. It is linear, fast, and reversible. t-SNE and UMAP are for visualisation only — distances between clusters in a t-SNE plot are not meaningful, so never feed t-SNE output into a model.

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Remember:** `n_components=0.95` lets PCA pick the count for you by variance target.

**Common mistake:** Running PCA before scaling, so one wide-range column becomes component 1 all by itself.

Practice: open `examples/10_compressing_a_dataset_without_losing_sig.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 60

- Explain **Why high dimensions hurt** to someone else without notes.
- Explain **PCA step by step** to someone else without notes.
- Explain **Explained variance and choosing components** to someone else without notes.
- Explain **PCA for visualisation vs for modelling** to someone else without notes.
- Explain **Kernel PCA** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
