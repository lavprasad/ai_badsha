# Day 35 — The machine learning problem framing

Today's goal: work through **The machine learning problem framing** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Starting from the decision, not the data |
| 2 | Supervised, unsupervised, reinforcement |
| 3 | Classification vs regression vs ranking |
| 4 | Choosing a target variable |
| 5 | Choosing an evaluation metric |
| 6 | Defining the unit of prediction |
| 7 | Baselines you must beat |
| 8 | Feasibility: is the signal even there |
| 9 | When not to use machine learning |
| 10 | Writing a one-page problem statement |

---

## 1. Starting from the decision, not the data

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

Practice: open `examples/01_starting_from_the_decision_not_the_data.py`, predict the output, change one line, predict again.

## 2. Supervised, unsupervised, reinforcement

Most failed ML projects failed at framing, not modelling. Write down: what decision changes because of this prediction, what the unit of prediction is, what metric measures success, and what the dumbest baseline scores. If a rule beats your model, ship the rule.

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Remember:** List what data exists *at prediction time* before you list features. That list kills most leaks.

**Common mistake:** Building a model for six weeks before discovering the decision it supports is already automated.

Practice: open `examples/02_supervised_unsupervised_reinforcement.py`, predict the output, change one line, predict again.

## 3. Classification vs regression vs ranking

Collaborative filtering says: people who liked what you liked also liked X. Matrix factorisation learns latent user and item vectors whose dot product predicts the rating. The cold-start problem — new users and new items with no history — is solved with content features, not more factorisation.

```python
import numpy as np

R = np.array([
    [5, 3, 0, 1],
    [4, 0, 0, 1],
    [1, 1, 0, 5],
    [0, 0, 5, 4],
], dtype=float)
mask = R > 0

rng = np.random.default_rng(0)
U, V = rng.normal(size=(4, 2)) * 0.1, rng.normal(size=(4, 2)) * 0.1
for _ in range(3000):
    err = (U @ V.T - R) * mask
    U -= 0.02 * (err @ V + 0.05 * U)
    V -= 0.02 * (err.T @ U + 0.05 * V)
print((U @ V.T).round(2))
```

**Remember:** Evaluate recommenders with ranking metrics (precision@k, NDCG), not RMSE on ratings.

**Common mistake:** Building a feedback loop that only ever recommends what it already recommended.

Practice: open `examples/03_classification_vs_regression_vs_ranking.py`, predict the output, change one line, predict again.

## 4. Choosing a target variable

Most failed ML projects failed at framing, not modelling. Write down: what decision changes because of this prediction, what the unit of prediction is, what metric measures success, and what the dumbest baseline scores. If a rule beats your model, ship the rule.

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Remember:** List what data exists *at prediction time* before you list features. That list kills most leaks.

**Common mistake:** Building a model for six weeks before discovering the decision it supports is already automated.

Practice: open `examples/04_choosing_a_target_variable.py`, predict the output, change one line, predict again.

## 5. Choosing an evaluation metric

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

Practice: open `examples/05_choosing_an_evaluation_metric.py`, predict the output, change one line, predict again.

## 6. Defining the unit of prediction

Most failed ML projects failed at framing, not modelling. Write down: what decision changes because of this prediction, what the unit of prediction is, what metric measures success, and what the dumbest baseline scores. If a rule beats your model, ship the rule.

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Remember:** List what data exists *at prediction time* before you list features. That list kills most leaks.

**Common mistake:** Building a model for six weeks before discovering the decision it supports is already automated.

Practice: open `examples/06_defining_the_unit_of_prediction.py`, predict the output, change one line, predict again.

## 7. Baselines you must beat

Most failed ML projects failed at framing, not modelling. Write down: what decision changes because of this prediction, what the unit of prediction is, what metric measures success, and what the dumbest baseline scores. If a rule beats your model, ship the rule.

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Remember:** List what data exists *at prediction time* before you list features. That list kills most leaks.

**Common mistake:** Building a model for six weeks before discovering the decision it supports is already automated.

Practice: open `examples/07_baselines_you_must_beat.py`, predict the output, change one line, predict again.

## 8. Feasibility: is the signal even there

Most failed ML projects failed at framing, not modelling. Write down: what decision changes because of this prediction, what the unit of prediction is, what metric measures success, and what the dumbest baseline scores. If a rule beats your model, ship the rule.

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Remember:** List what data exists *at prediction time* before you list features. That list kills most leaks.

**Common mistake:** Building a model for six weeks before discovering the decision it supports is already automated.

Practice: open `examples/08_feasibility_is_the_signal_even_there.py`, predict the output, change one line, predict again.

## 9. When not to use machine learning

Most failed ML projects failed at framing, not modelling. Write down: what decision changes because of this prediction, what the unit of prediction is, what metric measures success, and what the dumbest baseline scores. If a rule beats your model, ship the rule.

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Remember:** List what data exists *at prediction time* before you list features. That list kills most leaks.

**Common mistake:** Building a model for six weeks before discovering the decision it supports is already automated.

Practice: open `examples/09_when_not_to_use_machine_learning.py`, predict the output, change one line, predict again.

## 10. Writing a one-page problem statement

Most failed ML projects failed at framing, not modelling. Write down: what decision changes because of this prediction, what the unit of prediction is, what metric measures success, and what the dumbest baseline scores. If a rule beats your model, ship the rule.

```python
BRIEF = {
    'decision': 'Which support tickets get routed to the billing team',
    'unit': 'one ticket at creation time',
    'target': 'team that eventually resolved it',
    'metric': 'macro F1, because small teams matter as much as big ones',
    'baseline': 'keyword rules -> 0.61 macro F1',
    'available_at_predict_time': ['subject', 'body', 'customer_plan'],
    'not_available': ['resolution_time', 'agent_notes'],
}
for k, v in BRIEF.items():
    print(f'{k:>26}: {v}')
```

**Remember:** List what data exists *at prediction time* before you list features. That list kills most leaks.

**Common mistake:** Building a model for six weeks before discovering the decision it supports is already automated.

Practice: open `examples/10_writing_a_one_page_problem_statement.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 35

- Explain **Starting from the decision, not the data** to someone else without notes.
- Explain **Supervised, unsupervised, reinforcement** to someone else without notes.
- Explain **Classification vs regression vs ranking** to someone else without notes.
- Explain **Choosing a target variable** to someone else without notes.
- Explain **Choosing an evaluation metric** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
