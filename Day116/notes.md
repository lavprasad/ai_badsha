# Day 116 — Edge and mobile vision

Today's goal: work through **edge and mobile vision** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Latency and power constraints |
| 2 | Model choice for edge devices |
| 3 | Quantised inference |
| 4 | ONNX Runtime and TFLite |
| 5 | Camera pipeline integration |
| 6 | Batching vs streaming |
| 7 | Thermal throttling |
| 8 | On-device privacy advantages |
| 9 | Measuring real device performance |
| 10 | Deploying a detector to a Raspberry Pi |

---

## 1. Latency and power constraints

Data parallelism replicates the model and splits the batch; model parallelism splits the model when it will not fit on one device. Scale only after profiling — most 'we need more GPUs' problems are actually a slow data loader.

```python
# Effective batch = per_device_batch * n_devices * grad_accum_steps
per_device, devices, accum = 8, 4, 4
print('effective batch size', per_device * devices * accum)
print('\\nGradient accumulation gives a large effective batch on small memory:')
print('  for i, batch in enumerate(loader):')
print('      loss = model(batch).loss / accum')
print('      loss.backward()')
print('      if (i + 1) % accum == 0:')
print('          opt.step(); opt.zero_grad()')
```

**Remember:** Profile first. GPU at 30% utilisation means the bottleneck is the data pipeline, not the GPU.

**Common mistake:** Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

## 2. Model choice for edge devices

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

## 3. Quantised inference

On a device you trade accuracy for latency, memory and battery. Export to a portable runtime, quantise, and measure on the actual hardware — desktop benchmarks tell you almost nothing about a phone under thermal load.

```python
BUDGET = {'latency_ms': 100, 'model_mb': 25, 'ram_mb': 150}

candidates = [
    {'name': 'resnet50-fp32',   'latency_ms': 340, 'model_mb': 98, 'ram_mb': 420},
    {'name': 'mobilenetv3-int8','latency_ms':  38, 'model_mb':  6, 'ram_mb':  90},
    {'name': 'efficientnet-b0', 'latency_ms': 120, 'model_mb': 21, 'ram_mb': 180},
]
for c in candidates:
    fits = all(c[k] <= v for k, v in BUDGET.items())
    print(f"{c['name']:<20} {'FITS' if fits else 'over budget'}")
```

**Remember:** Measure on the target device, warm and under load — not on your laptop, once, cold.

**Common mistake:** Validating latency on a desktop GPU and discovering the phone throttles after 40 seconds.

## 4. ONNX Runtime and TFLite

Training cost is paid once; inference cost is paid on every request forever. Distillation trains a small student on the large teacher's outputs, quantisation stores weights in fewer bits, and ONNX gives you one artefact that runs across runtimes. Measure the accuracy you lose against the latency you gain.

```python
# Memory footprint by precision, for a 7B parameter model
params = 7e9
for name, bits in [('fp32', 32), ('fp16/bf16', 16), ('int8', 8), ('int4', 4)]:
    gb = params * bits / 8 / 1e9
    print(f'{name:<10} {bits:>2} bits -> {gb:6.1f} GB of weights')
print('\nPlus KV cache and activations at runtime — budget roughly 20-30% more.')
```

**Remember:** Quantise, measure quality on your own eval set, then decide. Published benchmarks are not your task.

**Common mistake:** Shipping an int4 model because it fits, without ever measuring what accuracy it cost you.

## 5. Camera pipeline integration

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

## 6. Batching vs streaming

Most training runs are not compute-bound; they are waiting on data. Before buying a bigger GPU, check utilisation: if it sits at 30%, the fix is more data-loader workers or a faster storage format. Estimate cost before starting — hours x instance price is a number you can approve or refuse.

```python
def training_estimate(samples, epochs, samples_per_sec, gpu_cost_per_hour):
    steps = samples * epochs
    hours = steps / samples_per_sec / 3600
    return {'hours': round(hours, 2), 'cost': round(hours * gpu_cost_per_hour, 2)}

print(training_estimate(samples=1_200_000, epochs=3, samples_per_sec=850, gpu_cost_per_hour=2.5))
print('If GPU utilization < 60%, fix the data pipeline before scaling hardware.')
```

**Remember:** Profile before you scale. A slow `__getitem__` wastes more money than a small GPU.

**Common mistake:** Renting four GPUs to fix a bottleneck that was a single-threaded JPEG decode.

## 7. Thermal throttling

Most training runs are not compute-bound; they are waiting on data. Before buying a bigger GPU, check utilisation: if it sits at 30%, the fix is more data-loader workers or a faster storage format. Estimate cost before starting — hours x instance price is a number you can approve or refuse.

```python
def training_estimate(samples, epochs, samples_per_sec, gpu_cost_per_hour):
    steps = samples * epochs
    hours = steps / samples_per_sec / 3600
    return {'hours': round(hours, 2), 'cost': round(hours * gpu_cost_per_hour, 2)}

print(training_estimate(samples=1_200_000, epochs=3, samples_per_sec=850, gpu_cost_per_hour=2.5))
print('If GPU utilization < 60%, fix the data pipeline before scaling hardware.')
```

**Remember:** Profile before you scale. A slow `__getitem__` wastes more money than a small GPU.

**Common mistake:** Renting four GPUs to fix a bottleneck that was a single-threaded JPEG decode.

## 8. On-device privacy advantages

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

## 9. Measuring real device performance

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

## 10. Deploying a detector to a Raspberry Pi

On a device you trade accuracy for latency, memory and battery. Export to a portable runtime, quantise, and measure on the actual hardware — desktop benchmarks tell you almost nothing about a phone under thermal load.

```python
BUDGET = {'latency_ms': 100, 'model_mb': 25, 'ram_mb': 150}

candidates = [
    {'name': 'resnet50-fp32',   'latency_ms': 340, 'model_mb': 98, 'ram_mb': 420},
    {'name': 'mobilenetv3-int8','latency_ms':  38, 'model_mb':  6, 'ram_mb':  90},
    {'name': 'efficientnet-b0', 'latency_ms': 120, 'model_mb': 21, 'ram_mb': 180},
]
for c in candidates:
    fits = all(c[k] <= v for k, v in BUDGET.items())
    print(f"{c['name']:<20} {'FITS' if fits else 'over budget'}")
```

**Remember:** Measure on the target device, warm and under load — not on your laptop, once, cold.

**Common mistake:** Validating latency on a desktop GPU and discovering the phone throttles after 40 seconds.

---

## What you should be able to do after Day 116

- Explain **Latency and power constraints** to someone else without notes.
- Explain **Model choice for edge devices** to someone else without notes.
- Explain **Quantised inference** to someone else without notes.
- Explain **ONNX Runtime and TFLite** to someone else without notes.
- Explain **Camera pipeline integration** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
