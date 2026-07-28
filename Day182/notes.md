# Day 182 — Monitoring models in production

Today's goal: work through **Monitoring models in production** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | The three things to monitor |
| 2 | Input data drift |
| 3 | Prediction drift |
| 4 | Ground truth lag |
| 5 | Population Stability Index |
| 6 | Performance monitoring when labels arrive |
| 7 | Segment-level monitoring |
| 8 | Alert thresholds without fatigue |
| 9 | Automated retraining triggers |
| 10 | An on-call runbook for a model |

---

## 1. The three things to monitor

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

## 2. Input data drift

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

## 3. Prediction drift

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

## 4. Ground truth lag

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

## 5. Population Stability Index

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

## 6. Performance monitoring when labels arrive

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

## 7. Segment-level monitoring

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

## 8. Alert thresholds without fatigue

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

## 9. Automated retraining triggers

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

## 10. An on-call runbook for a model

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

---

## What you should be able to do after Day 182

- Explain **The three things to monitor** to someone else without notes.
- Explain **Input data drift** to someone else without notes.
- Explain **Prediction drift** to someone else without notes.
- Explain **Ground truth lag** to someone else without notes.
- Explain **Population Stability Index** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
