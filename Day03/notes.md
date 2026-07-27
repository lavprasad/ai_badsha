# Day 03 — Pythonic data handling

Today's goal: work through **pythonic data handling** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | List comprehensions |
| 2 | Dict and set comprehensions |
| 3 | Generators and yield |
| 4 | enumerate, zip and unpacking |
| 5 | map, filter and lambda |
| 6 | sorted with key functions |
| 7 | collections: Counter, defaultdict |
| 8 | itertools for combinatorics |
| 9 | Lazy evaluation for big data |
| 10 | Choosing the right container |

---

## 1. List comprehensions

A comprehension builds a list eagerly; a generator produces items one at a time and never holds the whole sequence in memory. For datasets larger than RAM, generators are the difference between working and crashing.

```python
squares = [x * x for x in range(10)]          # list, all in memory
lazy = (x * x for x in range(10_000_000))    # generator, one at a time

def batches(seq, n):
    buf = []
    for item in seq:
        buf.append(item)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf

print(sum(lazy))
print(next(batches(range(10), 3)))
```

**Remember:** A generator can only be consumed once — re-create it if you need a second pass.

**Common mistake:** Calling `len()` on a generator, or iterating it twice and getting nothing the second time.

## 2. Dict and set comprehensions

These are the tools that replace hand-written loops with one readable line. `Counter` counts, `defaultdict` removes the 'if key not in dict' dance, `sorted(key=...)` sorts by anything, and `zip` walks two sequences together. Reaching for them is the difference between Python that reads like Python and Python that reads like translated Java.

```python
from collections import Counter, defaultdict
from itertools import combinations

words = ['ai', 'ml', 'ai', 'data', 'ml', 'ai']
print('counts   ', Counter(words).most_common(2))

by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)          # no 'if key not in' needed
print('by length', dict(by_len))

scores = {'ai': 0.9, 'ml': 0.4, 'data': 0.7}
print('ranked   ', sorted(scores, key=scores.get, reverse=True))
print('squares  ', {n: n * n for n in range(4)})
print('pairs    ', list(combinations(['a', 'b', 'c'], 2)))

for i, (w, s) in enumerate(zip(scores, scores.values()), 1):
    print(f'  {i}. {w} = {s}')
```

**Remember:** `Counter` and `defaultdict` remove most of the bookkeeping code people write by hand.

**Common mistake:** Building frequency counts with `if k in d: d[k] += 1 else: d[k] = 1` in every script forever.

## 3. Generators and yield

A comprehension builds a list eagerly; a generator produces items one at a time and never holds the whole sequence in memory. For datasets larger than RAM, generators are the difference between working and crashing.

```python
squares = [x * x for x in range(10)]          # list, all in memory
lazy = (x * x for x in range(10_000_000))    # generator, one at a time

def batches(seq, n):
    buf = []
    for item in seq:
        buf.append(item)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf

print(sum(lazy))
print(next(batches(range(10), 3)))
```

**Remember:** A generator can only be consumed once — re-create it if you need a second pass.

**Common mistake:** Calling `len()` on a generator, or iterating it twice and getting nothing the second time.

## 4. enumerate, zip and unpacking

These are the tools that replace hand-written loops with one readable line. `Counter` counts, `defaultdict` removes the 'if key not in dict' dance, `sorted(key=...)` sorts by anything, and `zip` walks two sequences together. Reaching for them is the difference between Python that reads like Python and Python that reads like translated Java.

```python
from collections import Counter, defaultdict
from itertools import combinations

words = ['ai', 'ml', 'ai', 'data', 'ml', 'ai']
print('counts   ', Counter(words).most_common(2))

by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)          # no 'if key not in' needed
print('by length', dict(by_len))

scores = {'ai': 0.9, 'ml': 0.4, 'data': 0.7}
print('ranked   ', sorted(scores, key=scores.get, reverse=True))
print('squares  ', {n: n * n for n in range(4)})
print('pairs    ', list(combinations(['a', 'b', 'c'], 2)))

for i, (w, s) in enumerate(zip(scores, scores.values()), 1):
    print(f'  {i}. {w} = {s}')
```

**Remember:** `Counter` and `defaultdict` remove most of the bookkeeping code people write by hand.

**Common mistake:** Building frequency counts with `if k in d: d[k] += 1 else: d[k] = 1` in every script forever.

## 5. map, filter and lambda

These are the tools that replace hand-written loops with one readable line. `Counter` counts, `defaultdict` removes the 'if key not in dict' dance, `sorted(key=...)` sorts by anything, and `zip` walks two sequences together. Reaching for them is the difference between Python that reads like Python and Python that reads like translated Java.

```python
from collections import Counter, defaultdict
from itertools import combinations

words = ['ai', 'ml', 'ai', 'data', 'ml', 'ai']
print('counts   ', Counter(words).most_common(2))

by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)          # no 'if key not in' needed
print('by length', dict(by_len))

scores = {'ai': 0.9, 'ml': 0.4, 'data': 0.7}
print('ranked   ', sorted(scores, key=scores.get, reverse=True))
print('squares  ', {n: n * n for n in range(4)})
print('pairs    ', list(combinations(['a', 'b', 'c'], 2)))

for i, (w, s) in enumerate(zip(scores, scores.values()), 1):
    print(f'  {i}. {w} = {s}')
```

