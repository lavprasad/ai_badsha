# Day 178 — Containers and deployment

Aaj ka goal: **Containers and deployment** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Dockerising an ML service |
| 2 | Layer caching for fast builds |
| 3 | Slim base images |
| 4 | Handling large model artefacts |
| 5 | Environment variables and secrets |
| 6 | docker compose for local stacks |
| 7 | Kubernetes concepts for ML |
| 8 | Autoscaling considerations |
| 9 | GPU scheduling |
| 10 | Deploying to a cloud runtime |

---

## 1. Dockerising an ML service

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

Practice: `examples/01_dockerising_an_ml_service.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Layer caching for fast builds

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

Practice: `examples/02_layer_caching_for_fast_builds.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Slim base images

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

Practice: `examples/03_slim_base_images.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Handling large model artefacts

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

Practice: `examples/04_handling_large_model_artefacts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Environment variables and secrets

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

Practice: `examples/05_environment_variables_and_secrets.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. docker compose for local stacks

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

Practice: `examples/06_docker_compose_for_local_stacks.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Kubernetes concepts for ML

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

Practice: `examples/07_kubernetes_concepts_for_ml.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Autoscaling considerations

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

Practice: `examples/08_autoscaling_considerations.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. GPU scheduling

### Aasaan Bhasha

GPU isliye jeette hain kyunki wo hazaaron multiply-add saath karte hain. Model aur data ek hi device par hone chahiye warna error. Mixed precision (bf16/fp16) memory aadhi kar deta hai aur modern cards par throughput lagbhag double, accuracy me lagbhag kuch kharcha kiye bina.

### Chhota code

```python
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print('using', device)

x = torch.randn(1000, 1000, device=device)
y = x @ x.T
print(y.shape, y.device)

if device == 'cuda':
    print('allocated MB', round(torch.cuda.memory_allocated() / 1e6, 1))
```

**Yaad rakho:** CUDA OOM par sabse pehle batch size ghatao; effective batch banaye rakhne ke liye gradient accumulation use karo.

**Aam galti:** Har step ka poora loss tensor list me rakhna — wo poora graph pakde rehta hai aur memory leak karta hai.

Practice: `examples/09_gpu_scheduling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Deploying to a cloud runtime

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

Practice: `examples/10_deploying_to_a_cloud_runtime.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 178 ke baad aapko ye aana chahiye

- **Dockerising an ML service** ko bina notes dekhe kisi dost ko samjha sakna.
- **Layer caching for fast builds** ko bina notes dekhe kisi dost ko samjha sakna.
- **Slim base images** ko bina notes dekhe kisi dost ko samjha sakna.
- **Handling large model artefacts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Environment variables and secrets** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
