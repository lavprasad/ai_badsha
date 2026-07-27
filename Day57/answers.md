# Day 57 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Parameters vs hyperparameters** — the classic failure is:

> Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Grid search** is `examples/03_grid_search.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Fix the random seed and log every trial, or you cannot reproduce your own best model.

---

### A3. Why this rule

Rule: Rare events make precision collapse no matter how good the classifier looks on accuracy.

It exists because of the failure directly underneath it: Reporting accuracy on an imbalanced problem where predicting 'no' always scores 99%.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Successive halving** in one line: Hyperparameters are the settings you choose, not learn.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

---

### A5. Debug it

For **Logging every trial**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
