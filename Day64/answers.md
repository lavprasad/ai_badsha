# Day 64 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why ensembles work** — the classic failure is:

> Using impurity-based importances for business decisions instead of permutation importance.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Averaging regressors** is `examples/03_averaging_regressors.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Always show the source of each retrieved chunk in the answer so users can verify it.

---

### A3. Why this rule

Rule: A boolean mask returns a copy; a basic slice returns a view. Mutating one does not affect the other the same way.

It exists because of the failure directly underneath it: Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Diversity beats individual strength** in one line: Ensembles work when the members make *different* mistakes.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Shipping a five-model ensemble for a 0.2% gain and quintupling inference cost and failure modes.

---

### A5. Debug it

For **Building a stacked ensemble correctly**, check in this order:

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
