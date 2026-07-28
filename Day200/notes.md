# Day 200 — Day 200: the road ahead

Today's goal: work through **Day 200: the road ahead** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | What 200 days actually gave you |
| 2 | Auditing your own gaps honestly |
| 3 | The fundamentals that will not expire |
| 4 | The tools that will expire |
| 5 | Choosing a specialisation |
| 6 | Building in public |
| 7 | Contributing to open source AI |
| 8 | Mentoring someone behind you |
| 9 | Ethics as an ongoing practice |
| 10 | Your next 200 days |

---

## 1. What 200 days actually gave you

The frameworks in this course will change; the fundamentals will not. Linear algebra, probability, honest evaluation, leakage, and knowing what your data can and cannot support outlive every library. Audit yourself against those, not against the tool list.

```python
DURABLE = ['linear algebra', 'probability and statistics', 'optimisation',
           'honest evaluation and splits', 'leakage detection', 'error analysis',
           'problem framing', 'writing clearly']
EXPIRING = ['this version of the framework API', 'today\'s best model name',
            'current pricing', 'the fashionable agent library']

print('Invest here (10-year shelf life):')
for d in DURABLE:
    print('  +', d)
print('\nLearn just-in-time (18-month shelf life):')
for e in EXPIRING:
    print('  -', e)
```

**Remember:** Rebuild one project from Day 1 knowledge at the end. The gap between the two versions is your progress.

**Common mistake:** Measuring your skill by the number of tools you have touched rather than problems you have solved.

Practice: open `examples/01_what_200_days_actually_gave_you.py`, predict the output, change one line, predict again.

## 2. Auditing your own gaps honestly

The frameworks in this course will change; the fundamentals will not. Linear algebra, probability, honest evaluation, leakage, and knowing what your data can and cannot support outlive every library. Audit yourself against those, not against the tool list.

```python
DURABLE = ['linear algebra', 'probability and statistics', 'optimisation',
           'honest evaluation and splits', 'leakage detection', 'error analysis',
           'problem framing', 'writing clearly']
EXPIRING = ['this version of the framework API', 'today\'s best model name',
            'current pricing', 'the fashionable agent library']

print('Invest here (10-year shelf life):')
for d in DURABLE:
    print('  +', d)
print('\nLearn just-in-time (18-month shelf life):')
for e in EXPIRING:
    print('  -', e)
```

**Remember:** Rebuild one project from Day 1 knowledge at the end. The gap between the two versions is your progress.

**Common mistake:** Measuring your skill by the number of tools you have touched rather than problems you have solved.

Practice: open `examples/02_auditing_your_own_gaps_honestly.py`, predict the output, change one line, predict again.

## 3. The fundamentals that will not expire

The frameworks in this course will change; the fundamentals will not. Linear algebra, probability, honest evaluation, leakage, and knowing what your data can and cannot support outlive every library. Audit yourself against those, not against the tool list.

```python
DURABLE = ['linear algebra', 'probability and statistics', 'optimisation',
           'honest evaluation and splits', 'leakage detection', 'error analysis',
           'problem framing', 'writing clearly']
EXPIRING = ['this version of the framework API', 'today\'s best model name',
            'current pricing', 'the fashionable agent library']

print('Invest here (10-year shelf life):')
for d in DURABLE:
    print('  +', d)
print('\nLearn just-in-time (18-month shelf life):')
for e in EXPIRING:
    print('  -', e)
```

**Remember:** Rebuild one project from Day 1 knowledge at the end. The gap between the two versions is your progress.

**Common mistake:** Measuring your skill by the number of tools you have touched rather than problems you have solved.

Practice: open `examples/03_the_fundamentals_that_will_not_expire.py`, predict the output, change one line, predict again.

## 4. The tools that will expire

The frameworks in this course will change; the fundamentals will not. Linear algebra, probability, honest evaluation, leakage, and knowing what your data can and cannot support outlive every library. Audit yourself against those, not against the tool list.

```python
DURABLE = ['linear algebra', 'probability and statistics', 'optimisation',
           'honest evaluation and splits', 'leakage detection', 'error analysis',
           'problem framing', 'writing clearly']
EXPIRING = ['this version of the framework API', 'today\'s best model name',
            'current pricing', 'the fashionable agent library']

print('Invest here (10-year shelf life):')
for d in DURABLE:
    print('  +', d)
print('\nLearn just-in-time (18-month shelf life):')
for e in EXPIRING:
    print('  -', e)
```

