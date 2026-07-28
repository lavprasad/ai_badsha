# Day 118 — Vision system design

Today's goal: work through **Vision system design** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Requirements: accuracy, latency, cost |
| 2 | Data collection plan |
| 3 | Annotation strategy and quality control |
| 4 | Choosing the model family |
| 5 | Handling class imbalance in vision |
| 6 | Monitoring in production |
| 7 | Human-in-the-loop review |
| 8 | Failure modes and fallbacks |
| 9 | Cost per inference |
| 10 | Writing the system design document |

---

## 1. Requirements: accuracy, latency, cost

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

Practice: open `examples/01_requirements_accuracy_latency_cost.py`, predict the output, change one line, predict again.

## 2. Data collection plan

A system design document forces the questions that kill projects late: where does the data come from, what happens when the model is unsure, who reviews it, what does one inference cost, and what happens when the service is down. Write it before the first training run.

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Remember:** The fallback path must handle 100% of traffic. If it cannot, you have built a single point of failure.

**Common mistake:** Designing for the happy path and discovering at 3am there is no route for low-confidence cases.

Practice: open `examples/02_data_collection_plan.py`, predict the output, change one line, predict again.

## 3. Annotation strategy and quality control

A system design document forces the questions that kill projects late: where does the data come from, what happens when the model is unsure, who reviews it, what does one inference cost, and what happens when the service is down. Write it before the first training run.

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Remember:** The fallback path must handle 100% of traffic. If it cannot, you have built a single point of failure.

**Common mistake:** Designing for the happy path and discovering at 3am there is no route for low-confidence cases.

Practice: open `examples/03_annotation_strategy_and_quality_control.py`, predict the output, change one line, predict again.

## 4. Choosing the model family

A system design document forces the questions that kill projects late: where does the data come from, what happens when the model is unsure, who reviews it, what does one inference cost, and what happens when the service is down. Write it before the first training run.

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Remember:** The fallback path must handle 100% of traffic. If it cannot, you have built a single point of failure.

**Common mistake:** Designing for the happy path and discovering at 3am there is no route for low-confidence cases.

Practice: open `examples/04_choosing_the_model_family.py`, predict the output, change one line, predict again.

## 5. Handling class imbalance in vision

Today's idea — **Handling class imbalance in vision** — sits inside the theme of Vision system design. Read it as a tool, not trivia: what job does it do, what does it assume about your data, and what breaks when that assumption is false?

```python
# Explore: Handling class imbalance in vision
print("practice: Handling class imbalance in vision")

# Write three lines here that make the idea concrete on data you already have.
# If you cannot, you have not understood it yet — go back to the notes.
```

**Remember:** State one assumption `Handling class imbalance in vision` makes about your data before you use it.

**Common mistake:** Copy-pasting `Handling class imbalance in vision` from a tutorial without knowing what it assumes or when it fails.

Practice: open `examples/05_handling_class_imbalance_in_vision.py`, predict the output, change one line, predict again.

## 6. Monitoring in production

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

Practice: open `examples/06_monitoring_in_production.py`, predict the output, change one line, predict again.

## 7. Human-in-the-loop review

A system design document forces the questions that kill projects late: where does the data come from, what happens when the model is unsure, who reviews it, what does one inference cost, and what happens when the service is down. Write it before the first training run.

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Remember:** The fallback path must handle 100% of traffic. If it cannot, you have built a single point of failure.

**Common mistake:** Designing for the happy path and discovering at 3am there is no route for low-confidence cases.

Practice: open `examples/07_human_in_the_loop_review.py`, predict the output, change one line, predict again.

## 8. Failure modes and fallbacks

A system design document forces the questions that kill projects late: where does the data come from, what happens when the model is unsure, who reviews it, what does one inference cost, and what happens when the service is down. Write it before the first training run.

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Remember:** The fallback path must handle 100% of traffic. If it cannot, you have built a single point of failure.

**Common mistake:** Designing for the happy path and discovering at 3am there is no route for low-confidence cases.

Practice: open `examples/08_failure_modes_and_fallbacks.py`, predict the output, change one line, predict again.

## 9. Cost per inference

A system design document forces the questions that kill projects late: where does the data come from, what happens when the model is unsure, who reviews it, what does one inference cost, and what happens when the service is down. Write it before the first training run.

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Remember:** The fallback path must handle 100% of traffic. If it cannot, you have built a single point of failure.

**Common mistake:** Designing for the happy path and discovering at 3am there is no route for low-confidence cases.

Practice: open `examples/09_cost_per_inference.py`, predict the output, change one line, predict again.

## 10. Writing the system design document

A system design document forces the questions that kill projects late: where does the data come from, what happens when the model is unsure, who reviews it, what does one inference cost, and what happens when the service is down. Write it before the first training run.

```python
DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')
```

**Remember:** The fallback path must handle 100% of traffic. If it cannot, you have built a single point of failure.

**Common mistake:** Designing for the happy path and discovering at 3am there is no route for low-confidence cases.

Practice: open `examples/10_writing_the_system_design_document.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 118

- Explain **Requirements: accuracy, latency, cost** to someone else without notes.
- Explain **Data collection plan** to someone else without notes.
- Explain **Annotation strategy and quality control** to someone else without notes.
- Explain **Choosing the model family** to someone else without notes.
- Explain **Handling class imbalance in vision** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
