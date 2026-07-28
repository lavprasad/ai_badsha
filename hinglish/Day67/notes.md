# Day 67 — Survival and duration models

Aaj ka goal: **Survival and duration models** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.

### Chhota code

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

**Yaad rakho:** Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.

**Aam galti:** Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.

Practice: `examples/01_time_to_event_framing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Censoring

### Aasaan Bhasha

Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.

### Chhota code

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

**Yaad rakho:** Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.

**Aam galti:** Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.

Practice: `examples/02_censoring.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Kaplan-Meier curves

### Aasaan Bhasha

Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.

### Chhota code

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

**Yaad rakho:** Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.

**Aam galti:** Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.

Practice: `examples/03_kaplan_meier_curves.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Hazard functions

### Aasaan Bhasha

Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.

### Chhota code

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

**Yaad rakho:** Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.

**Aam galti:** Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.

Practice: `examples/04_hazard_functions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Cox proportional hazards

### Aasaan Bhasha

Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.

### Chhota code

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

**Yaad rakho:** Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.

**Aam galti:** Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.

Practice: `examples/05_cox_proportional_hazards.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Churn as a survival problem

### Aasaan Bhasha

Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.

### Chhota code

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

**Yaad rakho:** Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.

**Aam galti:** Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.

Practice: `examples/06_churn_as_a_survival_problem.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Features that change over time

### Aasaan Bhasha

Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.

### Chhota code

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

**Yaad rakho:** Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.

**Aam galti:** Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.

Practice: `examples/07_features_that_change_over_time.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Evaluating survival models

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

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

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/08_evaluating_survival_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Business use: retention and maintenance

### Aasaan Bhasha

Missing data information hai, sirf noise nahi. Kuch bharne se pehle poochho ki **kyun** missing hai: jo sensor sirf load par fail hota hai wo randomly missing nahi hai. Phir chuno: rows drop, column drop, statistic se fill, ya ek explicit 'ye missing tha' indicator column.

### Chhota code

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Yaad rakho:** Fill karne wali statistic sirf TRAIN split par nikalo, phir test par lagao.

**Aam galti:** Poore dataset ke mean se fill karna — ye test ki information training me leak kar deta hai.

Practice: `examples/09_business_use_retention_and_maintenance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. When plain classification is enough

### Aasaan Bhasha

Survival analysis 'event hone me kitna waqt' ka jawab deta hai jab kuch subjects ke saath ab tak hua hi nahi — wahi censoring hai, aur un rows ko phenk dena sab kuch bias kar deta hai. Churn, machine failure aur time-to-conversion sab survival problems hain jinhe log aam taur par classification samajh lete hain.

### Chhota code

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

**Yaad rakho:** Censored row bhi information rakhti hai: wo kam se kam itna to chali. Use kabhi drop mat karo.

**Aam galti:** Churn ko '30 din me churn hua haan/na' bana kar chupchap un sab ko hata dena jo pichhle hafte hi jude the.

Practice: `examples/10_when_plain_classification_is_enough.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 67 ke baad aapko ye aana chahiye

- **Time-to-event framing** ko bina notes dekhe kisi dost ko samjha sakna.
- **Censoring** ko bina notes dekhe kisi dost ko samjha sakna.
- **Kaplan-Meier curves** ko bina notes dekhe kisi dost ko samjha sakna.
- **Hazard functions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Cox proportional hazards** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
