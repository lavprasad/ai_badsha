# Day 68 — Causal inference basics

Today's goal: work through **Causal inference basics** — ten concepts, ten runnable examples, five questions.

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

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

## 2. Confounders

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

## 3. Randomised experiments as the gold standard

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

## 4. Propensity score matching

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

## 5. Difference-in-differences

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

## 6. Instrumental variables

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

## 7. Directed acyclic graphs

Most production data lives in a database, and pulling ten million rows into pandas to compute one average is a waste of everything. Aggregate in SQL, bring back the small result. Window functions give you lag features and running totals without leaving the database.

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

**Remember:** Push filtering and aggregation into SQL; pull only what you will actually model on.

**Common mistake:** `SELECT *` on a wide table, then dropping 90% of the columns in pandas.

## 8. Uplift modelling

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

## 9. Why ML models answer the wrong question

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

## 10. Asking causal questions honestly

Prediction asks 'what will happen'; causal inference asks 'what happens if I intervene'. A model can predict perfectly using a confounded correlation and give you catastrophically wrong advice about what to change. Randomised experiments answer causal questions; observational data needs strong assumptions you must state.

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

**Remember:** Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

**Common mistake:** Telling a business to change X because the model gave X a high feature importance.

---

## What you should be able to do after Day 68

- Explain **Prediction vs intervention** to someone else without notes.
- Explain **Confounders** to someone else without notes.
- Explain **Randomised experiments as the gold standard** to someone else without notes.
- Explain **Propensity score matching** to someone else without notes.
- Explain **Difference-in-differences** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
