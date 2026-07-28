# Day 178 — Containers and deployment

Today's goal: work through **Containers and deployment** — ten concepts, ten runnable examples, five questions.

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

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/01_dockerising_an_ml_service.py`, predict the output, change one line, predict again.

## 2. Layer caching for fast builds

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/02_layer_caching_for_fast_builds.py`, predict the output, change one line, predict again.

## 3. Slim base images

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/03_slim_base_images.py`, predict the output, change one line, predict again.

## 4. Handling large model artefacts

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/04_handling_large_model_artefacts.py`, predict the output, change one line, predict again.

## 5. Environment variables and secrets

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/05_environment_variables_and_secrets.py`, predict the output, change one line, predict again.

## 6. docker compose for local stacks

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/06_docker_compose_for_local_stacks.py`, predict the output, change one line, predict again.

## 7. Kubernetes concepts for ML

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/07_kubernetes_concepts_for_ml.py`, predict the output, change one line, predict again.

## 8. Autoscaling considerations

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/08_autoscaling_considerations.py`, predict the output, change one line, predict again.

## 9. GPU scheduling

GPUs win by doing thousands of multiply-adds in parallel. Model and data must live on the same device or you get an error. Mixed precision (bf16/fp16) halves memory and roughly doubles throughput on modern cards with almost no accuracy cost.

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

**Remember:** Reduce batch size first when you hit CUDA OOM; use gradient accumulation to keep the effective batch.

**Common mistake:** Keeping the full loss tensor in a list each step — it holds the whole graph and leaks memory.

Practice: open `examples/09_gpu_scheduling.py`, predict the output, change one line, predict again.

## 10. Deploying to a cloud runtime

A container packages code, dependencies and the interpreter so it runs identically everywhere. Pin your versions, use a slim base, and keep model weights out of the image layer if they are large — mount or download them instead.

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

**Remember:** `--no-cache-dir` and a slim base keep images small; small images deploy fast.

**Common mistake:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Practice: open `examples/10_deploying_to_a_cloud_runtime.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 178

- Explain **Dockerising an ML service** to someone else without notes.
- Explain **Layer caching for fast builds** to someone else without notes.
- Explain **Slim base images** to someone else without notes.
- Explain **Handling large model artefacts** to someone else without notes.
- Explain **Environment variables and secrets** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
