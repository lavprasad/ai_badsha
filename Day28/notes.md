# Day 28 — Discrete maths for AI

Today's goal: work through **Discrete maths for AI** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Sets, relations and functions |
| 2 | Combinatorics: permutations and combinations |
| 3 | Graphs, nodes and edges |
| 4 | Adjacency matrices |
| 5 | Trees and traversal |
| 6 | Big-O notation |
| 7 | Complexity of common ML operations |
| 8 | Recursion and dynamic programming |
| 9 | Hashing and hash collisions |
| 10 | Why complexity decides your architecture |

---

## 1. Sets, relations and functions

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 2. Combinatorics: permutations and combinations

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 3. Graphs, nodes and edges

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 4. Adjacency matrices

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 5. Trees and traversal

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 6. Big-O notation

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 7. Complexity of common ML operations

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 8. Recursion and dynamic programming

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 9. Hashing and hash collisions

Complexity decides architecture. Attention is quadratic in sequence length, kNN is linear in dataset size per query, and a hash lookup is constant. Knowing which operation dominates tells you what will break first when your data grows tenfold.

```python
import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')
```

**Remember:** Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

**Common mistake:** A membership test against a list inside a loop, turning a linear job into a quadratic one.

## 10. Why complexity decides your architecture

A transformer block is attention + feed-forward, each wrapped in a residual connection and a LayerNorm. Attention alone is order-blind, so positions are injected explicitly. Encoder-only (BERT) is for understanding, decoder-only (GPT) for generation, encoder-decoder (T5) for translation-shaped tasks.

```python
import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / np.power(10_000, (2 * (i // 2)) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe

pe = positional_encoding(6, 8)
print(pe.round(2))
print('shape', pe.shape)
```

**Remember:** Block = LayerNorm -> Attention -> add residual -> LayerNorm -> MLP -> add residual. Memorise it.

**Common mistake:** Assuming a bigger context window is free — attention cost grows with the square of sequence length.

---

## What you should be able to do after Day 28

- Explain **Sets, relations and functions** to someone else without notes.
- Explain **Combinatorics: permutations and combinations** to someone else without notes.
- Explain **Graphs, nodes and edges** to someone else without notes.
- Explain **Adjacency matrices** to someone else without notes.
- Explain **Trees and traversal** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
