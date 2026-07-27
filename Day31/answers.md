# Day 31 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**The linear model equation** — the classic failure is:

> Copy-pasting `The linear model equation` from a tutorial without knowing what it assumes or when it fails.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Deriving the normal equations** is `examples/03_deriving_the_normal_equations.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Cosine similarity ignores magnitude; Euclidean distance does not. Pick the one that matches your question.

---

### A3. Why this rule

Rule: Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

It exists because of the failure directly underneath it: Auditing fairness once at launch and never again as the data drifts.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Multicollinearity and its symptoms** in one line: Today's idea — **Multicollinearity and its symptoms** — sits inside the theme of Linear models, mathematically.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Copy-pasting `Multicollinearity and its symptoms` from a tutorial without knowing what it assumes or when it fails.

---

### A5. Debug it

For **Interpreting coefficients honestly**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Testing only the happy path, so an all-null column silently trains a constant model.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
