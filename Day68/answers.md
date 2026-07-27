# Day 68 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Prediction vs intervention** — the classic failure is:

> Telling a business to change X because the model gave X a high feature importance.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Randomised experiments as the gold standard** is `examples/03_randomised_experiments_as_the_gold_stand.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

---

### A3. Why this rule

Rule: Name the confounders before you interpret any observational effect. If you cannot, do not claim causality.

It exists because of the failure directly underneath it: Telling a business to change X because the model gave X a high feature importance.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Directed acyclic graphs** in one line: Most production data lives in a database, and pulling ten million rows into pandas to compute one average is a waste of everything.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: `SELECT *` on a wide table, then dropping 90% of the columns in pandas.

---

### A5. Debug it

For **Asking causal questions honestly**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Telling a business to change X because the model gave X a high feature importance.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
