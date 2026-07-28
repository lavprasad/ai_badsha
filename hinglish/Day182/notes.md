# Day 182 — Monitoring models in production

Aaj ka goal: **Monitoring models in production** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/01_the_three_things_to_monitor.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Input data drift

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/02_input_data_drift.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Prediction drift

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/03_prediction_drift.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Ground truth lag

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/04_ground_truth_lag.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Population Stability Index

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/05_population_stability_index.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Performance monitoring when labels arrive

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/06_performance_monitoring_when_labels_arriv.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Segment-level monitoring

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/07_segment_level_monitoring.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Alert thresholds without fatigue

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/08_alert_thresholds_without_fatigue.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Automated retraining triggers

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/09_automated_retraining_triggers.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. An on-call runbook for a model

### Aasaan Bhasha

Models sadte hain. Duniya badalti hai, inputs shift hote hain (data drift) ya rishta hi badal jaata hai (concept drift). Input aur prediction distributions roz monitor karo, kyunki ground-truth labels aksar hafton baad aate hain.

### Chhota code

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

**Yaad rakho:** PSI 0.1 se kam stable, 0.1-0.2 nazar rakho, 0.2 se upar jaanch karo. Prediction distribution par bhi alert lagao.

**Aam galti:** Sirf uptime monitor karna, jisse 200 OK lautaata hua bilkul galat model bhi healthy dikhta hai.

Practice: `examples/10_an_on_call_runbook_for_a_model.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 182 ke baad aapko ye aana chahiye

- **The three things to monitor** ko bina notes dekhe kisi dost ko samjha sakna.
- **Input data drift** ko bina notes dekhe kisi dost ko samjha sakna.
- **Prediction drift** ko bina notes dekhe kisi dost ko samjha sakna.
- **Ground truth lag** ko bina notes dekhe kisi dost ko samjha sakna.
- **Population Stability Index** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
