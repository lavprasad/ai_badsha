# Day 06 — NumPy foundations

Aaj ka goal: **NumPy foundations** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Aaj ka idea — **Why NumPy is fast: contiguous memory** — NumPy foundations ke theme ke andar aata hai. Ise trivia nahi, ek tool ki tarah padho: ye kaam kya karta hai, aapke data ke baare me kya maan kar chalta hai, aur wo maanyata jhooth nikle to kya tootta hai?

### Chhota code

```python
# Explore: Why NumPy is fast: contiguous memory
print("practice: Why NumPy is fast: contiguous memory")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Yaad rakho:** `Why NumPy is fast: contiguous memory` use karne se pehle ek assumption likho jo ye aapke data ke baare me maanta hai.

**Aam galti:** `Why NumPy is fast: contiguous memory` ko tutorial se copy-paste kar lena bina jaane ki wo kya maanta hai aur kab fail hota hai.

Practice: `examples/01_why_numpy_is_fast_contiguous_memory.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Creating arrays: array, zeros, arange, linspace

### Aasaan Bhasha

NumPy ki taakat bina loops ke select aur combine karna hai. Boolean mask condition se rows chunta hai, fancy indexing position se, `np.where` condition se naya array banata hai, aur `argsort` ordering deta hai taaki aap kai arrays ko ek hi tarah sort kar sako.

### Chhota code

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

**Yaad rakho:** Boolean mask copy lautata hai; saada slice view lautata hai. Ek ko badalna doosre par ek jaisa asar nahi karta.

**Aam galti:** `arr[mask][0] = 5` chain karna aur sochna ki original array kyun nahi badla — aapne copy par likha.

Practice: `examples/02_creating_arrays_array_zeros_arange_linsp.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. dtype and memory footprint

### Aasaan Bhasha

NumPy numbers ko ek continuous typed block me rakhta hai aur loops C me chalata hai. Vectorised code (poore array par operation) aksar Python loop se 50-100x tez hota hai aur maths jaisa padhta hai. Broadcasting chhoti shapes ko bina copy kiye stretch kar deta hai.

### Chhota code

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
print(a.shape, a.dtype)

b = np.array([10, 20, 30])       # shape (3,)
print(a + b)                     # broadcast over rows

print(a.sum(axis=0))             # column sums
print(a.sum(axis=1))             # row sums
```

**Yaad rakho:** `axis=0` rows ko collapse karta hai (columns ke neeche); `axis=1` columns ko (ek row ke aar-paar).

**Aam galti:** Python loop me array elements ghumana, vectorised operation use karne ke bajaye.

Practice: `examples/03_dtype_and_memory_footprint.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Shape, reshape and ravel

### Aasaan Bhasha

Agar aap decision samjha nahi sakte, to aap use defend bhi nahi kar sakte — aur credit, hiring aur healthcare me ye legally zaroori hai. Permutation importance model-agnostic aur imaandaar hai. SHAP per-prediction attributions deta hai theoretical base ke saath par sach me compute maangta hai.

### Chhota code

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

**Yaad rakho:** TEST set par permutation importance batati hai ki generalise karne ke liye model kis par tik raha hai.

**Aam galti:** Importance ko causation ki tarah pesh karna — model ne correlation dhoonda hai, bas.

Practice: `examples/04_shape_reshape_and_ravel.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Indexing, slicing and views vs copies

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

Practice: `examples/05_indexing_slicing_and_views_vs_copies.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Boolean masking

### Aasaan Bhasha

NumPy ki taakat bina loops ke select aur combine karna hai. Boolean mask condition se rows chunta hai, fancy indexing position se, `np.where` condition se naya array banata hai, aur `argsort` ordering deta hai taaki aap kai arrays ko ek hi tarah sort kar sako.

### Chhota code

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

**Yaad rakho:** Boolean mask copy lautata hai; saada slice view lautata hai. Ek ko badalna doosre par ek jaisa asar nahi karta.

**Aam galti:** `arr[mask][0] = 5` chain karna aur sochna ki original array kyun nahi badla — aapne copy par likha.

Practice: `examples/06_boolean_masking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Fancy indexing

### Aasaan Bhasha

NumPy ki taakat bina loops ke select aur combine karna hai. Boolean mask condition se rows chunta hai, fancy indexing position se, `np.where` condition se naya array banata hai, aur `argsort` ordering deta hai taaki aap kai arrays ko ek hi tarah sort kar sako.

### Chhota code

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

**Yaad rakho:** Boolean mask copy lautata hai; saada slice view lautata hai. Ek ko badalna doosre par ek jaisa asar nahi karta.

**Aam galti:** `arr[mask][0] = 5` chain karna aur sochna ki original array kyun nahi badla — aapne copy par likha.

Practice: `examples/07_fancy_indexing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Vectorisation vs Python loops

### Aasaan Bhasha

NumPy numbers ko ek continuous typed block me rakhta hai aur loops C me chalata hai. Vectorised code (poore array par operation) aksar Python loop se 50-100x tez hota hai aur maths jaisa padhta hai. Broadcasting chhoti shapes ko bina copy kiye stretch kar deta hai.

### Chhota code

```python
import numpy as np

a = np.arange(6).reshape(2, 3)
print(a.shape, a.dtype)

b = np.array([10, 20, 30])       # shape (3,)
print(a + b)                     # broadcast over rows

print(a.sum(axis=0))             # column sums
print(a.sum(axis=1))             # row sums
```

**Yaad rakho:** `axis=0` rows ko collapse karta hai (columns ke neeche); `axis=1` columns ko (ek row ke aar-paar).

**Aam galti:** Python loop me array elements ghumana, vectorised operation use karne ke bajaye.

Practice: `examples/08_vectorisation_vs_python_loops.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Random numbers with default_rng

### Aasaan Bhasha

NumPy ki taakat bina loops ke select aur combine karna hai. Boolean mask condition se rows chunta hai, fancy indexing position se, `np.where` condition se naya array banata hai, aur `argsort` ordering deta hai taaki aap kai arrays ko ek hi tarah sort kar sako.

### Chhota code

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

**Yaad rakho:** Boolean mask copy lautata hai; saada slice view lautata hai. Ek ko badalna doosre par ek jaisa asar nahi karta.

**Aam galti:** `arr[mask][0] = 5` chain karna aur sochna ki original array kyun nahi badla — aapne copy par likha.

Practice: `examples/09_random_numbers_with_default_rng.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Timing a vectorised speedup

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/10_timing_a_vectorised_speedup.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 06 ke baad aapko ye aana chahiye

- **Why NumPy is fast: contiguous memory** ko bina notes dekhe kisi dost ko samjha sakna.
- **Creating arrays: array, zeros, arange, linspace** ko bina notes dekhe kisi dost ko samjha sakna.
- **dtype and memory footprint** ko bina notes dekhe kisi dost ko samjha sakna.
- **Shape, reshape and ravel** ko bina notes dekhe kisi dost ko samjha sakna.
- **Indexing, slicing and views vs copies** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
