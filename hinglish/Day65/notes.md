# Day 65 — Recommender systems

Aaj ka goal: **Recommender systems** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Content-based filtering |
| 2 | Collaborative filtering |
| 3 | User-item matrices and sparsity |
| 4 | Matrix factorisation |
| 5 | Implicit vs explicit feedback |
| 6 | The cold-start problem |
| 7 | Popularity bias and feedback loops |
| 8 | Ranking metrics: precision@k, NDCG |
| 9 | Candidate generation and reranking |
| 10 | A movie recommender walkthrough |

---

## 1. Content-based filtering

### Aasaan Bhasha

Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.

### Chhota code

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Yaad rakho:** Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.

**Aam galti:** Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.

Practice: `examples/01_content_based_filtering.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Collaborative filtering

### Aasaan Bhasha

Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.

### Chhota code

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Yaad rakho:** Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.

**Aam galti:** Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.

Practice: `examples/02_collaborative_filtering.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. User-item matrices and sparsity

### Aasaan Bhasha

Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.

### Chhota code

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Yaad rakho:** Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.

**Aam galti:** Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.

Practice: `examples/03_user_item_matrices_and_sparsity.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Matrix factorisation

### Aasaan Bhasha

Matrix ek linear transformation hai. Matrices ko multiply karna transformations ko jodta hai — neural network ki layers stack karna bilkul yahi hai. Shapes milni chahiye: (m,k) @ (k,n) -> (m,n); andar wale dimensions match hone chahiye aur wahi gayab ho jaate hain.

### Chhota code

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))
```

**Yaad rakho:** Har shape error ko 'andar wale dimensions match nahi hue' padho aur shapes print kar do.

**Aam galti:** `Ax=b` solve karne ke liye `np.linalg.inv` uthana, jabki `np.linalg.solve` zyada safe hai.

Practice: `examples/04_matrix_factorisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Implicit vs explicit feedback

### Aasaan Bhasha

Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.

### Chhota code

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Yaad rakho:** Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.

**Aam galti:** Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.

Practice: `examples/05_implicit_vs_explicit_feedback.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. The cold-start problem

### Aasaan Bhasha

Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.

### Chhota code

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Yaad rakho:** Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.

**Aam galti:** Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.

Practice: `examples/06_the_cold_start_problem.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Popularity bias and feedback loops

### Aasaan Bhasha

Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.

### Chhota code

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Yaad rakho:** Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.

**Aam galti:** Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.

Practice: `examples/07_popularity_bias_and_feedback_loops.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Ranking metrics: precision@k, NDCG

### Aasaan Bhasha

Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.

### Chhota code

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Yaad rakho:** Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.

**Aam galti:** Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.

Practice: `examples/08_ranking_metrics_precision_k_ndcg.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Candidate generation and reranking

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

```python
import numpy as np

docs = [
    'Refunds are processed within 5 business days.',
    'Our office is in Pune, open 9am to 6pm.',
    'Enterprise plans include a dedicated support engineer.',
]

def fake_embed(text):                       # stand-in for a real embedding model
    rng = np.random.default_rng(abs(hash(text)) % (2 ** 32))
    v = rng.normal(size=32)
    return v / np.linalg.norm(v)

index = np.array([fake_embed(d) for d in docs])
q = fake_embed('how long do refunds take')
top = int(np.argmax(index @ q))
print('retrieved:', docs[top])
print('\\nReal pipeline: chunk 300-800 tokens with overlap -> embed -> ANN index -> rerank -> prompt.')
```

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/09_candidate_generation_and_reranking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A movie recommender walkthrough

### Aasaan Bhasha

Collaborative filtering kehta hai: jinhe wo pasand aaya jo aapko pasand aaya, unhe X bhi pasand aaya. Matrix factorisation latent user aur item vectors seekhta hai jinka dot product rating predict karta hai. Cold-start problem — naye users aur naye items bina history ke — content features se hal hoti hai, aur factorisation se nahi.

### Chhota code

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Yaad rakho:** Recommenders ko ranking metrics (precision@k, NDCG) se evaluate karo, ratings par RMSE se nahi.

**Aam galti:** Aisa feedback loop banana jo hamesha wahi recommend karta hai jo pehle se recommend kar raha tha.

Practice: `examples/10_a_movie_recommender_walkthrough.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 65 ke baad aapko ye aana chahiye

- **Content-based filtering** ko bina notes dekhe kisi dost ko samjha sakna.
- **Collaborative filtering** ko bina notes dekhe kisi dost ko samjha sakna.
- **User-item matrices and sparsity** ko bina notes dekhe kisi dost ko samjha sakna.
- **Matrix factorisation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Implicit vs explicit feedback** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
