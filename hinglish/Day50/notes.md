# Day 50 — k-nearest neighbours

Aaj ka goal: **k-nearest neighbours** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | The idea: similarity is prediction |
| 2 | Choosing k |
| 3 | Distance metrics and weighting |
| 4 | Why scaling is mandatory |
| 5 | kNN for regression |
| 6 | Computational cost at prediction time |
| 7 | KD-trees and ball trees |
| 8 | The curse of dimensionality |
| 9 | kNN as the ancestor of vector search |
| 10 | Implementing kNN from scratch |

---

## 1. The idea: similarity is prediction

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/01_the_idea_similarity_is_prediction.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Choosing k

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/02_choosing_k.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Distance metrics and weighting

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/03_distance_metrics_and_weighting.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Why scaling is mandatory

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/04_why_scaling_is_mandatory.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. kNN for regression

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/05_knn_for_regression.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Computational cost at prediction time

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/06_computational_cost_at_prediction_time.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. KD-trees and ball trees

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/07_kd_trees_and_ball_trees.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. The curse of dimensionality

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/08_the_curse_of_dimensionality.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. kNN as the ancestor of vector search

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

Practice: `examples/09_knn_as_the_ancestor_of_vector_search.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Implementing kNN from scratch

### Aasaan Bhasha

kNN me training step hota hi nahi: ye data rakh leta hai aur prediction ke waqt k sabse paas ke points me vote karwa leta hai. Ye ek badhiya sanity baseline hai, aur vector database bhi retrieval ke liye literally yahi karta hai — samajhna do baar kaam aata hai.

### Chhota code

```python
import numpy as np

def knn_predict(X_train, y_train, x, k=3):
    d = np.linalg.norm(X_train - x, axis=1)
    idx = np.argsort(d)[:k]
    vals, counts = np.unique(y_train[idx], return_counts=True)
    return vals[np.argmax(counts)]

rng = np.random.default_rng(0)
X = rng.normal(size=(200, 2))
y = (X[:, 0] > 0).astype(int)
print('predicted', knn_predict(X, y, np.array([1.5, 0.0])), 'expected 1')
```

**Yaad rakho:** Pehle features scale karo — kNN sirf distance hai, to units hi jawab tay karti hain.

**Aam galti:** High-dimensional data par kNN, jahan har point har doosre point se lagbhag barabar door hota hai.

Practice: `examples/10_implementing_knn_from_scratch.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 50 ke baad aapko ye aana chahiye

- **The idea: similarity is prediction** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing k** ko bina notes dekhe kisi dost ko samjha sakna.
- **Distance metrics and weighting** ko bina notes dekhe kisi dost ko samjha sakna.
- **Why scaling is mandatory** ko bina notes dekhe kisi dost ko samjha sakna.
- **kNN for regression** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
