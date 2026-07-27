# Day 47 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why unregularised models overfit wide data** — the classic failure is:

> Copy-pasting `Why unregularised models overfit wide data` from a tutorial without knowing what it assumes or when it fails.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Lasso and automatic feature selection** is `examples/03_lasso_and_automatic_feature_selection.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Scale features before regularising, or the penalty punishes whichever column happens to use small units.

---

### A3. Why this rule

Rule: Report the spread across folds, not just the mean — high variance means you cannot trust the mean.

It exists because of the failure directly underneath it: Random K-fold on time-series or on grouped data (same patient in train and test) — both leak.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Coefficient paths** in one line: ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Testing only the happy path, so an all-null column silently trains a constant model.

---

### A5. Debug it

For **Comparing all four on one dataset**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Copy-pasting `Comparing all four on one dataset` from a tutorial without knowing what it assumes or when it fails.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
