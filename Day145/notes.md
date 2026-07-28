# Day 145 — Small models and local AI

Today's goal: work through **Small models and local AI** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why small models matter |
| 2 | Distillation from a large teacher |
| 3 | Task-specific small models |
| 4 | Running models on a laptop |
| 5 | GGUF quantisation levels |
| 6 | Ollama and LM Studio |
| 7 | Privacy advantages of local inference |
| 8 | Latency and cost comparison |
| 9 | Quality gap by task type |
| 10 | Routing between small and large models |

---

## 1. Why small models matter

Today's idea — **Why small models matter** — sits inside the theme of Small models and local AI. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Why small models matter
print("practice: Why small models matter")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Why small models matter` makes about your data before you use it.

**Common mistake:** Copy-pasting `Why small models matter` from a tutorial without knowing what it assumes or when it fails.

## 2. Distillation from a large teacher

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

## 3. Task-specific small models

ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance. Add one behavioural test per known failure mode — a test that would have caught last quarter's outage is worth more than 90% coverage.

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Remember:** Test the data contract, not just the function — bad data breaks more models than bad code.

**Common mistake:** Testing only the happy path, so an all-null column silently trains a constant model.

## 4. Running models on a laptop

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

## 5. GGUF quantisation levels

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

## 6. Ollama and LM Studio

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

## 7. Privacy advantages of local inference

Models learn the bias in their training data and then apply it at scale with a veneer of objectivity. Measure error rates per group, not just overall. Fairness definitions genuinely conflict with each other — you must choose one explicitly and document why.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'group': ['a'] * 100 + ['b'] * 100,
    'y':     [1] * 50 + [0] * 50 + [1] * 50 + [0] * 50,
    'pred':  [1] * 45 + [0] * 55 + [1] * 30 + [0] * 70,
})
for g, sub in df.groupby('group'):
    tpr = ((sub.pred == 1) & (sub.y == 1)).sum() / max((sub.y == 1).sum(), 1)
    rate = (sub.pred == 1).mean()
    print(f'group {g}: selection rate {rate:.2f}  recall {tpr:.2f}')
print('Large gaps here are the finding — investigate before shipping.')
```

**Remember:** Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

**Common mistake:** Auditing fairness once at launch and never again as the data drifts.

## 8. Latency and cost comparison

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

## 9. Quality gap by task type

Today's idea — **Quality gap by task type** — sits inside the theme of Small models and local AI. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Quality gap by task type
print("practice: Quality gap by task type")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Quality gap by task type` makes about your data before you use it.

**Common mistake:** Copy-pasting `Quality gap by task type` from a tutorial without knowing what it assumes or when it fails.

## 10. Routing between small and large models

Today's idea — **Routing between small and large models** — sits inside the theme of Small models and local AI. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Routing between small and large models
print("practice: Routing between small and large models")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Routing between small and large models` makes about your data before you use it.

**Common mistake:** Copy-pasting `Routing between small and large models` from a tutorial without knowing what it assumes or when it fails.

---

## What you should be able to do after Day 145

- Explain **Why small models matter** to someone else without notes.
- Explain **Distillation from a large teacher** to someone else without notes.
- Explain **Task-specific small models** to someone else without notes.
- Explain **Running models on a laptop** to someone else without notes.
- Explain **GGUF quantisation levels** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
