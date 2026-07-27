# Day 41 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Train, validation and test roles** — the classic failure is:

> A random split on data with repeated customers, so the model recognises the customer, not the pattern.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Stratified split for imbalance** is `examples/03_stratified_split_for_imbalance.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: One entity must live on exactly one side of the split. Check the overlap; do not assume it.

---

### A3. Why this rule

Rule: One entity must live on exactly one side of the split. Check the overlap; do not assume it.

It exists because of the failure directly underneath it: A random split on data with repeated customers, so the model recognises the customer, not the pattern.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Stratified and grouped K-fold** in one line: Three splits, three jobs: train fits parameters, validation picks hyperparameters, test gives one honest final number.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Random K-fold on time-series or on grouped data (same patient in train and test) — both leak.

---

### A5. Debug it

For **Locking the test set away**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** A random split on data with repeated customers, so the model recognises the customer, not the pattern.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
