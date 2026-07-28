# Day 27 — Linear algebra in practice

Today's goal: work through **Linear algebra in practice** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Representing a dataset as a matrix |
| 2 | Feature scaling as a linear map |
| 3 | Normal equations for least squares |
| 4 | Numerical stability in practice |
| 5 | float32 vs float64 trade-offs |
| 6 | Broadcasting pitfalls in real code |
| 7 | Einstein summation with einsum |
| 8 | Memory layout and cache effects |
| 9 | Benchmarking matrix operations |
| 10 | Reading shapes in a model summary |

---

## 1. Representing a dataset as a matrix

A matrix is a linear transformation. Multiplying matrices composes transformations, which is exactly what stacking neural network layers does. Shapes must line up: (m,k) @ (k,n) -> (m,n); the inner dimensions must match and they vanish.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))
```

**Remember:** Read every shape error as 'the inner dimensions did not match' and print the shapes.

**Common mistake:** Reaching for `np.linalg.inv` to solve `Ax=b` instead of the numerically safer `np.linalg.solve`.

Practice: open `examples/01_representing_a_dataset_as_a_matrix.py`, predict the output, change one line, predict again.

## 2. Feature scaling as a linear map

Distance and gradient-based models care about units: a salary column in rupees will dominate an age column purely by magnitude. Standardise (mean 0, std 1) for most models; min-max scale when you need a bounded [0,1] range. Tree models do not care.

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
print('cv accuracy', cross_val_score(pipe, X, y, cv=5).mean().round(4))
```

**Remember:** Put the scaler INSIDE a Pipeline so cross-validation refits it per fold and cannot leak.

**Common mistake:** Calling `fit_transform` on the full dataset before splitting — classic, silent, score-inflating leak.

Practice: open `examples/02_feature_scaling_as_a_linear_map.py`, predict the output, change one line, predict again.

## 3. Normal equations for least squares

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

Practice: open `examples/03_normal_equations_for_least_squares.py`, predict the output, change one line, predict again.

## 4. Numerical stability in practice

`einsum` writes tensor contractions as index notation — clearer than a chain of transposes and reshapes. float32 halves memory and is standard for training; float64 is for scientific work where accumulation error matters. Row-major layout means iterating along the last axis is cache-friendly and much faster.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(4, 5))
B = np.random.default_rng(1).normal(size=(5, 3))

print(np.allclose(A @ B, np.einsum('ik,kj->ij', A, B)))
print('batched trace:', np.einsum('ii->', A @ A.T).round(3))

small = A.astype(np.float32)
print('float64 bytes', A.nbytes, '| float32 bytes', small.nbytes)
```

**Remember:** Train in float32 (or bf16); reserve float64 for numerically delicate accumulations.

**Common mistake:** Mixing float32 and float64 accidentally and silently doubling memory across a pipeline.

Practice: open `examples/04_numerical_stability_in_practice.py`, predict the output, change one line, predict again.

## 5. float32 vs float64 trade-offs

`einsum` writes tensor contractions as index notation — clearer than a chain of transposes and reshapes. float32 halves memory and is standard for training; float64 is for scientific work where accumulation error matters. Row-major layout means iterating along the last axis is cache-friendly and much faster.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(4, 5))
B = np.random.default_rng(1).normal(size=(5, 3))

print(np.allclose(A @ B, np.einsum('ik,kj->ij', A, B)))
print('batched trace:', np.einsum('ii->', A @ A.T).round(3))

small = A.astype(np.float32)
print('float64 bytes', A.nbytes, '| float32 bytes', small.nbytes)
```

**Remember:** Train in float32 (or bf16); reserve float64 for numerically delicate accumulations.

**Common mistake:** Mixing float32 and float64 accidentally and silently doubling memory across a pipeline.

Practice: open `examples/05_float32_vs_float64_trade_offs.py`, predict the output, change one line, predict again.

## 6. Broadcasting pitfalls in real code

NumPy stores numbers in one contiguous typed block and runs loops in C. Vectorised code (whole-array operations) is often 50-100x faster than a Python `for` loop and reads closer to the maths. Broadcasting stretches smaller shapes to match without copying data.

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
print(a.shape, a.dtype)

