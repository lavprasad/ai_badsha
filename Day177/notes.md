# Day 177 — Model serving

Today's goal: work through **Model serving** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Batch vs online inference |
| 2 | REST APIs with FastAPI |
| 3 | Input validation with Pydantic |
| 4 | Loading models at startup |
| 5 | Concurrency and worker processes |
| 6 | Request batching for GPUs |
| 7 | Health and readiness endpoints |
| 8 | Versioned endpoints |
| 9 | Graceful shutdown |
| 10 | Load testing your endpoint |

---

## 1. Batch vs online inference

Serving a model means loading it once at startup and answering HTTP requests. Validate the input schema, return errors as structured JSON, add a health endpoint, and never load the model inside the request handler.

```python
# pip install fastapi uvicorn ; run: uvicorn app:app --reload
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
#
# app = FastAPI()
# model = joblib.load('model.joblib')      # once, at startup
#
# class Req(BaseModel):
#     features: list[float]
#
# @app.get('/health')
# def health():
#     return {'ok': True}
#
# @app.post('/predict')
# def predict(req: Req):
#     return {'prediction': float(model.predict([req.features])[0])}
print('Load once at startup; validate with a schema; expose /health for the load balancer.')
```

**Remember:** Batch requests where latency allows — GPU throughput collapses on batch size 1.

**Common mistake:** Reloading the model per request and wondering why p99 latency is four seconds.

## 2. REST APIs with FastAPI

Serving a model means loading it once at startup and answering HTTP requests. Validate the input schema, return errors as structured JSON, add a health endpoint, and never load the model inside the request handler.

```python
# pip install fastapi uvicorn ; run: uvicorn app:app --reload
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
#
# app = FastAPI()
# model = joblib.load('model.joblib')      # once, at startup
#
# class Req(BaseModel):
#     features: list[float]
#
# @app.get('/health')
# def health():
#     return {'ok': True}
#
# @app.post('/predict')
# def predict(req: Req):
#     return {'prediction': float(model.predict([req.features])[0])}
print('Load once at startup; validate with a schema; expose /health for the load balancer.')
```

**Remember:** Batch requests where latency allows — GPU throughput collapses on batch size 1.

**Common mistake:** Reloading the model per request and wondering why p99 latency is four seconds.

## 3. Input validation with Pydantic

Serving a model means loading it once at startup and answering HTTP requests. Validate the input schema, return errors as structured JSON, add a health endpoint, and never load the model inside the request handler.

```python
# pip install fastapi uvicorn ; run: uvicorn app:app --reload
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
#
# app = FastAPI()
# model = joblib.load('model.joblib')      # once, at startup
#
# class Req(BaseModel):
#     features: list[float]
#
# @app.get('/health')
# def health():
#     return {'ok': True}
#
# @app.post('/predict')
# def predict(req: Req):
#     return {'prediction': float(model.predict([req.features])[0])}
print('Load once at startup; validate with a schema; expose /health for the load balancer.')
```

**Remember:** Batch requests where latency allows — GPU throughput collapses on batch size 1.

**Common mistake:** Reloading the model per request and wondering why p99 latency is four seconds.

## 4. Loading models at startup

Serving a model means loading it once at startup and answering HTTP requests. Validate the input schema, return errors as structured JSON, add a health endpoint, and never load the model inside the request handler.

```python
# pip install fastapi uvicorn ; run: uvicorn app:app --reload
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
#
# app = FastAPI()
# model = joblib.load('model.joblib')      # once, at startup
#
# class Req(BaseModel):
#     features: list[float]
#
# @app.get('/health')
# def health():
#     return {'ok': True}
#
# @app.post('/predict')
# def predict(req: Req):
#     return {'prediction': float(model.predict([req.features])[0])}
print('Load once at startup; validate with a schema; expose /health for the load balancer.')
```

**Remember:** Batch requests where latency allows — GPU throughput collapses on batch size 1.

**Common mistake:** Reloading the model per request and wondering why p99 latency is four seconds.

## 5. Concurrency and worker processes

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

## 6. Request batching for GPUs

Serving a model means loading it once at startup and answering HTTP requests. Validate the input schema, return errors as structured JSON, add a health endpoint, and never load the model inside the request handler.

```python
# pip install fastapi uvicorn ; run: uvicorn app:app --reload
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
#
# app = FastAPI()
# model = joblib.load('model.joblib')      # once, at startup
#
# class Req(BaseModel):
#     features: list[float]
#
# @app.get('/health')
# def health():
#     return {'ok': True}
#
# @app.post('/predict')
# def predict(req: Req):
#     return {'prediction': float(model.predict([req.features])[0])}
print('Load once at startup; validate with a schema; expose /health for the load balancer.')
```

