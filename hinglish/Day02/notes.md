# Day 02 — Python essentials refresher

Aaj ka goal: **Python essentials refresher** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Python types runtime par tay karta hai, jo likhne me tez hai aur chupke se galat karna aasan. Apne containers ki cost jaano: order ke liye list, membership ke liye set, keyed lookup ke liye dict. Truthiness `0`, `''`, `[]`, `{}` aur `None` ko false maanti hai — isiliye `if x:` aur `if x is not None:` alag sawaal hain.

### Chhota code

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Yaad rakho:** `if x:` aur `if x is not None:` 0, '' aur khaali containers par alag hain. Soch kar chuno.

**Aam galti:** Missing field check karne ke liye `if not value:` use karna aur ek jaayaz zero ko reject kar dena.

Practice: `examples/01_variables_types_and_dynamic_typing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Numbers, strings and f-strings

### Aasaan Bhasha

Python types runtime par tay karta hai, jo likhne me tez hai aur chupke se galat karna aasan. Apne containers ki cost jaano: order ke liye list, membership ke liye set, keyed lookup ke liye dict. Truthiness `0`, `''`, `[]`, `{}` aur `None` ko false maanti hai — isiliye `if x:` aur `if x is not None:` alag sawaal hain.

### Chhota code

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Yaad rakho:** `if x:` aur `if x is not None:` 0, '' aur khaali containers par alag hain. Soch kar chuno.

**Aam galti:** Missing field check karne ke liye `if not value:` use karna aur ek jaayaz zero ko reject kar dena.

Practice: `examples/02_numbers_strings_and_f_strings.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Lists, tuples, sets, dicts

### Aasaan Bhasha

Python types runtime par tay karta hai, jo likhne me tez hai aur chupke se galat karna aasan. Apne containers ki cost jaano: order ke liye list, membership ke liye set, keyed lookup ke liye dict. Truthiness `0`, `''`, `[]`, `{}` aur `None` ko false maanti hai — isiliye `if x:` aur `if x is not None:` alag sawaal hain.

### Chhota code

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Yaad rakho:** `if x:` aur `if x is not None:` 0, '' aur khaali containers par alag hain. Soch kar chuno.

**Aam galti:** Missing field check karne ke liye `if not value:` use karna aur ek jaayaz zero ko reject kar dena.

Practice: `examples/03_lists_tuples_sets_dicts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Slicing and indexing rules

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

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

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/04_slicing_and_indexing_rules.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. if/elif/else and truthiness

### Aasaan Bhasha

Python types runtime par tay karta hai, jo likhne me tez hai aur chupke se galat karna aasan. Apne containers ki cost jaano: order ke liye list, membership ke liye set, keyed lookup ke liye dict. Truthiness `0`, `''`, `[]`, `{}` aur `None` ko false maanti hai — isiliye `if x:` aur `if x is not None:` alag sawaal hain.

### Chhota code

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Yaad rakho:** `if x:` aur `if x is not None:` 0, '' aur khaali containers par alag hain. Soch kar chuno.

**Aam galti:** Missing field check karne ke liye `if not value:` use karna aur ek jaayaz zero ko reject kar dena.

Practice: `examples/05_if_elif_else_and_truthiness.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. for and while loops

### Aasaan Bhasha

Python types runtime par tay karta hai, jo likhne me tez hai aur chupke se galat karna aasan. Apne containers ki cost jaano: order ke liye list, membership ke liye set, keyed lookup ke liye dict. Truthiness `0`, `''`, `[]`, `{}` aur `None` ko false maanti hai — isiliye `if x:` aur `if x is not None:` alag sawaal hain.

### Chhota code

```python
counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)
```

**Yaad rakho:** `if x:` aur `if x is not None:` 0, '' aur khaali containers par alag hain. Soch kar chuno.

**Aam galti:** Missing field check karne ke liye `if not value:` use karna aur ek jaayaz zero ko reject kar dena.

Practice: `examples/06_for_and_while_loops.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Functions, arguments and defaults

### Aasaan Bhasha

Default arguments ek hi baar evaluate hote hain, function define hone ke waqt. Isliye mutable default (list, dict, set) har call me share hota hai — ye bug aise dikhta hai ki 'mera function pichhli call yaad rakhta hai'. `None` use karo aur asli default andar banao.

### Chhota code

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

**Yaad rakho:** Default arguments immutable hone chahiye. `None` plus ek check hi standard fix hai.

**Aam galti:** Aisa `def f(x, cache={})` jo process ki har call me chupchap state jama karta rehta hai.

Practice: `examples/07_functions_arguments_and_defaults.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Scope and the mutable default trap

### Aasaan Bhasha

Default arguments ek hi baar evaluate hote hain, function define hone ke waqt. Isliye mutable default (list, dict, set) har call me share hota hai — ye bug aise dikhta hai ki 'mera function pichhli call yaad rakhta hai'. `None` use karo aur asli default andar banao.

### Chhota code

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

**Yaad rakho:** Default arguments immutable hone chahiye. `None` plus ek check hi standard fix hai.

**Aam galti:** Aisa `def f(x, cache={})` jo process ki har call me chupchap state jama karta rehta hai.

Practice: `examples/08_scope_and_the_mutable_default_trap.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Modules, imports and __main__

### Aasaan Bhasha

Aaj ka idea — **Modules, imports and __main__** — Python essentials refresher ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Modules, imports and __main__
print("practice: Modules, imports and __main__")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Modules, imports and __main__` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Modules, imports and __main__` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/09_modules_imports_and_main.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Reading the standard library docs

### Aasaan Bhasha

Type hints runtime behaviour nahi badalte; wo ye badalte hain ki koi insaan (ya checker) function ko kitni jaldi samajhta hai. Data pipeline me signature aisi documentation hai jo purani nahi ho sakti. Chhote functions aur imaandaar naamon ke saath milao aur zyadatar comments ki zaroorat hi nahi rahegi.

### Chhota code

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

**Yaad rakho:** Boundaries par hints do (function signatures, config objects); obvious locals par chhod do.

**Aam galti:** Har cheez par annotation lagana, throwaway locals par bhi, jab tak types logic se bhaari na ho jaayein.

Practice: `examples/10_reading_the_standard_library_docs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 02 ke baad aapko ye aana chahiye

- **Variables, types and dynamic typing** ko bina notes dekhe kisi dost ko samjha sakna.
- **Numbers, strings and f-strings** ko bina notes dekhe kisi dost ko samjha sakna.
- **Lists, tuples, sets, dicts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Slicing and indexing rules** ko bina notes dekhe kisi dost ko samjha sakna.
- **if/elif/else and truthiness** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
