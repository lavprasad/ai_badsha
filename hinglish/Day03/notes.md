# Day 03 — Pythonic data handling

Aaj ka goal: **Pythonic data handling** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Comprehension poori list turant bana deti hai; generator ek-ek item deta hai aur puri sequence memory me kabhi nahi rakhta. RAM se badi dataset par generator hi 'chalta hai' aur 'crash' ke beech ka farq hai.

### Chhota code

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

**Yaad rakho:** Generator sirf ek baar consume hota hai — doosre pass ke liye use dobara banao.

**Aam galti:** Generator par `len()` lagana, ya do baar iterate karke doosri baar khaali paana.

Practice: `examples/01_list_comprehensions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Dict and set comprehensions

### Aasaan Bhasha

Ye wo tools hain jo haath se likhe loops ki jagah ek padhne layak line le lete hain. `Counter` ginta hai, `defaultdict` 'if key not in dict' wala natak hata deta hai, `sorted(key=...)` kisi bhi cheez se sort karta hai, aur `zip` do sequences ko saath chalata hai. Inhe uthana hi wo farq hai jo Python ko Python jaisa banata hai, translate kiye hue Java jaisa nahi.

### Chhota code

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

**Yaad rakho:** `Counter` aur `defaultdict` wo zyadatar bookkeeping code hata dete hain jo log haath se likhte hain.

**Aam galti:** Har script me hamesha ke liye `if k in d: d[k] += 1 else: d[k] = 1` se frequency counts banana.

Practice: `examples/02_dict_and_set_comprehensions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Generators and yield

### Aasaan Bhasha

Comprehension poori list turant bana deti hai; generator ek-ek item deta hai aur puri sequence memory me kabhi nahi rakhta. RAM se badi dataset par generator hi 'chalta hai' aur 'crash' ke beech ka farq hai.

### Chhota code

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

**Yaad rakho:** Generator sirf ek baar consume hota hai — doosre pass ke liye use dobara banao.

**Aam galti:** Generator par `len()` lagana, ya do baar iterate karke doosri baar khaali paana.

Practice: `examples/03_generators_and_yield.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. enumerate, zip and unpacking

### Aasaan Bhasha

Ye wo tools hain jo haath se likhe loops ki jagah ek padhne layak line le lete hain. `Counter` ginta hai, `defaultdict` 'if key not in dict' wala natak hata deta hai, `sorted(key=...)` kisi bhi cheez se sort karta hai, aur `zip` do sequences ko saath chalata hai. Inhe uthana hi wo farq hai jo Python ko Python jaisa banata hai, translate kiye hue Java jaisa nahi.

### Chhota code

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

**Yaad rakho:** `Counter` aur `defaultdict` wo zyadatar bookkeeping code hata dete hain jo log haath se likhte hain.

**Aam galti:** Har script me hamesha ke liye `if k in d: d[k] += 1 else: d[k] = 1` se frequency counts banana.

Practice: `examples/04_enumerate_zip_and_unpacking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. map, filter and lambda

### Aasaan Bhasha

Ye wo tools hain jo haath se likhe loops ki jagah ek padhne layak line le lete hain. `Counter` ginta hai, `defaultdict` 'if key not in dict' wala natak hata deta hai, `sorted(key=...)` kisi bhi cheez se sort karta hai, aur `zip` do sequences ko saath chalata hai. Inhe uthana hi wo farq hai jo Python ko Python jaisa banata hai, translate kiye hue Java jaisa nahi.

### Chhota code

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

**Yaad rakho:** `Counter` aur `defaultdict` wo zyadatar bookkeeping code hata dete hain jo log haath se likhte hain.

**Aam galti:** Har script me hamesha ke liye `if k in d: d[k] += 1 else: d[k] = 1` se frequency counts banana.

