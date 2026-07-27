# Day 34 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Goal: a tiny numeric library you understand fully** — the classic failure is:

> Six weeks of feature engineering with no baseline to prove any of it helped.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Numeric gradient utility** is `examples/03_numeric_gradient_utility.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

---

### A3. Why this rule

Rule: Cosine similarity ignores magnitude; Euclidean distance does not. Pick the one that matches your question.

It exists because of the failure directly underneath it: Comparing raw embeddings with Euclidean distance when only direction carries meaning.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Logistic regression from scratch** in one line: Logistic regression squashes a linear score through a sigmoid to get a probability.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Reading the raw output as a calibrated probability without ever checking a calibration curve.

---

### A5. Debug it

For **What you now never have to take on faith**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Six weeks of feature engineering with no baseline to prove any of it helped.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
