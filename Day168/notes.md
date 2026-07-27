# Day 168 — Data flywheels

Today's goal: work through **data flywheels** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Capturing user feedback |
| 2 | Implicit signals: edits, retries, abandonment |
| 3 | Building a labelling loop |
| 4 | Active learning: label what is uncertain |
| 5 | Turning corrections into eval cases |
| 6 | Retraining and re-prompting cadence |
| 7 | Avoiding feedback loop bias |
| 8 | Privacy constraints on user data |
| 9 | Measuring flywheel velocity |
| 10 | Designing the loop from day one |

---

## 1. Capturing user feedback

The examples your model gets wrong are the most valuable training data you will ever have, and they are free — if you capture them. Log inputs, outputs and corrections from day one; retrofitting a feedback loop after launch means starting from zero.

```python
import numpy as np

def select_for_labelling(probs, budget=5):
    """Label where the model is least certain — uncertainty sampling."""
    margin = np.abs(probs - 0.5)
    return np.argsort(margin)[:budget]

rng = np.random.default_rng(0)
probs = rng.random(20)
pick = select_for_labelling(probs)
print('label these rows first:', pick)
print('their probabilities    :', probs[pick].round(3))
print('\n50 uncertain labels beat 5000 random ones.')
```

**Remember:** Capture the correction, not just the thumbs-down. 'What should it have said' is the training signal.

**Common mistake:** Shipping without logging, then having no data to improve on after three months of traffic.

## 2. Implicit signals: edits, retries, abandonment

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

## 3. Building a labelling loop

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

## 4. Active learning: label what is uncertain

The examples your model gets wrong are the most valuable training data you will ever have, and they are free — if you capture them. Log inputs, outputs and corrections from day one; retrofitting a feedback loop after launch means starting from zero.

```python
import numpy as np

def select_for_labelling(probs, budget=5):
    """Label where the model is least certain — uncertainty sampling."""
    margin = np.abs(probs - 0.5)
    return np.argsort(margin)[:budget]

rng = np.random.default_rng(0)
probs = rng.random(20)
pick = select_for_labelling(probs)
print('label these rows first:', pick)
print('their probabilities    :', probs[pick].round(3))
print('\n50 uncertain labels beat 5000 random ones.')
```

**Remember:** Capture the correction, not just the thumbs-down. 'What should it have said' is the training signal.

**Common mistake:** Shipping without logging, then having no data to improve on after three months of traffic.

## 5. Turning corrections into eval cases

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

## 6. Retraining and re-prompting cadence

A prompt is a program written in English. Be specific about role, task, format and constraints. Few-shot examples teach format better than any description. Asking for reasoning steps helps on multi-step problems and wastes tokens on simple lookups.

```python
prompt = '''You are a support triage assistant.

Classify the ticket into exactly one of: BILLING, BUG, FEATURE, OTHER.
Return JSON only: {"label": ..., "confidence": 0.0-1.0}

Examples:
Ticket: "charged twice this month" -> {"label": "BILLING", "confidence": 0.95}
Ticket: "app crashes on upload"    -> {"label": "BUG", "confidence": 0.92}

Ticket: "can you add dark mode?"
'''
print(prompt)
print('Structure: role -> task -> allowed outputs -> format -> examples -> input.')
```

**Remember:** Put the output format last and show it as an example — models copy the nearest pattern.

**Common mistake:** Writing a vague prompt, getting vague output, and blaming the model.

## 7. Avoiding feedback loop bias

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

## 8. Privacy constraints on user data

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

## 9. Measuring flywheel velocity

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

## 10. Designing the loop from day one

The examples your model gets wrong are the most valuable training data you will ever have, and they are free — if you capture them. Log inputs, outputs and corrections from day one; retrofitting a feedback loop after launch means starting from zero.

```python
import numpy as np

def select_for_labelling(probs, budget=5):
    """Label where the model is least certain — uncertainty sampling."""
    margin = np.abs(probs - 0.5)
    return np.argsort(margin)[:budget]

rng = np.random.default_rng(0)
probs = rng.random(20)
pick = select_for_labelling(probs)
print('label these rows first:', pick)
print('their probabilities    :', probs[pick].round(3))
print('\n50 uncertain labels beat 5000 random ones.')
```

**Remember:** Capture the correction, not just the thumbs-down. 'What should it have said' is the training signal.

**Common mistake:** Shipping without logging, then having no data to improve on after three months of traffic.

---

## What you should be able to do after Day 168

- Explain **Capturing user feedback** to someone else without notes.
- Explain **Implicit signals: edits, retries, abandonment** to someone else without notes.
- Explain **Building a labelling loop** to someone else without notes.
- Explain **Active learning: label what is uncertain** to someone else without notes.
- Explain **Turning corrections into eval cases** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