Practice: `examples/05_map_filter_and_lambda.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. sorted with key functions

### Aasaan Bhasha

Ye wo tools hain jo haath se likhe loops ki jagah ek padhne layak line le lete hain. `Counter` ginta hai, `defaultdict` 'if key not in dict' wala natak hata deta hai, `sorted(key=...)` kisi bhi cheez se sort karta hai, aur `zip` do sequences ko saath chalata hai. Inhe uthana hi wo farq hai jo Python ko Python jaisa banata hai, translate kiye hue Java jaisa nahi.

### Chhota code

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

**Yaad rakho:** `Counter` aur `defaultdict` wo zyadatar bookkeeping code hata dete hain jo log haath se likhte hain.

**Aam galti:** Har script me hamesha ke liye `if k in d: d[k] += 1 else: d[k] = 1` se frequency counts banana.

Practice: `examples/06_sorted_with_key_functions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. collections: Counter, defaultdict

### Aasaan Bhasha

Ye wo tools hain jo haath se likhe loops ki jagah ek padhne layak line le lete hain. `Counter` ginta hai, `defaultdict` 'if key not in dict' wala natak hata deta hai, `sorted(key=...)` kisi bhi cheez se sort karta hai, aur `zip` do sequences ko saath chalata hai. Inhe uthana hi wo farq hai jo Python ko Python jaisa banata hai, translate kiye hue Java jaisa nahi.

### Chhota code

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

**Yaad rakho:** `Counter` aur `defaultdict` wo zyadatar bookkeeping code hata dete hain jo log haath se likhte hain.

**Aam galti:** Har script me hamesha ke liye `if k in d: d[k] += 1 else: d[k] = 1` se frequency counts banana.

Practice: `examples/07_collections_counter_defaultdict.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. itertools for combinatorics

### Aasaan Bhasha

Ye wo tools hain jo haath se likhe loops ki jagah ek padhne layak line le lete hain. `Counter` ginta hai, `defaultdict` 'if key not in dict' wala natak hata deta hai, `sorted(key=...)` kisi bhi cheez se sort karta hai, aur `zip` do sequences ko saath chalata hai. Inhe uthana hi wo farq hai jo Python ko Python jaisa banata hai, translate kiye hue Java jaisa nahi.

### Chhota code

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

**Yaad rakho:** `Counter` aur `defaultdict` wo zyadatar bookkeeping code hata dete hain jo log haath se likhte hain.

**Aam galti:** Har script me hamesha ke liye `if k in d: d[k] += 1 else: d[k] = 1` se frequency counts banana.

Practice: `examples/08_itertools_for_combinatorics.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Lazy evaluation for big data

### Aasaan Bhasha

Comprehension poori list turant bana deti hai; generator ek-ek item deta hai aur puri sequence memory me kabhi nahi rakhta. RAM se badi dataset par generator hi 'chalta hai' aur 'crash' ke beech ka farq hai.

### Chhota code

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

**Yaad rakho:** Generator sirf ek baar consume hota hai — doosre pass ke liye use dobara banao.

**Aam galti:** Generator par `len()` lagana, ya do baar iterate karke doosri baar khaali paana.

Practice: `examples/09_lazy_evaluation_for_big_data.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Choosing the right container

### Aasaan Bhasha

Container code, dependencies aur interpreter ko package kar deta hai taaki har jagah ek jaisa chale. Versions pin karo, slim base use karo, aur bade model weights image layer se bahar rakho — unhe mount ya download karo.

### Chhota code

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

**Yaad rakho:** `--no-cache-dir` aur slim base images chhoti rakhte hain; chhoti images tez deploy hoti hain.

**Aam galti:** `pip install` se pehle `COPY . .` likhna, jisse har code edit par dependency cache toot jaata hai.

Practice: `examples/10_choosing_the_right_container.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 03 ke baad aapko ye aana chahiye

- **List comprehensions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Dict and set comprehensions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Generators and yield** ko bina notes dekhe kisi dost ko samjha sakna.
- **enumerate, zip and unpacking** ko bina notes dekhe kisi dost ko samjha sakna.
- **map, filter and lambda** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
