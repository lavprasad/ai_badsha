"""Day 13 — SQL for AI practitioners
Concept 9: Pushing aggregation to the database

Run:  python 09_pushing_aggregation_to_the_database.py
"""

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

# ---------------------------------------------------------------------
# Remember: Push filtering and aggregation into SQL; pull only what you will actually model on.
# Common mistake: `SELECT *` on a wide table, then dropping 90% of the columns in pandas.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
