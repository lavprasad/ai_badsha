# Day 172 — Open source and self-hosting

Aaj ka goal: **Open source and self-hosting** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

'Open weights' matlab 'open source' nahi — kai licences commercial use, scale ya redistribution par rok lagate hain. Self-hosting tab sahi hai jab data residency, oonchi steady volume, ya bhaari customisation ho; APIs spiky traffic aur zero ops par jeette hain. Ideology se pehle ganit karo.

### Chhota code

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Yaad rakho:** Self-hosting ki cost tab bhi chalti hai jab traffic nahi chalta. Spiky workloads lagbhag hamesha API ke haq me hote hain.

**Aam galti:** 24/7 GPU kiraye par lena aise workload ke liye jo din me do ghante 8% utilisation par peak karta hai.

Practice: `examples/01_open_weights_vs_open_source.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Licence obligations

### Aasaan Bhasha

'Open weights' matlab 'open source' nahi — kai licences commercial use, scale ya redistribution par rok lagate hain. Self-hosting tab sahi hai jab data residency, oonchi steady volume, ya bhaari customisation ho; APIs spiky traffic aur zero ops par jeette hain. Ideology se pehle ganit karo.

### Chhota code

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Yaad rakho:** Self-hosting ki cost tab bhi chalti hai jab traffic nahi chalta. Spiky workloads lagbhag hamesha API ke haq me hote hain.

**Aam galti:** 24/7 GPU kiraye par lena aise workload ke liye jo din me do ghante 8% utilisation par peak karta hai.

Practice: `examples/02_licence_obligations.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Choosing an open model

### Aasaan Bhasha

'Open weights' matlab 'open source' nahi — kai licences commercial use, scale ya redistribution par rok lagate hain. Self-hosting tab sahi hai jab data residency, oonchi steady volume, ya bhaari customisation ho; APIs spiky traffic aur zero ops par jeette hain. Ideology se pehle ganit karo.

### Chhota code

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Yaad rakho:** Self-hosting ki cost tab bhi chalti hai jab traffic nahi chalta. Spiky workloads lagbhag hamesha API ke haq me hote hain.

**Aam galti:** 24/7 GPU kiraye par lena aise workload ke liye jo din me do ghante 8% utilisation par peak karta hai.

Practice: `examples/03_choosing_an_open_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Hardware requirements by model size

### Aasaan Bhasha

'Open weights' matlab 'open source' nahi — kai licences commercial use, scale ya redistribution par rok lagate hain. Self-hosting tab sahi hai jab data residency, oonchi steady volume, ya bhaari customisation ho; APIs spiky traffic aur zero ops par jeette hain. Ideology se pehle ganit karo.

### Chhota code

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Yaad rakho:** Self-hosting ki cost tab bhi chalti hai jab traffic nahi chalta. Spiky workloads lagbhag hamesha API ke haq me hote hain.

**Aam galti:** 24/7 GPU kiraye par lena aise workload ke liye jo din me do ghante 8% utilisation par peak karta hai.

Practice: `examples/04_hardware_requirements_by_model_size.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Serving with vLLM or TGI

### Aasaan Bhasha

Model serve karna matlab use startup par ek baar load karna aur HTTP requests ka jawab dena. Input schema validate karo, errors structured JSON me lautao, health endpoint jodo, aur model ko request handler ke andar kabhi load mat karo.

### Chhota code

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

**Yaad rakho:** Jahan latency ijaazat de wahan requests batch karo — batch size 1 par GPU throughput dhah jaata hai.

**Aam galti:** Har request par model dobara load karna aur sochna ki p99 latency chaar second kyun hai.

Practice: `examples/05_serving_with_vllm_or_tgi.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Fine-tuning your own

### Aasaan Bhasha

Hyperparameters wo settings hain jo aap chunte ho, seekhi nahi jaatin. Grid search poora chhaanta hai aur barbaad karta hai; random search high dimensions me acche ilaake jaldi dhoondta hai; Bayesian search pichhle trials se seekhta hai. Search hamesha cross-validation ke andar karo.

### Chhota code

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

**Yaad rakho:** Random seed fix karo aur har trial log karo, warna aap apna hi best model dobara nahi bana paoge.

**Aam galti:** 400 rows par 40 hyperparameters tune karna — ab aap validation set hi fit kar rahe ho.

Practice: `examples/06_fine_tuning_your_own.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Update and maintenance burden

### Aasaan Bhasha

Missing data information hai, sirf noise nahi. Kuch bharne se pehle poochho ki **kyun** missing hai: jo sensor sirf load par fail hota hai wo randomly missing nahi hai. Phir chuno: rows drop, column drop, statistic se fill, ya ek explicit 'ye missing tha' indicator column.

### Chhota code

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Yaad rakho:** Fill karne wali statistic sirf TRAIN split par nikalo, phir test par lagao.

**Aam galti:** Poore dataset ke mean se fill karna — ye test ki information training me leak kar deta hai.

Practice: `examples/07_update_and_maintenance_burden.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Cost comparison with APIs

### Aasaan Bhasha

'Open weights' matlab 'open source' nahi — kai licences commercial use, scale ya redistribution par rok lagate hain. Self-hosting tab sahi hai jab data residency, oonchi steady volume, ya bhaari customisation ho; APIs spiky traffic aur zero ops par jeette hain. Ideology se pehle ganit karo.

### Chhota code

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Yaad rakho:** Self-hosting ki cost tab bhi chalti hai jab traffic nahi chalta. Spiky workloads lagbhag hamesha API ke haq me hote hain.

**Aam galti:** 24/7 GPU kiraye par lena aise workload ke liye jo din me do ghante 8% utilisation par peak karta hai.

Practice: `examples/08_cost_comparison_with_apis.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Data residency requirements

### Aasaan Bhasha

'Open weights' matlab 'open source' nahi — kai licences commercial use, scale ya redistribution par rok lagate hain. Self-hosting tab sahi hai jab data residency, oonchi steady volume, ya bhaari customisation ho; APIs spiky traffic aur zero ops par jeette hain. Ideology se pehle ganit karo.

### Chhota code

```python
def monthly_comparison(requests, tokens_per_req, api_price_per_mtok, gpu_hourly, gpu_util):
    api = requests * tokens_per_req / 1e6 * api_price_per_mtok
    self_host = gpu_hourly * 24 * 30 / max(gpu_util, 0.01)
    return {'api': round(api), 'self_hosted': round(self_host)}

for reqs in (50_000, 2_000_000, 20_000_000):
    print(f'{reqs:>10,} req/mo ->', monthly_comparison(reqs, 1200, 3.0, 2.5, 1.0))
```

**Yaad rakho:** Self-hosting ki cost tab bhi chalti hai jab traffic nahi chalta. Spiky workloads lagbhag hamesha API ke haq me hote hain.

**Aam galti:** 24/7 GPU kiraye par lena aise workload ke liye jo din me do ghante 8% utilisation par peak karta hai.

Practice: `examples/09_data_residency_requirements.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Making the build-vs-buy call

### Aasaan Bhasha

Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.

### Chhota code

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

**Yaad rakho:** Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.

**Aam galti:** Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.

Practice: `examples/10_making_the_build_vs_buy_call.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 172 ke baad aapko ye aana chahiye

- **Open weights vs open source** ko bina notes dekhe kisi dost ko samjha sakna.
- **Licence obligations** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing an open model** ko bina notes dekhe kisi dost ko samjha sakna.
- **Hardware requirements by model size** ko bina notes dekhe kisi dost ko samjha sakna.
- **Serving with vLLM or TGI** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
