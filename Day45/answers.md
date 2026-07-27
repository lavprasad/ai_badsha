# Day 45 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**The scikit-learn estimator API** — the classic failure is:

> Testing only the happy path, so an all-null column silently trains a constant model.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Loading a built-in dataset** is `examples/03_loading_a_built_in_dataset.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Report your model's score next to the dummy's. A number alone means nothing.

---

### A3. Why this rule

Rule: Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

It exists because of the failure directly underneath it: Reading the raw output as a calibrated probability without ever checking a calibration curve.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Comparing against a dummy baseline** in one line: Every scikit-learn model has the same three methods, which means swapping algorithms is a one-line change.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Celebrating 92% accuracy on data where 91% of rows are one class.

---

### A5. Debug it

For **The seven-line template you will reuse forever**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Celebrating 92% accuracy on data where 91% of rows are one class.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
