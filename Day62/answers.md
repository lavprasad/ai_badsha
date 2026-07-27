# Day 62 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Global vs local explanation** — the classic failure is:

> Presenting importance as causation — the model found correlation, nothing more.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Impurity importance and its bias** is `examples/03_impurity_importance_and_its_bias.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

---

### A3. Why this rule

Rule: Label the axes. An unlabelled plot is a decoration, not evidence.

It exists because of the failure directly underneath it: Judging a model by its accuracy number alone without ever looking at the data.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**SHAP values** in one line: If you cannot explain a decision, you cannot defend it — and in credit, hiring and healthcare you are legally required to.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Presenting importance as causation — the model found correlation, nothing more.

---

### A5. Debug it

For **Explanation is not causation**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Presenting importance as causation — the model found correlation, nothing more.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
