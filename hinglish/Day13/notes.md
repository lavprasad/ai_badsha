# Day 13 — SQL for AI practitioners

Aaj ka goal: **SQL for AI practitioners** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

Practice: `examples/01_why_sql_is_still_where_the_data_lives.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. SELECT, WHERE, ORDER BY, LIMIT

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

Practice: `examples/02_select_where_order_by_limit.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. GROUP BY and HAVING

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

Practice: `examples/03_group_by_and_having.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. JOIN types and row explosions

### Aasaan Bhasha

DataFrame ek table hai jisme labelled columns aur ek index hota hai. Asli ML ka 80% kaam tables ko reshape karna hi hai: load, clean, group, join, aggregate. `groupby` aur `merge` acche se seekh lo to zyadatar data sawaal bina loop likhe hal ho jaate hain.

### Chhota code

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

**Yaad rakho:** Merge se pehle aur baad me `df.shape` zaroor check karo — chupke se rows badhna matlab duplicate keys.

**Aam galti:** Chained assignment (`df[df.a > 1]['b'] = 0`) jo copy par likhta hai aur kuch nahi badalta.

Practice: `examples/04_join_types_and_row_explosions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Window functions for lag features

### Aasaan Bhasha

Time series wo i.i.d. assumption todti hain jis par baaki har model tika hai. Aapko time se split karna hi padega, random se kabhi nahi. Zyadatar value lag features, rolling statistics aur calendar effects se aati hai — aksar upar se saada gradient boosting laga kar.

### Chhota code

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

**Yaad rakho:** Har feature `.shift(1)` ya usse aage ka use kare — koi row apna khud ka future na dekhe.

**Aam galti:** Aisa rolling mean jo current row ko bhi shaamil kare, jo target ko feature me leak kar deta hai.

Practice: `examples/05_window_functions_for_lag_features.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. CTEs for readable queries

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

Practice: `examples/06_ctes_for_readable_queries.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. sqlite3 from Python

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

Practice: `examples/07_sqlite3_from_python.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. pandas read_sql and to_sql

### Aasaan Bhasha

DataFrame ek table hai jisme labelled columns aur ek index hota hai. Asli ML ka 80% kaam tables ko reshape karna hi hai: load, clean, group, join, aggregate. `groupby` aur `merge` acche se seekh lo to zyadatar data sawaal bina loop likhe hal ho jaate hain.

### Chhota code

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

**Yaad rakho:** Merge se pehle aur baad me `df.shape` zaroor check karo — chupke se rows badhna matlab duplicate keys.

**Aam galti:** Chained assignment (`df[df.a > 1]['b'] = 0`) jo copy par likhta hai aur kuch nahi badalta.

Practice: `examples/08_pandas_read_sql_and_to_sql.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Pushing aggregation to the database

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

Practice: `examples/09_pushing_aggregation_to_the_database.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Query performance basics

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

Practice: `examples/10_query_performance_basics.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 13 ke baad aapko ye aana chahiye

- **Why SQL is still where the data lives** ko bina notes dekhe kisi dost ko samjha sakna.
- **SELECT, WHERE, ORDER BY, LIMIT** ko bina notes dekhe kisi dost ko samjha sakna.
- **GROUP BY and HAVING** ko bina notes dekhe kisi dost ko samjha sakna.
- **JOIN types and row explosions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Window functions for lag features** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
