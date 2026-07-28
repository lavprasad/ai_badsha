# Day 18 — Eigenvalues, SVD and decomposition

Today's goal: work through **Eigenvalues, SVD and decomposition** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Eigenvectors as invariant directions |
| 2 | Eigenvalues as stretch factors |
| 3 | The characteristic equation |
| 4 | Diagonalisation |
| 5 | Singular value decomposition |
| 6 | Low-rank approximation |
| 7 | SVD for image compression |
| 8 | Condition number and numerical stability |
| 9 | Connection to PCA |
| 10 | Connection to LoRA adapters |

---

## 1. Eigenvectors as invariant directions

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

Practice: open `examples/01_eigenvectors_as_invariant_directions.py`, predict the output, change one line, predict again.

## 2. Eigenvalues as stretch factors

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

Practice: open `examples/02_eigenvalues_as_stretch_factors.py`, predict the output, change one line, predict again.

## 3. The characteristic equation

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

Practice: open `examples/03_the_characteristic_equation.py`, predict the output, change one line, predict again.

## 4. Diagonalisation

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

Practice: open `examples/04_diagonalisation.py`, predict the output, change one line, predict again.

## 5. Singular value decomposition

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

Practice: open `examples/05_singular_value_decomposition.py`, predict the output, change one line, predict again.

## 6. Low-rank approximation

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

Practice: open `examples/06_low_rank_approximation.py`, predict the output, change one line, predict again.

## 7. SVD for image compression

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

Practice: open `examples/07_svd_for_image_compression.py`, predict the output, change one line, predict again.

## 8. Condition number and numerical stability

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

Practice: open `examples/08_condition_number_and_numerical_stability.py`, predict the output, change one line, predict again.

## 9. Connection to PCA

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

Practice: open `examples/09_connection_to_pca.py`, predict the output, change one line, predict again.

## 10. Connection to LoRA adapters

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

Practice: open `examples/10_connection_to_lora_adapters.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 18

- Explain **Eigenvectors as invariant directions** to someone else without notes.
- Explain **Eigenvalues as stretch factors** to someone else without notes.
- Explain **The characteristic equation** to someone else without notes.
- Explain **Diagonalisation** to someone else without notes.
- Explain **Singular value decomposition** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
