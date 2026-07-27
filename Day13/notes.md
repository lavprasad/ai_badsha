# Day 13 — SQL for AI practitioners

Today's goal: work through **sql for ai practitioners** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Why SQL is still where the data lives |
| 2 | SELECT, WHERE, ORDER BY, LIMIT |
| 3 | GROUP BY and HAVING |
| 4 | JOIN types and row explosions |
| 5 | Window functions for lag features |
| 6 | CTEs for readable queries |
| 7 | sqlite3 from Python |
| 8 | pandas read_sql and to_sql |
| 9 | Pushing aggregation to the database |
| 10 | Query performance basics |

---

## 1. Why SQL is still where the data lives

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

## 2. SELECT, WHERE, ORDER BY, LIMIT

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

## 3. GROUP BY and HAVING

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

## 4. JOIN types and row explosions

A DataFrame is a table with labelled columns and an index. Most real ML work is 80% reshaping tables: load, clean, group, join, aggregate. Learn `groupby` and `merge` well and you can answer most data questions without writing loops.

```python
import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))
```

**Remember:** Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

**Common mistake:** Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

## 5. Window functions for lag features

Time series break the i.i.d. assumption every other model relies on. You must split by time, never randomly. Most of the value comes from lag features, rolling statistics and calendar effects — often with plain gradient boosting on top.

```python
import pandas as pd
import numpy as np

idx = pd.date_range('2024-01-01', periods=120, freq='D')
y = pd.Series(np.arange(120) * 0.3 + 10 * np.sin(np.arange(120) / 7) + np.random.default_rng(0).normal(0, 1, 120), index=idx)

feat = pd.DataFrame({'y': y})
feat['lag_1'] = feat['y'].shift(1)
feat['lag_7'] = feat['y'].shift(7)
feat['roll_7'] = feat['y'].shift(1).rolling(7).mean()
feat['dow'] = feat.index.dayofweek
print(feat.dropna().head())

cut = int(len(feat) * 0.8)
print('train ends', feat.index[cut - 1].date(), '| test starts', feat.index[cut].date())
```

**Remember:** Every feature must use `.shift(1)` or later — no row may see its own future.

**Common mistake:** A rolling mean that includes the current row, which leaks the target into the feature.

## 6. CTEs for readable queries

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

## 7. sqlite3 from Python

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

## 8. pandas read_sql and to_sql

A DataFrame is a table with labelled columns and an index. Most real ML work is 80% reshaping tables: load, clean, group, join, aggregate. Learn `groupby` and `merge` well and you can answer most data questions without writing loops.

```python
import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))
```

**Remember:** Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

**Common mistake:** Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

## 9. Pushing aggregation to the database

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

## 10. Query performance basics

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

---

## What you should be able to do after Day 13

- Explain **Why SQL is still where the data lives** to someone else without notes.
- Explain **SELECT, WHERE, ORDER BY, LIMIT** to someone else without notes.
- Explain **GROUP BY and HAVING** to someone else without notes.
- Explain **JOIN types and row explosions** to someone else without notes.
- Explain **Window functions for lag features** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
