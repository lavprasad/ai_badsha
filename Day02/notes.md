# Day 02 — Python essentials refresher

Today's goal: work through **python essentials refresher** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Variables, types and dynamic typing |
| 2 | Numbers, strings and f-strings |
| 3 | Lists, tuples, sets, dicts |
| 4 | Slicing and indexing rules |
| 5 | if/elif/else and truthiness |
| 6 | for and while loops |
| 7 | Functions, arguments and defaults |
| 8 | Scope and the mutable default trap |
| 9 | Modules, imports and __main__ |
| 10 | Reading the standard library docs |

---

## 1. Variables, types and dynamic typing

Python decides types at runtime, which is fast to write and easy to get subtly wrong. Know your container costs: list for order, set for membership, dict for keyed lookup. Truthiness treats `0`, `''`, `[]`, `{}` and `None` as false — which is why `if x:` and `if x is not None:` are different tests.

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Remember:** `if x:` and `if x is not None:` differ for 0, '' and empty containers. Pick deliberately.

**Common mistake:** Using `if not value:` to check for a missing field and rejecting a legitimate zero.

## 2. Numbers, strings and f-strings

Python decides types at runtime, which is fast to write and easy to get subtly wrong. Know your container costs: list for order, set for membership, dict for keyed lookup. Truthiness treats `0`, `''`, `[]`, `{}` and `None` as false — which is why `if x:` and `if x is not None:` are different tests.

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Remember:** `if x:` and `if x is not None:` differ for 0, '' and empty containers. Pick deliberately.

**Common mistake:** Using `if not value:` to check for a missing field and rejecting a legitimate zero.

## 3. Lists, tuples, sets, dicts

Python decides types at runtime, which is fast to write and easy to get subtly wrong. Know your container costs: list for order, set for membership, dict for keyed lookup. Truthiness treats `0`, `''`, `[]`, `{}` and `None` as false — which is why `if x:` and `if x is not None:` are different tests.

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Remember:** `if x:` and `if x is not None:` differ for 0, '' and empty containers. Pick deliberately.

**Common mistake:** Using `if not value:` to check for a missing field and rejecting a legitimate zero.

## 4. Slicing and indexing rules

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

## 5. if/elif/else and truthiness

Python decides types at runtime, which is fast to write and easy to get subtly wrong. Know your container costs: list for order, set for membership, dict for keyed lookup. Truthiness treats `0`, `''`, `[]`, `{}` and `None` as false — which is why `if x:` and `if x is not None:` are different tests.

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Remember:** `if x:` and `if x is not None:` differ for 0, '' and empty containers. Pick deliberately.

**Common mistake:** Using `if not value:` to check for a missing field and rejecting a legitimate zero.

## 6. for and while loops

Python decides types at runtime, which is fast to write and easy to get subtly wrong. Know your container costs: list for order, set for membership, dict for keyed lookup. Truthiness treats `0`, `''`, `[]`, `{}` and `None` as false — which is why `if x:` and `if x is not None:` are different tests.

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Remember:** `if x:` and `if x is not None:` differ for 0, '' and empty containers. Pick deliberately.

**Common mistake:** Using `if not value:` to check for a missing field and rejecting a legitimate zero.

## 7. Functions, arguments and defaults

Default arguments are evaluated once, at function definition time. A mutable default (list, dict, set) is therefore shared by every call — a bug that shows up as 'my function remembers the last call'. Use `None` and build the real default inside.

```python
def bad(item, bucket=[]):        # created ONCE
    bucket.append(item)
    return bucket

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(bad(1), bad(2))     # [1] [1, 2]  <- leaked
print(good(1), good(2))   # [1] [2]     <- correct
```

**Remember:** Default arguments must be immutable. `None` plus a check is the standard fix.

**Common mistake:** A `def f(x, cache={})` that silently accumulates state across every call in the process.

## 8. Scope and the mutable default trap

Default arguments are evaluated once, at function definition time. A mutable default (list, dict, set) is therefore shared by every call — a bug that shows up as 'my function remembers the last call'. Use `None` and build the real default inside.

```python
def bad(item, bucket=[]):        # created ONCE
    bucket.append(item)
    return bucket

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(bad(1), bad(2))     # [1] [1, 2]  <- leaked
print(good(1), good(2))   # [1] [2]     <- correct
```

**Remember:** Default arguments must be immutable. `None` plus a check is the standard fix.

**Common mistake:** A `def f(x, cache={})` that silently accumulates state across every call in the process.

## 9. Modules, imports and __main__

Today's idea — **Modules, imports and __main__** — sits inside the theme of Python essentials refresher. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Modules, imports and __main__
print("practice: Modules, imports and __main__")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Modules, imports and __main__` makes about your data before you use it.

**Common mistake:** Copy-pasting `Modules, imports and __main__` from a tutorial without knowing what it assumes or when it fails.

## 10. Reading the standard library docs

Type hints do not change runtime behaviour; they change how fast a human (or a checker) understands the function. On a data pipeline, the signature is documentation that cannot go stale. Combine with short functions and honest names and you can drop most comments.

```python
from pathlib import Path

def load_rows(path: Path, limit: int | None = None) -> list[dict[str, str]]:
    """Read a CSV into dicts. `limit` caps rows for quick experiments."""
    import csv
    with path.open(encoding='utf-8', newline='') as fh:
        rows = list(csv.DictReader(fh))
    return rows[:limit] if limit else rows

print(load_rows.__annotations__)
```

**Remember:** Hint the boundaries (function signatures, config objects); skip hints on obvious locals.

**Common mistake:** Annotating everything, including throwaway locals, until the types outweigh the logic.

---

## What you should be able to do after Day 02

- Explain **Variables, types and dynamic typing** to someone else without notes.
- Explain **Numbers, strings and f-strings** to someone else without notes.
- Explain **Lists, tuples, sets, dicts** to someone else without notes.
- Explain **Slicing and indexing rules** to someone else without notes.
- Explain **if/elif/else and truthiness** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
