# Day 24 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Population vs sample** — the classic failure is:

> Slicing the data 15 ways after the fact and reporting the one slice that reached significance.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Confidence intervals** is `examples/03_confidence_intervals.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Decide the sample size and the metric BEFORE looking at the data.

---

### A3. Why this rule

Rule: Decide the sample size and the metric BEFORE looking at the data.

It exists because of the failure directly underneath it: Peeking daily and stopping the test the moment p < 0.05 — that inflates false positives badly.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Type I and Type II errors** in one line: You measure a sample and want to claim something about a population.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Slicing the data 15 ways after the fact and reporting the one slice that reached significance.

---

### A5. Debug it

For **Bootstrapping without formulas**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Using impurity-based importances for business decisions instead of permutation importance.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
