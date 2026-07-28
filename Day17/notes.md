# Day 17 — Matrices and linear transformations

Today's goal: work through **Matrices and linear transformations** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | A matrix as a transformation |
| 2 | Matrix multiplication rules and shapes |
| 3 | Identity and inverse matrices |
| 4 | Transpose and symmetric matrices |
| 5 | Determinant and what zero means |
| 6 | Rank and rank deficiency |
| 7 | Solving linear systems with solve |
| 8 | Why inv() is the wrong tool |
| 9 | Sparse matrices and when they matter |
| 10 | Batched matrix operations |

---

## 1. A matrix as a transformation

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

## 2. Matrix multiplication rules and shapes

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

## 3. Identity and inverse matrices

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

## 4. Transpose and symmetric matrices

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

## 5. Determinant and what zero means

Missing data is information, not just noise. Before filling anything, ask *why* it is missing: a sensor that fails only under load is not missing at random. Then choose: drop rows, drop the column, fill with a statistic, or add an explicit 'was missing' indicator column.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Remember:** Compute the fill statistic on the TRAIN split only, then apply it to test.

**Common mistake:** Filling with the mean computed over the full dataset — that leaks test information into training.

## 6. Rank and rank deficiency

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

## 7. Solving linear systems with solve

To solve `Ax = b`, use a solver, not an inverse. Computing `inv(A) @ b` is slower and numerically worse. Sparse matrices (mostly zeros — text features, graphs) need sparse storage or you will allocate gigabytes of zeros.

```python
import numpy as np

rng = np.random.default_rng(0)
A = rng.normal(size=(500, 500)) + np.eye(500) * 5
b = rng.normal(size=500)

x_solve = np.linalg.solve(A, b)
x_inv = np.linalg.inv(A) @ b
print('same answer:', np.allclose(x_solve, x_inv))
print('residual solve:', float(np.linalg.norm(A @ x_solve - b)))
print('residual inv  :', float(np.linalg.norm(A @ x_inv - b)))
```

**Remember:** `np.linalg.solve(A, b)` over `inv(A) @ b`, always.

**Common mistake:** Densifying a sparse TF-IDF matrix with `.toarray()` and exhausting memory.

## 8. Why inv() is the wrong tool

To solve `Ax = b`, use a solver, not an inverse. Computing `inv(A) @ b` is slower and numerically worse. Sparse matrices (mostly zeros — text features, graphs) need sparse storage or you will allocate gigabytes of zeros.

```python
import numpy as np

rng = np.random.default_rng(0)
A = rng.normal(size=(500, 500)) + np.eye(500) * 5
b = rng.normal(size=500)

x_solve = np.linalg.solve(A, b)
x_inv = np.linalg.inv(A) @ b
print('same answer:', np.allclose(x_solve, x_inv))
print('residual solve:', float(np.linalg.norm(A @ x_solve - b)))
print('residual inv  :', float(np.linalg.norm(A @ x_inv - b)))
```

**Remember:** `np.linalg.solve(A, b)` over `inv(A) @ b`, always.

**Common mistake:** Densifying a sparse TF-IDF matrix with `.toarray()` and exhausting memory.

## 9. Sparse matrices and when they matter

To solve `Ax = b`, use a solver, not an inverse. Computing `inv(A) @ b` is slower and numerically worse. Sparse matrices (mostly zeros — text features, graphs) need sparse storage or you will allocate gigabytes of zeros.

```python
import numpy as np

rng = np.random.default_rng(0)
A = rng.normal(size=(500, 500)) + np.eye(500) * 5
b = rng.normal(size=500)

x_solve = np.linalg.solve(A, b)
x_inv = np.linalg.inv(A) @ b
print('same answer:', np.allclose(x_solve, x_inv))
print('residual solve:', float(np.linalg.norm(A @ x_solve - b)))
print('residual inv  :', float(np.linalg.norm(A @ x_inv - b)))
```

**Remember:** `np.linalg.solve(A, b)` over `inv(A) @ b`, always.

**Common mistake:** Densifying a sparse TF-IDF matrix with `.toarray()` and exhausting memory.

## 10. Batched matrix operations

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

---

## What you should be able to do after Day 17

- Explain **A matrix as a transformation** to someone else without notes.
- Explain **Matrix multiplication rules and shapes** to someone else without notes.
- Explain **Identity and inverse matrices** to someone else without notes.
- Explain **Transpose and symmetric matrices** to someone else without notes.
- Explain **Determinant and what zero means** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
