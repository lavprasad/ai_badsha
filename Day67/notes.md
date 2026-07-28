# Day 67 — Survival and duration models

Today's goal: work through **Survival and duration models** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Time-to-event framing |
| 2 | Censoring |
| 3 | Kaplan-Meier curves |
| 4 | Hazard functions |
| 5 | Cox proportional hazards |
| 6 | Churn as a survival problem |
| 7 | Features that change over time |
| 8 | Evaluating survival models |
| 9 | Business use: retention and maintenance |
| 10 | When plain classification is enough |

---

## 1. Time-to-event framing

Survival analysis answers 'how long until the event' when some subjects have not had it yet — that is censoring, and throwing those rows away biases everything. Churn, machine failure and time-to-conversion are all survival problems people usually mis-model as classification.

```python
import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)
```

**Remember:** A censored row still carries information: it survived at least that long. Never drop it.

**Common mistake:** Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.

Practice: open `examples/01_time_to_event_framing.py`, predict the output, change one line, predict again.

## 2. Censoring

Survival analysis answers 'how long until the event' when some subjects have not had it yet — that is censoring, and throwing those rows away biases everything. Churn, machine failure and time-to-conversion are all survival problems people usually mis-model as classification.

```python
import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)
```

**Remember:** A censored row still carries information: it survived at least that long. Never drop it.

**Common mistake:** Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.

Practice: open `examples/02_censoring.py`, predict the output, change one line, predict again.

## 3. Kaplan-Meier curves

Survival analysis answers 'how long until the event' when some subjects have not had it yet — that is censoring, and throwing those rows away biases everything. Churn, machine failure and time-to-conversion are all survival problems people usually mis-model as classification.

```python
import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)
```

**Remember:** A censored row still carries information: it survived at least that long. Never drop it.

**Common mistake:** Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.

Practice: open `examples/03_kaplan_meier_curves.py`, predict the output, change one line, predict again.

## 4. Hazard functions

Survival analysis answers 'how long until the event' when some subjects have not had it yet — that is censoring, and throwing those rows away biases everything. Churn, machine failure and time-to-conversion are all survival problems people usually mis-model as classification.

```python
import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)
```

**Remember:** A censored row still carries information: it survived at least that long. Never drop it.

**Common mistake:** Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.

Practice: open `examples/04_hazard_functions.py`, predict the output, change one line, predict again.

## 5. Cox proportional hazards

Survival analysis answers 'how long until the event' when some subjects have not had it yet — that is censoring, and throwing those rows away biases everything. Churn, machine failure and time-to-conversion are all survival problems people usually mis-model as classification.

```python
import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)
```

**Remember:** A censored row still carries information: it survived at least that long. Never drop it.

**Common mistake:** Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.

Practice: open `examples/05_cox_proportional_hazards.py`, predict the output, change one line, predict again.

## 6. Churn as a survival problem

Survival analysis answers 'how long until the event' when some subjects have not had it yet — that is censoring, and throwing those rows away biases everything. Churn, machine failure and time-to-conversion are all survival problems people usually mis-model as classification.

```python
import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)
```

**Remember:** A censored row still carries information: it survived at least that long. Never drop it.

**Common mistake:** Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.

Practice: open `examples/06_churn_as_a_survival_problem.py`, predict the output, change one line, predict again.

## 7. Features that change over time

Survival analysis answers 'how long until the event' when some subjects have not had it yet — that is censoring, and throwing those rows away biases everything. Churn, machine failure and time-to-conversion are all survival problems people usually mis-model as classification.

```python
import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)
```

**Remember:** A censored row still carries information: it survived at least that long. Never drop it.

**Common mistake:** Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.

Practice: open `examples/07_features_that_change_over_time.py`, predict the output, change one line, predict again.

## 8. Evaluating survival models

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

Practice: open `examples/08_evaluating_survival_models.py`, predict the output, change one line, predict again.

## 9. Business use: retention and maintenance

Missing data is information, not just noise. Before filling anything, ask *why* it is missing: a sensor that fails only under load is not missing at random. Then choose: drop rows, drop the column, fill with a statistic, or add an explicit 'was missing' indicator column.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Remember:** Compute the fill statistic on the TRAIN split only, then apply it to test.

**Common mistake:** Filling with the mean computed over the full dataset — that leaks test information into training.

Practice: open `examples/09_business_use_retention_and_maintenance.py`, predict the output, change one line, predict again.

## 10. When plain classification is enough

Survival analysis answers 'how long until the event' when some subjects have not had it yet — that is censoring, and throwing those rows away biases everything. Churn, machine failure and time-to-conversion are all survival problems people usually mis-model as classification.

```python
import numpy as np

# Kaplan-Meier estimator, by hand
times = np.array([2, 3, 3, 5, 8, 9, 12])
event = np.array([1, 1, 0, 1, 0, 1, 0])   # 0 = still alive at last contact (censored)

surv, n_at_risk, s = [], len(times), 1.0
for t in np.unique(times):
    at_risk = int((times >= t).sum())
    died = int(((times == t) & (event == 1)).sum())
    if died:
        s *= (1 - died / at_risk)
    surv.append((int(t), at_risk, died, round(s, 3)))

print('time  at_risk  events  S(t)')
for row in surv:
    print('%4d %8d %7d %6.3f' % row)
```

**Remember:** A censored row still carries information: it survived at least that long. Never drop it.

**Common mistake:** Modelling churn as 'churned in 30 days yes/no' and silently discarding everyone who joined last week.

Practice: open `examples/10_when_plain_classification_is_enough.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 67

- Explain **Time-to-event framing** to someone else without notes.
- Explain **Censoring** to someone else without notes.
- Explain **Kaplan-Meier curves** to someone else without notes.
- Explain **Hazard functions** to someone else without notes.
- Explain **Cox proportional hazards** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
