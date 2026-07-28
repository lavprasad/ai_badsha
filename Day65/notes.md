# Day 65 — Recommender systems

Today's goal: work through **Recommender systems** — ten concepts, ten runnable examples, five questions.

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

Collaborative filtering says: people who liked what you liked also liked X. Matrix factorisation learns latent user and item vectors whose dot product predicts the rating. The cold-start problem — new users and new items with no history — is solved with content features, not more factorisation.

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

**Remember:** Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.

**Common mistake:** Building a feedback loop that only ever recommends what it already recommended.

Practice: open `examples/01_content_based_filtering.py`, predict the output, change one line, predict again.

## 2. Collaborative filtering

Collaborative filtering says: people who liked what you liked also liked X. Matrix factorisation learns latent user and item vectors whose dot product predicts the rating. The cold-start problem — new users and new items with no history — is solved with content features, not more factorisation.

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

**Remember:** Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.

**Common mistake:** Building a feedback loop that only ever recommends what it already recommended.

Practice: open `examples/02_collaborative_filtering.py`, predict the output, change one line, predict again.

## 3. User-item matrices and sparsity

Collaborative filtering says: people who liked what you liked also liked X. Matrix factorisation learns latent user and item vectors whose dot product predicts the rating. The cold-start problem — new users and new items with no history — is solved with content features, not more factorisation.

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

**Remember:** Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.

**Common mistake:** Building a feedback loop that only ever recommends what it already recommended.

Practice: open `examples/03_user_item_matrices_and_sparsity.py`, predict the output, change one line, predict again.

## 4. Matrix factorisation

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

Practice: open `examples/04_matrix_factorisation.py`, predict the output, change one line, predict again.

## 5. Implicit vs explicit feedback

Collaborative filtering says: people who liked what you liked also liked X. Matrix factorisation learns latent user and item vectors whose dot product predicts the rating. The cold-start problem — new users and new items with no history — is solved with content features, not more factorisation.

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

**Remember:** Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.

**Common mistake:** Building a feedback loop that only ever recommends what it already recommended.

Practice: open `examples/05_implicit_vs_explicit_feedback.py`, predict the output, change one line, predict again.

## 6. The cold-start problem

Collaborative filtering says: people who liked what you liked also liked X. Matrix factorisation learns latent user and item vectors whose dot product predicts the rating. The cold-start problem — new users and new items with no history — is solved with content features, not more factorisation.

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

**Remember:** Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.

**Common mistake:** Building a feedback loop that only ever recommends what it already recommended.

Practice: open `examples/06_the_cold_start_problem.py`, predict the output, change one line, predict again.

## 7. Popularity bias and feedback loops

Collaborative filtering says: people who liked what you liked also liked X. Matrix factorisation learns latent user and item vectors whose dot product predicts the rating. The cold-start problem — new users and new items with no history — is solved with content features, not more factorisation.

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

**Remember:** Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.

**Common mistake:** Building a feedback loop that only ever recommends what it already recommended.

Practice: open `examples/07_popularity_bias_and_feedback_loops.py`, predict the output, change one line, predict again.

## 8. Ranking metrics: precision@k, NDCG

Accuracy hides everything on imbalanced data. Precision asks 'of the ones I flagged, how many were real'; recall asks 'of the real ones, how many did I catch'. You trade one for the other with the threshold, and the business decides which error hurts more.

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

**Remember:** Tune the decision threshold on validation data; 0.5 is a default, not a decision.

**Common mistake:** Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

Practice: open `examples/08_ranking_metrics_precision_k_ndcg.py`, predict the output, change one line, predict again.

## 9. Candidate generation and reranking

RAG grounds answers in your documents: chunk, embed, store, retrieve the top-k for the question, and put them in the prompt. Retrieval quality is the whole ballgame — a perfect model answering from the wrong three chunks is still wrong.

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

**Remember:** Always show the source of each retrieved chunk in the answer so users can verify it.

**Common mistake:** Chunking blindly at 1000 characters and cutting tables and code blocks in half.

Practice: open `examples/09_candidate_generation_and_reranking.py`, predict the output, change one line, predict again.

## 10. A movie recommender walkthrough

Collaborative filtering says: people who liked what you liked also liked X. Matrix factorisation learns latent user and item vectors whose dot product predicts the rating. The cold-start problem — new users and new items with no history — is solved with content features, not more factorisation.

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

**Remember:** Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.

**Common mistake:** Building a feedback loop that only ever recommends what it already recommended.

Practice: open `examples/10_a_movie_recommender_walkthrough.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 65

- Explain **Content-based filtering** to someone else without notes.
- Explain **Collaborative filtering** to someone else without notes.
- Explain **User-item matrices and sparsity** to someone else without notes.
- Explain **Matrix factorisation** to someone else without notes.
- Explain **Implicit vs explicit feedback** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