**Remember:** `Counter` and `defaultdict` remove most of the bookkeeping code people write by hand.

**Common mistake:** Building frequency counts with `if k in d: d[k] += 1 else: d[k] = 1` in every script forever.

## 6. sorted with key functions

These are the tools that replace hand-written loops with one readable line. `Counter` counts, `defaultdict` removes the 'if key not in dict' dance, `sorted(key=...)` sorts by anything, and `zip` walks two sequences together. Reaching for them is the difference between Python that reads like Python and Python that reads like translated Java.

```python
from collections import Counter, defaultdict
from itertools import combinations

words = ['ai', 'ml', 'ai', 'data', 'ml', 'ai']
print('counts   ', Counter(words).most_common(2))

by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)          # no 'if key not in' needed
print('by length', dict(by_len))

scores = {'ai': 0.9, 'ml': 0.4, 'data': 0.7}
print('ranked   ', sorted(scores, key=scores.get, reverse=True))
print('squares  ', {n: n * n for n in range(4)})
print('pairs    ', list(combinations(['a', 'b', 'c'], 2)))

for i, (w, s) in enumerate(zip(scores, scores.values()), 1):
    print(f'  {i}. {w} = {s}')
```

**Remember:** `Counter` and `defaultdict` remove most of the bookkeeping code people write by hand.

**Common mistake:** Building frequency counts with `if k in d: d[k] += 1 else: d[k] = 1` in every script forever.

## 7. collections: Counter, defaultdict

These are the tools that replace hand-written loops with one readable line. `Counter` counts, `defaultdict` removes the 'if key not in dict' dance, `sorted(key=...)` sorts by anything, and `zip` walks two sequences together. Reaching for them is the difference between Python that reads like Python and Python that reads like translated Java.

```python
from collections import Counter, defaultdict
from itertools import combinations

words = ['ai', 'ml', 'ai', 'data', 'ml', 'ai']
print('counts   ', Counter(words).most_common(2))

by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)          # no 'if key not in' needed
print('by length', dict(by_len))

scores = {'ai': 0.9, 'ml': 0.4, 'data': 0.7}
print('ranked   ', sorted(scores, key=scores.get, reverse=True))
print('squares  ', {n: n * n for n in range(4)})
print('pairs    ', list(combinations(['a', 'b', 'c'], 2)))

for i, (w, s) in enumerate(zip(scores, scores.values()), 1):
    print(f'  {i}. {w} = {s}')
```

**Remember:** `Counter` and `defaultdict` remove most of the bookkeeping code people write by hand.

**Common mistake:** Building frequency counts with `if k in d: d[k] += 1 else: d[k] = 1` in every script forever.

## 8. itertools for combinatorics

These are the tools that replace hand-written loops with one readable line. `Counter` counts, `defaultdict` removes the 'if key not in dict' dance, `sorted(key=...)` sorts by anything, and `zip` walks two sequences together. Reaching for them is the difference between Python that reads like Python and Python that reads like translated Java.

```python
from collections import Counter, defaultdict
from itertools import combinations

words = ['ai', 'ml', 'ai', 'data', 'ml', 'ai']
print('counts   ', Counter(words).most_common(2))

by_len = defaultdict(list)
for w in words:
    by_len[len(w)].append(w)          # no 'if key not in' needed
print('by length', dict(by_len))

scores = {'ai': 0.9, 'ml': 0.4, 'data': 0.7}
print('ranked   ', sorted(scores, key=scores.get, reverse=True))
print('squares  ', {n: n * n for n in range(4)})
print('pairs    ', list(combinations(['a', 'b', 'c'], 2)))

for i, (w, s) in enumerate(zip(scores, scores.values()), 1):
    print(f'  {i}. {w} = {s}')
```

**Remember:** `Counter` and `defaultdict` remove most of the bookkeeping code people write by hand.

**Common mistake:** Building frequency counts with `if k in d: d[k] += 1 else: d[k] = 1` in every script forever.

## 9. Lazy evaluation for big data

A comprehension builds a list eagerly; a generator produces items one at a time and never holds the whole sequence in memory. For datasets larger than RAM, generators are the difference between working and crashing.

```python
squares = [x * x for x in range(10)]          # list, all in memory
lazy = (x * x for x in range(10_000_000))    # generator, one at a time

def batches(seq, n):
    buf = []
    for item in seq:
        buf.append(item)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf

print(sum(lazy))
print(next(batches(range(10), 3)))
```

**Remember:** A generator can only be consumed once — re-create it if you need a second pass.

**Common mistake:** Calling `len()` on a generator, or iterating it twice and getting nothing the second time.

## 10. Choosing the right container

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

```python
DOCKERFILE = '''
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
'''
print(DOCKERFILE)
print('Copy requirements first so the pip layer caches across code changes.')
```

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

---

## What you should be able to do after Day 03

- Explain **List comprehensions** to someone else without notes.
- Explain **Dict and set comprehensions** to someone else without notes.
- Explain **Generators and yield** to someone else without notes.
- Explain **enumerate, zip and unpacking** to someone else without notes.
- Explain **map, filter and lambda** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
