# Day 39 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Features carry more weight than algorithms** — the classic failure is:

> Building a feature from a column that is only filled in AFTER the event you are predicting.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Aggregations over groups** is `examples/03_aggregations_over_groups.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Every engineered feature must be computable at prediction time with data you will actually have.

---

### A3. Why this rule

Rule: Every engineered feature must be computable at prediction time with data you will actually have.

It exists because of the failure directly underneath it: Building a feature from a column that is only filled in AFTER the event you are predicting.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Interaction terms** in one line: Feature engineering is where domain knowledge beats compute.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Building a feature from a column that is only filled in AFTER the event you are predicting.

---

### A5. Debug it

For **Documenting every feature's meaning**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Removing 'outliers' automatically when they are the exact events you were hired to predict.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