**Remember:** Rebuild one project from Day 1 knowledge at the end. The gap between the two versions is your progress.

**Common mistake:** Measuring your skill by the number of tools you have touched rather than problems you have solved.

Practice: open `examples/04_the_tools_that_will_expire.py`, predict the output, change one line, predict again.

## 5. Choosing a specialisation

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

Practice: open `examples/05_choosing_a_specialisation.py`, predict the output, change one line, predict again.

## 6. Building in public

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

Practice: open `examples/06_building_in_public.py`, predict the output, change one line, predict again.

## 7. Contributing to open source AI

The frameworks in this course will change; the fundamentals will not. Linear algebra, probability, honest evaluation, leakage, and knowing what your data can and cannot support outlive every library. Audit yourself against those, not against the tool list.

```python
DURABLE = ['linear algebra', 'probability and statistics', 'optimisation',
           'honest evaluation and splits', 'leakage detection', 'error analysis',
           'problem framing', 'writing clearly']
EXPIRING = ['this version of the framework API', 'today\'s best model name',
            'current pricing', 'the fashionable agent library']

print('Invest here (10-year shelf life):')
for d in DURABLE:
    print('  +', d)
print('\nLearn just-in-time (18-month shelf life):')
for e in EXPIRING:
    print('  -', e)
```

**Remember:** Rebuild one project from Day 1 knowledge at the end. The gap between the two versions is your progress.

**Common mistake:** Measuring your skill by the number of tools you have touched rather than problems you have solved.

Practice: open `examples/07_contributing_to_open_source_ai.py`, predict the output, change one line, predict again.

## 8. Mentoring someone behind you

The frameworks in this course will change; the fundamentals will not. Linear algebra, probability, honest evaluation, leakage, and knowing what your data can and cannot support outlive every library. Audit yourself against those, not against the tool list.

```python
DURABLE = ['linear algebra', 'probability and statistics', 'optimisation',
           'honest evaluation and splits', 'leakage detection', 'error analysis',
           'problem framing', 'writing clearly']
EXPIRING = ['this version of the framework API', 'today\'s best model name',
            'current pricing', 'the fashionable agent library']

print('Invest here (10-year shelf life):')
for d in DURABLE:
    print('  +', d)
print('\nLearn just-in-time (18-month shelf life):')
for e in EXPIRING:
    print('  -', e)
```

**Remember:** Rebuild one project from Day 1 knowledge at the end. The gap between the two versions is your progress.

**Common mistake:** Measuring your skill by the number of tools you have touched rather than problems you have solved.

Practice: open `examples/08_mentoring_someone_behind_you.py`, predict the output, change one line, predict again.

## 9. Ethics as an ongoing practice

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

Practice: open `examples/09_ethics_as_an_ongoing_practice.py`, predict the output, change one line, predict again.

## 10. Your next 200 days

The frameworks in this course will change; the fundamentals will not. Linear algebra, probability, honest evaluation, leakage, and knowing what your data can and cannot support outlive every library. Audit yourself against those, not against the tool list.

```python
DURABLE = ['linear algebra', 'probability and statistics', 'optimisation',
           'honest evaluation and splits', 'leakage detection', 'error analysis',
           'problem framing', 'writing clearly']
EXPIRING = ['this version of the framework API', 'today\'s best model name',
            'current pricing', 'the fashionable agent library']

print('Invest here (10-year shelf life):')
for d in DURABLE:
    print('  +', d)
print('\nLearn just-in-time (18-month shelf life):')
for e in EXPIRING:
    print('  -', e)
```

**Remember:** Rebuild one project from Day 1 knowledge at the end. The gap between the two versions is your progress.

**Common mistake:** Measuring your skill by the number of tools you have touched rather than problems you have solved.

Practice: open `examples/10_your_next_200_days.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 200

- Explain **What 200 days actually gave you** to someone else without notes.
- Explain **Auditing your own gaps honestly** to someone else without notes.
- Explain **The fundamentals that will not expire** to someone else without notes.
- Explain **The tools that will expire** to someone else without notes.
- Explain **Choosing a specialisation** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
