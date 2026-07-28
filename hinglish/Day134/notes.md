# Day 134 — Serving LLMs efficiently

Aaj ka goal: **Serving LLMs efficiently** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Prefill vs decode phases |
| 2 | KV cache memory maths |
| 3 | Continuous batching |
| 4 | PagedAttention and vLLM |
| 5 | Quantised inference: GPTQ, AWQ, GGUF |
| 6 | Speculative decoding |
| 7 | Throughput vs latency trade-offs |
| 8 | Cost per million tokens |
| 9 | Local models with llama.cpp and Ollama |
| 10 | Choosing hosted vs self-hosted |

---

## 1. Prefill vs decode phases

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

Practice: `examples/01_prefill_vs_decode_phases.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. KV cache memory maths

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

Practice: `examples/02_kv_cache_memory_maths.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Continuous batching

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

Practice: `examples/03_continuous_batching.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. PagedAttention and vLLM

### Aasaan Bhasha

Attention har token ko har doosre token ko dekh kar tay karne deta hai ki kya important hai. Har token ek query, ek key aur ek value deta hai; query-key dot products values par weights ban jaate hain. Multiple heads model ko ek saath kai rishton par dhyaan dene dete hain.

### Chhota code

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Yaad rakho:** 1/sqrt(d) wala scale sajावat nahi hai — uske bina softmax saturate ho jaata hai aur gradients mar jaate hain.

**Aam galti:** Decoder me causal mask chhod dena, jisse model agla token padh kar aasani se cheating kar leta hai.

Practice: `examples/04_pagedattention_and_vllm.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Quantised inference: GPTQ, AWQ, GGUF

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

Practice: `examples/05_quantised_inference_gptq_awq_gguf.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Speculative decoding

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

Practice: `examples/06_speculative_decoding.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Throughput vs latency trade-offs

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

Practice: `examples/07_throughput_vs_latency_trade_offs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Cost per million tokens

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

Practice: `examples/08_cost_per_million_tokens.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Local models with llama.cpp and Ollama

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

Practice: `examples/09_local_models_with_llama_cpp_and_ollama.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Choosing hosted vs self-hosted

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

Practice: `examples/10_choosing_hosted_vs_self_hosted.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 134 ke baad aapko ye aana chahiye

- **Prefill vs decode phases** ko bina notes dekhe kisi dost ko samjha sakna.
- **KV cache memory maths** ko bina notes dekhe kisi dost ko samjha sakna.
- **Continuous batching** ko bina notes dekhe kisi dost ko samjha sakna.
- **PagedAttention and vLLM** ko bina notes dekhe kisi dost ko samjha sakna.
- **Quantised inference: GPTQ, AWQ, GGUF** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
