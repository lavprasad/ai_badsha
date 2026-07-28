# Day 149 — PROJECT: fine-tuned domain assistant

Today's goal: work through **PROJECT: fine-tuned domain assistant** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Goal: a small model specialised to one task |
| 2 | Collecting and curating examples |
| 3 | Formatting an SFT dataset |
| 4 | Choosing base model and LoRA settings |
| 5 | Training run and monitoring |
| 6 | Evaluating against the base model |
| 7 | Comparing against a prompted large model |
| 8 | Cost and latency comparison |
| 9 | Deciding whether tuning was worth it |
| 10 | Packaging the adapter |

---

## 1. Goal: a small model specialised to one task

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

Practice: open `examples/01_goal_a_small_model_specialised_to_one_ta.py`, predict the output, change one line, predict again.

## 2. Collecting and curating examples

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

Practice: open `examples/02_collecting_and_curating_examples.py`, predict the output, change one line, predict again.

## 3. Formatting an SFT dataset

Fine-tuning continues training a pretrained model on your examples. It teaches format, tone and task shape far better than it teaches new facts — for facts, use retrieval. A few hundred excellent examples usually beat ten thousand mediocre ones.

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Remember:** Fine-tune for behaviour and format. Use RAG for knowledge that changes.

**Common mistake:** Fine-tuning to inject company facts, then re-training every time a policy document changes.

Practice: open `examples/03_formatting_an_sft_dataset.py`, predict the output, change one line, predict again.

## 4. Choosing base model and LoRA settings

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

Practice: open `examples/04_choosing_base_model_and_lora_settings.py`, predict the output, change one line, predict again.

## 5. Training run and monitoring

Models rot. The world moves, inputs shift (data drift) or the relationship itself changes (concept drift). Monitor input distributions and prediction distributions daily, because ground-truth labels usually arrive weeks late.

```python
import numpy as np

def psi(expected, actual, bins=10):
    """Population Stability Index: >0.2 means investigate."""
    edges = np.percentile(expected, np.linspace(0, 100, bins + 1))
    edges[0], edges[-1] = -np.inf, np.inf
    e = np.histogram(expected, edges)[0] / len(expected) + 1e-6
    a = np.histogram(actual, edges)[0] / len(actual) + 1e-6
    return float(np.sum((a - e) * np.log(a / e)))

rng = np.random.default_rng(0)
baseline = rng.normal(0, 1, 10_000)
print('same dist  PSI', round(psi(baseline, rng.normal(0, 1, 5_000)), 4))
print('shifted    PSI', round(psi(baseline, rng.normal(0.6, 1.2, 5_000)), 4))
```

**Remember:** PSI under 0.1 stable, 0.1-0.2 watch, above 0.2 investigate. Alert on the prediction distribution too.

**Common mistake:** Only monitoring uptime, so a model that returns 200 OK while being badly wrong looks healthy.

Practice: open `examples/05_training_run_and_monitoring.py`, predict the output, change one line, predict again.

## 6. Evaluating against the base model

Vibes do not survive a prompt change. Build a small golden set of real inputs with expected outputs, run it on every change, and track the score. Use an LLM judge for open-ended quality, but calibrate the judge against human ratings first.

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Remember:** 50 real examples you curated beat 5000 synthetic ones nobody checked.

**Common mistake:** Changing the prompt on Friday with no eval and finding out from customers on Monday.

Practice: open `examples/06_evaluating_against_the_base_model.py`, predict the output, change one line, predict again.

## 7. Comparing against a prompted large model

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

Practice: open `examples/07_comparing_against_a_prompted_large_model.py`, predict the output, change one line, predict again.

## 8. Cost and latency comparison

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

Practice: open `examples/08_cost_and_latency_comparison.py`, predict the output, change one line, predict again.

## 9. Deciding whether tuning was worth it

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

Practice: open `examples/09_deciding_whether_tuning_was_worth_it.py`, predict the output, change one line, predict again.

## 10. Packaging the adapter

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

Practice: open `examples/10_packaging_the_adapter.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 149

- Explain **Goal: a small model specialised to one task** to someone else without notes.
- Explain **Collecting and curating examples** to someone else without notes.
- Explain **Formatting an SFT dataset** to someone else without notes.
- Explain **Choosing base model and LoRA settings** to someone else without notes.
- Explain **Training run and monitoring** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
