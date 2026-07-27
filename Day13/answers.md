# Day 13 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why SQL is still where the data lives** — the classic failure is:

> `SELECT *` on a wide table, then dropping 90% of the columns in pandas.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **GROUP BY and HAVING** is `examples/03_group_by_and_having.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Push filtering and aggregation into SQL; pull only what you will actually model on.

---

### A3. Why this rule

Rule: Every feature must use `.shift(1)` or later — no row may see its own future.

It exists because of the failure directly underneath it: A rolling mean that includes the current row, which leaks the target into the feature.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**sqlite3 from Python** in one line: Most production data lives in a database, and pulling ten million rows into pandas to compute one average is a waste of everything.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: `SELECT *` on a wide table, then dropping 90% of the columns in pandas.

---

### A5. Debug it

For **Query performance basics**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** `SELECT *` on a wide table, then dropping 90% of the columns in pandas.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
