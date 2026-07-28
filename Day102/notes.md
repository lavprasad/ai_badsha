# Day 102 — Hardware and performance

Today's goal: work through **Hardware and performance** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | CPU vs GPU vs TPU |
| 2 | Memory bandwidth as the real bottleneck |
| 3 | Batch size and utilisation |
| 4 | Mixed precision: fp16 and bf16 |
| 5 | Gradient checkpointing |
| 6 | Profiling a training run |
| 7 | Data loading bottlenecks |
| 8 | Multi-GPU data parallelism |
| 9 | Model and pipeline parallelism |
| 10 | Estimating training cost before you start |

---

## 1. CPU vs GPU vs TPU

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

Practice: open `examples/01_cpu_vs_gpu_vs_tpu.py`, predict the output, change one line, predict again.

## 2. Memory bandwidth as the real bottleneck

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

Practice: open `examples/02_memory_bandwidth_as_the_real_bottleneck.py`, predict the output, change one line, predict again.

## 3. Batch size and utilisation

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

Practice: open `examples/03_batch_size_and_utilisation.py`, predict the output, change one line, predict again.

## 4. Mixed precision: fp16 and bf16

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

Practice: open `examples/04_mixed_precision_fp16_and_bf16.py`, predict the output, change one line, predict again.

## 5. Gradient checkpointing

The derivative answers: if I nudge this input a little, how much does the output move? The gradient is that answer for every input at once, so it points uphill. Training walks downhill by stepping against the gradient. The chain rule is what lets you propagate that answer through a stack of layers.

```python
import numpy as np

def f(x):
    return x ** 2 + 3 * x

def numeric_grad(fn, x, h=1e-6):
    return (fn(x + h) - fn(x - h)) / (2 * h)

x = 2.0
print('numeric  ', numeric_grad(f, x))
print('analytic ', 2 * x + 3)   # should match to ~1e-6
```

**Remember:** A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

**Common mistake:** Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

Practice: open `examples/05_gradient_checkpointing.py`, predict the output, change one line, predict again.

## 6. Profiling a training run

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

Practice: open `examples/06_profiling_a_training_run.py`, predict the output, change one line, predict again.

## 7. Data loading bottlenecks

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

Practice: open `examples/07_data_loading_bottlenecks.py`, predict the output, change one line, predict again.

## 8. Multi-GPU data parallelism

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

Practice: open `examples/08_multi_gpu_data_parallelism.py`, predict the output, change one line, predict again.

## 9. Model and pipeline parallelism

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

Practice: open `examples/09_model_and_pipeline_parallelism.py`, predict the output, change one line, predict again.

## 10. Estimating training cost before you start

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

Practice: open `examples/10_estimating_training_cost_before_you_star.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 102

- Explain **CPU vs GPU vs TPU** to someone else without notes.
- Explain **Memory bandwidth as the real bottleneck** to someone else without notes.
- Explain **Batch size and utilisation** to someone else without notes.
- Explain **Mixed precision: fp16 and bf16** to someone else without notes.
- Explain **Gradient checkpointing** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
