# Day 175 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why notebooks do not ship** — the classic failure is:

> Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Configuration files over hard-coded values** is `examples/03_configuration_files_over_hard_coded_valu.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: 'Restart kernel and run all' is the only honest test that a notebook works.

---

### A3. Why this rule

Rule: 'Restart kernel and run all' is the only honest test that a notebook works.

It exists because of the failure directly underneath it: Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Packaging with pyproject.toml** in one line: Notebooks keep state between cells, which is great for exploring and terrible for reproducibility.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

---

### A5. Debug it

For **Refactoring a notebook into modules**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
