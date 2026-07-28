# Day 06 — NumPy foundations

Today's goal: work through **NumPy foundations** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why NumPy is fast: contiguous memory |
| 2 | Creating arrays: array, zeros, arange, linspace |
| 3 | dtype and memory footprint |
| 4 | Shape, reshape and ravel |
| 5 | Indexing, slicing and views vs copies |
| 6 | Boolean masking |
| 7 | Fancy indexing |
| 8 | Vectorisation vs Python loops |
| 9 | Random numbers with default_rng |
| 10 | Timing a vectorised speedup |

---

## 1. Why NumPy is fast: contiguous memory

Today's idea — **Why NumPy is fast: contiguous memory** — sits inside the theme of NumPy foundations. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Why NumPy is fast: contiguous memory
print("practice: Why NumPy is fast: contiguous memory")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Why NumPy is fast: contiguous memory` makes about your data before you use it.

**Common mistake:** Copy-pasting `Why NumPy is fast: contiguous memory` from a tutorial without knowing what it assumes or when it fails.

Practice: open `examples/01_why_numpy_is_fast_contiguous_memory.py`, predict the output, change one line, predict again.

## 2. Creating arrays: array, zeros, arange, linspace

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

Practice: open `examples/02_creating_arrays_array_zeros_arange_linsp.py`, predict the output, change one line, predict again.

## 3. dtype and memory footprint

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

Practice: open `examples/03_dtype_and_memory_footprint.py`, predict the output, change one line, predict again.

## 4. Shape, reshape and ravel

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

Practice: open `examples/04_shape_reshape_and_ravel.py`, predict the output, change one line, predict again.

## 5. Indexing, slicing and views vs copies

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

Practice: open `examples/05_indexing_slicing_and_views_vs_copies.py`, predict the output, change one line, predict again.

## 6. Boolean masking

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

Practice: open `examples/06_boolean_masking.py`, predict the output, change one line, predict again.

## 7. Fancy indexing

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

Practice: open `examples/07_fancy_indexing.py`, predict the output, change one line, predict again.

## 8. Vectorisation vs Python loops

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

Practice: open `examples/08_vectorisation_vs_python_loops.py`, predict the output, change one line, predict again.

## 9. Random numbers with default_rng

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

Practice: open `examples/09_random_numbers_with_default_rng.py`, predict the output, change one line, predict again.

## 10. Timing a vectorised speedup

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

Practice: open `examples/10_timing_a_vectorised_speedup.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 06

- Explain **Why NumPy is fast: contiguous memory** to someone else without notes.
- Explain **Creating arrays: array, zeros, arange, linspace** to someone else without notes.
- Explain **dtype and memory footprint** to someone else without notes.
- Explain **Shape, reshape and ravel** to someone else without notes.
- Explain **Indexing, slicing and views vs copies** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
