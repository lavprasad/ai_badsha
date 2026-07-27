# Day 32 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**From linear score to probability** — the classic failure is:

> Reporting accuracy on an imbalanced problem where predicting 'no' always scores 99%.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Odds and log-odds interpretation** is `examples/03_odds_and_log_odds_interpretation.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Clip the sigmoid input — `exp` of a large negative number overflows and returns NaN.

---

### A3. Why this rule

Rule: Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

It exists because of the failure directly underneath it: Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Decision boundaries** in one line: Logistic regression squashes a linear score through a sigmoid to get a probability.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Reading the raw output as a calibrated probability without ever checking a calibration curve.

---

### A5. Debug it

For **Implementing it from scratch**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Reading the raw output as a calibrated probability without ever checking a calibration curve.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
