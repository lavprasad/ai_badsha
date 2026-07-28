# Day 150 — Designing with LLMs

Today's goal: work through **Designing with LLMs** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | What LLMs are good and bad at |
| 2 | Choosing between rules, ML and LLMs |
| 3 | Task decomposition |
| 4 | Deterministic scaffolding around a stochastic core |
| 5 | Where to put validation |
| 6 | Failure budgets |
| 7 | Human-in-the-loop design |
| 8 | Cost modelling before building |
| 9 | Latency budgets |
| 10 | Writing an LLM system design doc |

---

## 1. What LLMs are good and bad at

Put the stochastic part in the smallest possible box. Deterministic code should decide what to call, validate what comes back, and enforce permissions; the model should do the fuzzy language work in between. Every boundary between them is a place to validate.

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Remember:** The model proposes; your code disposes. Never let model output be the last check before an action.

**Common mistake:** Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Practice: open `examples/01_what_llms_are_good_and_bad_at.py`, predict the output, change one line, predict again.

## 2. Choosing between rules, ML and LLMs

Put the stochastic part in the smallest possible box. Deterministic code should decide what to call, validate what comes back, and enforce permissions; the model should do the fuzzy language work in between. Every boundary between them is a place to validate.

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Remember:** The model proposes; your code disposes. Never let model output be the last check before an action.

**Common mistake:** Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Practice: open `examples/02_choosing_between_rules_ml_and_llms.py`, predict the output, change one line, predict again.

## 3. Task decomposition

Eigenvectors are the directions a matrix only stretches, never rotates; the eigenvalue is the stretch factor. SVD generalises this to any matrix and is the engine under PCA, low-rank compression, and LoRA adapters.

```python
import numpy as np

X = np.random.default_rng(0).normal(size=(100, 5))
U, S, Vt = np.linalg.svd(X, full_matrices=False)
print('singular values', np.round(S, 2))

energy = np.cumsum(S ** 2) / np.sum(S ** 2)
print('variance kept by first 2 dims:', round(float(energy[1]), 3))
```

**Remember:** Singular values sorted descending tell you how many dimensions actually carry information.

**Common mistake:** Running PCA/SVD on unscaled features so the largest-unit column dominates every component.

Practice: open `examples/03_task_decomposition.py`, predict the output, change one line, predict again.

## 4. Deterministic scaffolding around a stochastic core

Put the stochastic part in the smallest possible box. Deterministic code should decide what to call, validate what comes back, and enforce permissions; the model should do the fuzzy language work in between. Every boundary between them is a place to validate.

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Remember:** The model proposes; your code disposes. Never let model output be the last check before an action.

**Common mistake:** Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Practice: open `examples/04_deterministic_scaffolding_around_a_stoch.py`, predict the output, change one line, predict again.

## 5. Where to put validation

Put the stochastic part in the smallest possible box. Deterministic code should decide what to call, validate what comes back, and enforce permissions; the model should do the fuzzy language work in between. Every boundary between them is a place to validate.

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Remember:** The model proposes; your code disposes. Never let model output be the last check before an action.

**Common mistake:** Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Practice: open `examples/05_where_to_put_validation.py`, predict the output, change one line, predict again.

## 6. Failure budgets

Put the stochastic part in the smallest possible box. Deterministic code should decide what to call, validate what comes back, and enforce permissions; the model should do the fuzzy language work in between. Every boundary between them is a place to validate.

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Remember:** The model proposes; your code disposes. Never let model output be the last check before an action.

**Common mistake:** Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Practice: open `examples/06_failure_budgets.py`, predict the output, change one line, predict again.

## 7. Human-in-the-loop design

Put the stochastic part in the smallest possible box. Deterministic code should decide what to call, validate what comes back, and enforce permissions; the model should do the fuzzy language work in between. Every boundary between them is a place to validate.

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Remember:** The model proposes; your code disposes. Never let model output be the last check before an action.

**Common mistake:** Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Practice: open `examples/07_human_in_the_loop_design.py`, predict the output, change one line, predict again.

## 8. Cost modelling before building

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

Practice: open `examples/08_cost_modelling_before_building.py`, predict the output, change one line, predict again.

## 9. Latency budgets

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

Practice: open `examples/09_latency_budgets.py`, predict the output, change one line, predict again.

## 10. Writing an LLM system design doc

Put the stochastic part in the smallest possible box. Deterministic code should decide what to call, validate what comes back, and enforce permissions; the model should do the fuzzy language work in between. Every boundary between them is a place to validate.

```python
def extract_and_act(text, model_call, db):
    raw = model_call(text)                       # 1. fuzzy: model reads language
    try:                                          # 2. deterministic: validate
        amount = float(raw['amount'])
        account = str(raw['account'])
    except (KeyError, ValueError, TypeError):
        return {'status': 'rejected', 'reason': 'unparseable model output'}
    if not 0 < amount <= 10_000:                  # 3. deterministic: business rules
        return {'status': 'escalate', 'reason': 'amount outside auto-approve band'}
    return {'status': 'approved', 'account': account, 'amount': amount}

print(extract_and_act('refund 500', lambda t: {'amount': '500', 'account': 'A-1'}, db=None))
print(extract_and_act('refund lots', lambda t: {'amount': '99000', 'account': 'A-1'}, db=None))
```

**Remember:** The model proposes; your code disposes. Never let model output be the last check before an action.

**Common mistake:** Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Practice: open `examples/10_writing_an_llm_system_design_doc.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 150

- Explain **What LLMs are good and bad at** to someone else without notes.
- Explain **Choosing between rules, ML and LLMs** to someone else without notes.
- Explain **Task decomposition** to someone else without notes.
- Explain **Deterministic scaffolding around a stochastic core** to someone else without notes.
- Explain **Where to put validation** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
