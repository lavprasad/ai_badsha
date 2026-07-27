# Day 56 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Comparing models fairly** — the classic failure is:

> Declaring a winner from a difference smaller than the standard error across folds.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Repeated and stratified CV** is `examples/03_repeated_and_stratified_cv.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Use the same `cv` object for every candidate, or you are comparing luck.

---

### A3. Why this rule

Rule: State one assumption `Statistical comparison of two models` makes about your data before you use it.

It exists because of the failure directly underneath it: Copy-pasting `Statistical comparison of two models` from a tutorial without knowing what it assumes or when it fails.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Nested CV for honest estimates** in one line: Two models differing by 0.3% with a 2% fold-to-fold spread are the same model.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Declaring a winner from a difference smaller than the standard error across folds.

---

### A5. Debug it

For **Choosing simplest-that-works**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Declaring a winner from a difference smaller than the standard error across folds.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