b = np.array([10, 20, 30])       # shape (3,)
print(a + b)                     # broadcast over rows

print(a.sum(axis=0))             # column sums
print(a.sum(axis=1))             # row sums
```

**Remember:** `axis=0` collapses rows (down the columns); `axis=1` collapses columns (across a row).

**Common mistake:** Looping over array elements in Python instead of using a vectorised operation.

Practice: open `examples/06_broadcasting_pitfalls_in_real_code.py`, predict the output, change one line, predict again.

## 7. Einstein summation with einsum

`einsum` writes tensor contractions as index notation — clearer than a chain of transposes and reshapes. float32 halves memory and is standard for training; float64 is for scientific work where accumulation error matters. Row-major layout means iterating along the last axis is cache-friendly and much faster.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(4, 5))
B = np.random.default_rng(1).normal(size=(5, 3))

print(np.allclose(A @ B, np.einsum('ik,kj->ij', A, B)))
print('batched trace:', np.einsum('ii->', A @ A.T).round(3))

small = A.astype(np.float32)
print('float64 bytes', A.nbytes, '| float32 bytes', small.nbytes)
```

**Remember:** Train in float32 (or bf16); reserve float64 for numerically delicate accumulations.

**Common mistake:** Mixing float32 and float64 accidentally and silently doubling memory across a pipeline.

Practice: open `examples/07_einstein_summation_with_einsum.py`, predict the output, change one line, predict again.

## 8. Memory layout and cache effects

`einsum` writes tensor contractions as index notation — clearer than a chain of transposes and reshapes. float32 halves memory and is standard for training; float64 is for scientific work where accumulation error matters. Row-major layout means iterating along the last axis is cache-friendly and much faster.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(4, 5))
B = np.random.default_rng(1).normal(size=(5, 3))

print(np.allclose(A @ B, np.einsum('ik,kj->ij', A, B)))
print('batched trace:', np.einsum('ii->', A @ A.T).round(3))

small = A.astype(np.float32)
print('float64 bytes', A.nbytes, '| float32 bytes', small.nbytes)
```

**Remember:** Train in float32 (or bf16); reserve float64 for numerically delicate accumulations.

**Common mistake:** Mixing float32 and float64 accidentally and silently doubling memory across a pipeline.

Practice: open `examples/08_memory_layout_and_cache_effects.py`, predict the output, change one line, predict again.

## 9. Benchmarking matrix operations

A matrix is a linear transformation. Multiplying matrices composes transformations, which is exactly what stacking neural network layers does. Shapes must line up: (m,k) @ (k,n) -> (m,n); the inner dimensions must match and they vanish.

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))
```

**Remember:** Read every shape error as 'the inner dimensions did not match' and print the shapes.

**Common mistake:** Reaching for `np.linalg.inv` to solve `Ax=b` instead of the numerically safer `np.linalg.solve`.

Practice: open `examples/09_benchmarking_matrix_operations.py`, predict the output, change one line, predict again.

## 10. Reading shapes in a model summary

If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to. Permutation importance is model-agnostic and honest. SHAP gives per-prediction attributions with a solid theoretical basis but costs real compute.

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

X, y = load_breast_cancer(return_X_y=True)
names = load_breast_cancer().feature_names
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=0)
m = RandomForestClassifier(n_estimators=200, random_state=0, n_jobs=-1).fit(Xtr, ytr)

imp = permutation_importance(m, Xte, yte, n_repeats=10, random_state=0)
for i in np.argsort(-imp.importances_mean)[:5]:
    print(f'{names[i]:<28} {imp.importances_mean[i]:.4f}')
```

**Remember:** Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

**Common mistake:** Presenting importance as causation — the model found correlation, nothing more.

Practice: open `examples/10_reading_shapes_in_a_model_summary.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 27

- Explain **Representing a dataset as a matrix** to someone else without notes.
- Explain **Feature scaling as a linear map** to someone else without notes.
- Explain **Normal equations for least squares** to someone else without notes.
- Explain **Numerical stability in practice** to someone else without notes.
- Explain **float32 vs float64 trade-offs** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
