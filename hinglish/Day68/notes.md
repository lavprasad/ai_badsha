# Day 68 — Causal inference basics

Aaj ka goal: **Causal inference basics** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Prediction vs intervention |
| 2 | Confounders |
| 3 | Randomised experiments as the gold standard |
| 4 | Propensity score matching |
| 5 | Difference-in-differences |
| 6 | Instrumental variables |
| 7 | Directed acyclic graphs |
| 8 | Uplift modelling |
| 9 | Why ML models answer the wrong question |
| 10 | Asking causal questions honestly |

---

## 1. Prediction vs intervention

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/01_prediction_vs_intervention.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Confounders

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/02_confounders.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Randomised experiments as the gold standard

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/03_randomised_experiments_as_the_gold_stand.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Propensity score matching

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/04_propensity_score_matching.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Difference-in-differences

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/05_difference_in_differences.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Instrumental variables

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/06_instrumental_variables.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Directed acyclic graphs

### Aasaan Bhasha

Zyadatar production data database me hi rehta hai, aur ek average nikalne ke liye ek crore rows pandas me kheenchna har cheez ki barbaadi hai. SQL me aggregate karo, chhota result wapas lao. Window functions aapko lag features aur running totals database chhode bina de dete hain.

### Chhota code

```python
import sqlite3

con = sqlite3.connect(':memory:')
con.executescript('''
CREATE TABLE sales (city TEXT, day TEXT, amount REAL);
INSERT INTO sales VALUES
  ('pune','2024-01-01',10),('pune','2024-01-02',15),
  ('delhi','2024-01-01',7),('delhi','2024-01-02',9);
''')

rows = con.execute('''
    WITH daily AS (
        SELECT city, day, amount,
               LAG(amount) OVER (PARTITION BY city ORDER BY day) AS prev
        FROM sales
    )
    SELECT city, day, amount, prev, amount - COALESCE(prev, 0) AS delta
    FROM daily ORDER BY city, day
''').fetchall()
for r in rows:
    print(r)
```

**Yaad rakho:** Filtering aur aggregation SQL me dhakelo; sirf wahi lao jis par aap sach me model banaoge.

**Aam galti:** Chaudi table par `SELECT *`, phir pandas me 90% columns drop kar dena.

Practice: `examples/07_directed_acyclic_graphs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Uplift modelling

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/08_uplift_modelling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Why ML models answer the wrong question

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/09_why_ml_models_answer_the_wrong_question.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Asking causal questions honestly

### Aasaan Bhasha

Prediction poochti hai 'kya hoga'; causal inference poochti hai 'agar main dakhal doon to kya hoga'. Model ek confounded correlation se perfectly predict kar sakta hai aur aapko ye salaah de sakta hai ki kya badalna hai — bilkul galat. Randomised experiments causal sawaalon ka jawab dete hain; observational data ko strong assumptions chahiye jo aapko likhni padengi.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
n = 5000
severe = rng.random(n) < 0.3                  # confounder: severity
treated = rng.random(n) < np.where(severe, 0.8, 0.2)   # sick people get treated
outcome = 0.6 * severe - 0.3 * treated + rng.normal(0, 0.1, n)

naive = outcome[treated].mean() - outcome[~treated].mean()
adjusted = np.mean([
    outcome[(treated) & (severe == s)].mean() - outcome[(~treated) & (severe == s)].mean()
    for s in (0, 1)
])
print(f'naive difference   {naive:+.3f}   (treatment looks harmful)')
print(f'adjusted for severity {adjusted:+.3f}   (true effect is -0.3)')
```

**Yaad rakho:** Kisi bhi observational effect ka matlab nikalne se pehle confounders ka naam lo. Naam na le sako to causality ka daawa mat karo.

**Aam galti:** Business ko X badalne ko kehna kyunki model ne X ko high feature importance di.

Practice: `examples/10_asking_causal_questions_honestly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 68 ke baad aapko ye aana chahiye

- **Prediction vs intervention** ko bina notes dekhe kisi dost ko samjha sakna.
- **Confounders** ko bina notes dekhe kisi dost ko samjha sakna.
- **Randomised experiments as the gold standard** ko bina notes dekhe kisi dost ko samjha sakna.
- **Propensity score matching** ko bina notes dekhe kisi dost ko samjha sakna.
- **Difference-in-differences** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
