# Day 78 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Loss as the objective you actually optimise** — the classic failure is:

> Optimising plain accuracy for a fraud model where a miss costs 10,000x a false alarm.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Mean absolute error and Huber** is `examples/03_mean_absolute_error_and_huber.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Quote median + IQR for skewed data, mean + std only for roughly symmetric data.

---

### A3. Why this rule

Rule: Clip probabilities before `log` — `log(0)` is `-inf` and poisons the whole batch.

It exists because of the failure directly underneath it: Applying softmax twice (once in the model, once in the loss) and getting flat, untrainable gradients.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Class weights inside the loss** in one line: When one class is 1% of the data, the model learns to always say 'no'.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Applying SMOTE before the split so synthetic copies of test rows appear in training.

---

### A5. Debug it

For **Custom losses for business costs**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Optimising plain accuracy for a fraud model where a miss costs 10,000x a false alarm.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
