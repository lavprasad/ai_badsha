# Day 172 — Open source and self-hosting

Today's goal: work through **Open source and self-hosting** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Open weights vs open source |
| 2 | Licence obligations |
| 3 | Choosing an open model |
| 4 | Hardware requirements by model size |
| 5 | Serving with vLLM or TGI |
| 6 | Fine-tuning your own |
| 7 | Update and maintenance burden |
| 8 | Cost comparison with APIs |
| 9 | Data residency requirements |
| 10 | Making the build-vs-buy call |

---

## 1. Open weights vs open source

'Open weights' is not 'open source' — many licences restrict commercial use, scale, or redistribution. Self-hosting makes sense for data residency, high steady volume, or heavy customisation; APIs win on spiky traffic and zero ops. Do the arithmetic before the ideology.

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Remember:** Self-hosting costs run whether or not traffic does. Spiky workloads almost always favour an API.

**Common mistake:** Renting a GPU 24/7 for a workload that peaks for two hours a day at 8% utilisation.

Practice: open `examples/01_open_weights_vs_open_source.py`, predict the output, change one line, predict again.

## 2. Licence obligations

'Open weights' is not 'open source' — many licences restrict commercial use, scale, or redistribution. Self-hosting makes sense for data residency, high steady volume, or heavy customisation; APIs win on spiky traffic and zero ops. Do the arithmetic before the ideology.

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Remember:** Self-hosting costs run whether or not traffic does. Spiky workloads almost always favour an API.

**Common mistake:** Renting a GPU 24/7 for a workload that peaks for two hours a day at 8% utilisation.

Practice: open `examples/02_licence_obligations.py`, predict the output, change one line, predict again.

## 3. Choosing an open model

'Open weights' is not 'open source' — many licences restrict commercial use, scale, or redistribution. Self-hosting makes sense for data residency, high steady volume, or heavy customisation; APIs win on spiky traffic and zero ops. Do the arithmetic before the ideology.

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Remember:** Self-hosting costs run whether or not traffic does. Spiky workloads almost always favour an API.

**Common mistake:** Renting a GPU 24/7 for a workload that peaks for two hours a day at 8% utilisation.

Practice: open `examples/03_choosing_an_open_model.py`, predict the output, change one line, predict again.

## 4. Hardware requirements by model size

'Open weights' is not 'open source' — many licences restrict commercial use, scale, or redistribution. Self-hosting makes sense for data residency, high steady volume, or heavy customisation; APIs win on spiky traffic and zero ops. Do the arithmetic before the ideology.

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Remember:** Self-hosting costs run whether or not traffic does. Spiky workloads almost always favour an API.

**Common mistake:** Renting a GPU 24/7 for a workload that peaks for two hours a day at 8% utilisation.

Practice: open `examples/04_hardware_requirements_by_model_size.py`, predict the output, change one line, predict again.

## 5. Serving with vLLM or TGI

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

Practice: open `examples/05_serving_with_vllm_or_tgi.py`, predict the output, change one line, predict again.

## 6. Fine-tuning your own

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Practice: open `examples/06_fine_tuning_your_own.py`, predict the output, change one line, predict again.

## 7. Update and maintenance burden

Missing data is information, not just noise. Before filling anything, ask *why* it is missing: a sensor that fails only under load is not missing at random. Then choose: drop rows, drop the column, fill with a statistic, or add an explicit 'was missing' indicator column.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Remember:** Compute the fill statistic on the TRAIN split only, then apply it to test.

**Common mistake:** Filling with the mean computed over the full dataset — that leaks test information into training.

Practice: open `examples/07_update_and_maintenance_burden.py`, predict the output, change one line, predict again.

## 8. Cost comparison with APIs

'Open weights' is not 'open source' — many licences restrict commercial use, scale, or redistribution. Self-hosting makes sense for data residency, high steady volume, or heavy customisation; APIs win on spiky traffic and zero ops. Do the arithmetic before the ideology.

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Remember:** Self-hosting costs run whether or not traffic does. Spiky workloads almost always favour an API.

**Common mistake:** Renting a GPU 24/7 for a workload that peaks for two hours a day at 8% utilisation.

Practice: open `examples/08_cost_comparison_with_apis.py`, predict the output, change one line, predict again.

## 9. Data residency requirements

'Open weights' is not 'open source' — many licences restrict commercial use, scale, or redistribution. Self-hosting makes sense for data residency, high steady volume, or heavy customisation; APIs win on spiky traffic and zero ops. Do the arithmetic before the ideology.

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Remember:** Self-hosting costs run whether or not traffic does. Spiky workloads almost always favour an API.

**Common mistake:** Renting a GPU 24/7 for a workload that peaks for two hours a day at 8% utilisation.

Practice: open `examples/09_data_residency_requirements.py`, predict the output, change one line, predict again.

## 10. Making the build-vs-buy call

Projects are where the learning sticks. Build a thin end-to-end slice first — load data, train something dumb, evaluate, serve one prediction — then improve one layer at a time. A working baseline on day one beats a perfect model that never ships.

```python
STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)
```

**Remember:** Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

**Common mistake:** Six weeks of feature engineering with no baseline to prove any of it helped.

Practice: open `examples/10_making_the_build_vs_buy_call.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 172

- Explain **Open weights vs open source** to someone else without notes.
- Explain **Licence obligations** to someone else without notes.
- Explain **Choosing an open model** to someone else without notes.
- Explain **Hardware requirements by model size** to someone else without notes.
- Explain **Serving with vLLM or TGI** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