**Remember:** Batch requests where latency allows — GPU throughput collapses on batch size 1.

**Common mistake:** Reloading the model per request and wondering why p99 latency is four seconds.

## 7. Health and readiness endpoints

After supervised tuning, models are aligned to human preference. RLHF trains a reward model on human comparisons, then optimises against it with PPO. DPO skips the reward model and optimises preference pairs directly — simpler, cheaper, and now the common choice.

```python
import numpy as np

# DPO intuition: raise logprob of the chosen reply relative to the rejected one,
# while a KL term keeps you near the reference model.
policy = {'chosen': -2.0, 'rejected': -2.5}     # log-probs under the trained model
ref = {'chosen': -2.4, 'rejected': -2.3}        # log-probs under the frozen reference
beta = 0.1

margin = beta * ((policy['chosen'] - ref['chosen']) - (policy['rejected'] - ref['rejected']))
loss = -np.log(1 / (1 + np.exp(-margin)))
print(f'margin {margin:.4f}  dpo loss {loss:.4f}')
```

**Remember:** Alignment optimises a proxy for what humans want; the proxy can always be gamed.

**Common mistake:** Over-optimising the reward model until outputs are sycophantic and useless — classic reward hacking.

## 8. Versioned endpoints

After supervised tuning, models are aligned to human preference. RLHF trains a reward model on human comparisons, then optimises against it with PPO. DPO skips the reward model and optimises preference pairs directly — simpler, cheaper, and now the common choice.

```python
import numpy as np

# DPO intuition: raise logprob of the chosen reply relative to the rejected one,
# while a KL term keeps you near the reference model.
policy = {'chosen': -2.0, 'rejected': -2.5}     # log-probs under the trained model
ref = {'chosen': -2.4, 'rejected': -2.3}        # log-probs under the frozen reference
beta = 0.1

margin = beta * ((policy['chosen'] - ref['chosen']) - (policy['rejected'] - ref['rejected']))
loss = -np.log(1 / (1 + np.exp(-margin)))
print(f'margin {margin:.4f}  dpo loss {loss:.4f}')
```

**Remember:** Alignment optimises a proxy for what humans want; the proxy can always be gamed.

**Common mistake:** Over-optimising the reward model until outputs are sycophantic and useless — classic reward hacking.

## 9. Graceful shutdown

Serving a model means loading it once at startup and answering HTTP requests. Validate the input schema, return errors as structured JSON, add a health endpoint, and never load the model inside the request handler.

```python
# pip install fastapi uvicorn ; run: uvicorn app:app --reload
# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
#
# app = FastAPI()
# model = joblib.load('model.joblib')      # once, at startup
#
# class Req(BaseModel):
#     features: list[float]
#
# @app.get('/health')
# def health():
#     return {'ok': True}
#
# @app.post('/predict')
# def predict(req: Req):
#     return {'prediction': float(model.predict([req.features])[0])}
print('Load once at startup; validate with a schema; expose /health for the load balancer.')
```

**Remember:** Batch requests where latency allows — GPU throughput collapses on batch size 1.

**Common mistake:** Reloading the model per request and wondering why p99 latency is four seconds.

## 10. Load testing your endpoint

After supervised tuning, models are aligned to human preference. RLHF trains a reward model on human comparisons, then optimises against it with PPO. DPO skips the reward model and optimises preference pairs directly — simpler, cheaper, and now the common choice.

```python
import numpy as np

# DPO intuition: raise logprob of the chosen reply relative to the rejected one,
# while a KL term keeps you near the reference model.
policy = {'chosen': -2.0, 'rejected': -2.5}     # log-probs under the trained model
ref = {'chosen': -2.4, 'rejected': -2.3}        # log-probs under the frozen reference
beta = 0.1

margin = beta * ((policy['chosen'] - ref['chosen']) - (policy['rejected'] - ref['rejected']))
loss = -np.log(1 / (1 + np.exp(-margin)))
print(f'margin {margin:.4f}  dpo loss {loss:.4f}')
```

**Remember:** Alignment optimises a proxy for what humans want; the proxy can always be gamed.

**Common mistake:** Over-optimising the reward model until outputs are sycophantic and useless — classic reward hacking.

---

## What you should be able to do after Day 177

- Explain **Batch vs online inference** to someone else without notes.
- Explain **REST APIs with FastAPI** to someone else without notes.
- Explain **Input validation with Pydantic** to someone else without notes.
- Explain **Loading models at startup** to someone else without notes.
- Explain **Concurrency and worker processes** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
