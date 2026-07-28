# Day 07 — NumPy for maths

Today's goal: work through **NumPy for maths** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Element-wise arithmetic |
| 2 | Broadcasting rules |
| 3 | Reductions: sum, mean, max along an axis |
| 4 | Matrix multiplication with @ |
| 5 | Transpose and axis swapping |
| 6 | Stacking: concatenate, vstack, hstack |
| 7 | np.where and conditional logic |
| 8 | Sorting and argsort |
| 9 | Saving and loading .npy files |
| 10 | Common shape errors and how to read them |

---

## 1. Element-wise arithmetic

NumPy's power is selecting and combining without loops. A boolean mask picks rows by condition, fancy indexing picks them by position, `np.where` builds a new array from a condition, and `argsort` gives you the ordering so you can sort several arrays consistently.

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Remember:** A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.

**Common mistake:** Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

## 2. Broadcasting rules

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

## 3. Reductions: sum, mean, max along an axis

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

## 4. Matrix multiplication with @

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

## 5. Transpose and axis swapping

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

## 6. Stacking: concatenate, vstack, hstack

NumPy's power is selecting and combining without loops. A boolean mask picks rows by condition, fancy indexing picks them by position, `np.where` builds a new array from a condition, and `argsort` gives you the ordering so you can sort several arrays consistently.

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Remember:** A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.

**Common mistake:** Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

## 7. np.where and conditional logic

NumPy's power is selecting and combining without loops. A boolean mask picks rows by condition, fancy indexing picks them by position, `np.where` builds a new array from a condition, and `argsort` gives you the ordering so you can sort several arrays consistently.

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Remember:** A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.

**Common mistake:** Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

## 8. Sorting and argsort

NumPy's power is selecting and combining without loops. A boolean mask picks rows by condition, fancy indexing picks them by position, `np.where` builds a new array from a condition, and `argsort` gives you the ordering so you can sort several arrays consistently.

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Remember:** A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.

**Common mistake:** Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

## 9. Saving and loading .npy files

NumPy's power is selecting and combining without loops. A boolean mask picks rows by condition, fancy indexing picks them by position, `np.where` builds a new array from a condition, and `argsort` gives you the ordering so you can sort several arrays consistently.

```python
import numpy as np

rng = np.random.default_rng(0)
x = rng.integers(0, 100, size=10)
print('data      ', x)

mask = x > 50
print('mask      ', mask)
print('selected  ', x[mask])                 # boolean mask
print('positions ', x[[0, 3, 5]])            # fancy indexing
print('clipped   ', np.where(x > 50, 50, x)) # conditional build

order = np.argsort(-x)
print('top 3     ', x[order[:3]])
```

**Remember:** A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.

**Common mistake:** Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

## 10. Common shape errors and how to read them

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

---

## What you should be able to do after Day 07

- Explain **Element-wise arithmetic** to someone else without notes.
- Explain **Broadcasting rules** to someone else without notes.
- Explain **Reductions: sum, mean, max along an axis** to someone else without notes.
- Explain **Matrix multiplication with @** to someone else without notes.
- Explain **Transpose and axis swapping** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
