# Day 101 — Model compression

Today's goal: work through **Model compression** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why inference cost matters more than training cost |
| 2 | Quantisation: int8 and int4 |
| 3 | Post-training vs quantisation-aware training |
| 4 | Pruning: structured and unstructured |
| 5 | Knowledge distillation |
| 6 | Low-rank factorisation |
| 7 | Operator fusion |
| 8 | ONNX and runtime portability |
| 9 | Measuring the accuracy/latency trade-off |
| 10 | Shrinking a model for edge deployment |

---

## 1. Why inference cost matters more than training cost

Temperature 0 is near-deterministic and right for extraction; higher values add diversity for creative work. Top-p keeps the smallest set of tokens covering p of the probability mass. Cost is per token in and out, so trimming the prompt is the cheapest optimisation there is.

```python
import numpy as np

def sample(logits, temperature=1.0, top_p=0.9, seed=0):
    z = np.array(logits) / max(temperature, 1e-6)
    p = np.exp(z - z.max())
    p /= p.sum()
    order = np.argsort(-p)
    keep = order[:max(1, int(np.searchsorted(np.cumsum(p[order]), top_p) + 1))]
    p2 = p[keep] / p[keep].sum()
    return int(np.random.default_rng(seed).choice(keep, p=p2))

logits = [3.0, 2.0, 1.0, 0.5]
print('greedy-ish (T=0.1):', sample(logits, temperature=0.1))
print('creative  (T=1.5):', sample(logits, temperature=1.5, seed=3))
```

**Remember:** Use temperature 0 for anything you will parse; save randomness for prose.

**Common mistake:** Running extraction at temperature 1 and debugging 'random' JSON failures for a week.

## 2. Quantisation: int8 and int4

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

## 3. Post-training vs quantisation-aware training

LoRA freezes the base weights and trains two small low-rank matrices whose product is added to each target layer. You update ~0.1% of the parameters, the checkpoint is megabytes not gigabytes, and you can swap adapters per customer. QLoRA adds 4-bit base weights so a 7B model fits on one consumer GPU.

```python
import numpy as np

d, r = 512, 8                      # full dim vs LoRA rank
rng = np.random.default_rng(0)
W = rng.normal(size=(d, d)) * 0.02  # frozen base weight
A = rng.normal(size=(d, r)) * 0.01  # trainable
B = np.zeros((r, d))                # trainable, starts at zero -> no change at step 0

delta = A @ B
print('base params   ', W.size)
print('lora params   ', A.size + B.size, f'({100 * (A.size + B.size) / W.size:.1f}%)')
print('effective W = W + A@B, shape', (W + delta).shape)
```

**Remember:** Initialise B to zeros so the adapted model starts exactly equal to the base model.

**Common mistake:** Setting rank far too high — you lose the efficiency and gain the overfitting.

## 4. Pruning: structured and unstructured

A tree asks yes/no questions, splitting to make each side purer. It needs no scaling, handles mixed types, and reads like a flowchart. Left unconstrained it memorises the training set perfectly, so depth and leaf-size limits are mandatory.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Remember:** A single unpruned tree is almost always worse than a small forest — but it is readable, which sometimes wins.

**Common mistake:** Trusting a deep tree's feature importances; they are unstable and biased toward high-cardinality columns.

## 5. Knowledge distillation

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

## 6. Low-rank factorisation

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

## 7. Operator fusion

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

## 8. ONNX and runtime portability

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

## 9. Measuring the accuracy/latency trade-off

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

## 10. Shrinking a model for edge deployment

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

---

## What you should be able to do after Day 101

- Explain **Why inference cost matters more than training cost** to someone else without notes.
- Explain **Quantisation: int8 and int4** to someone else without notes.
- Explain **Post-training vs quantisation-aware training** to someone else without notes.
- Explain **Pruning: structured and unstructured** to someone else without notes.
- Explain **Knowledge distillation** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
