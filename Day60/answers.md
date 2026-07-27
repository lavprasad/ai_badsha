# Day 60 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why high dimensions hurt** — the classic failure is:

> Running PCA before scaling, so one wide-range column becomes component 1 all by itself.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Explained variance and choosing components** is `examples/03_explained_variance_and_choosing_componen.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Quote median + IQR for skewed data, mean + std only for roughly symmetric data.

---

### A3. Why this rule

Rule: 'Restart kernel and run all' is the only honest test that a notebook works.

It exists because of the failure directly underneath it: Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**UMAP** in one line: PCA rotates the data onto axes of maximum variance and lets you drop the rest.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Running PCA before scaling, so one wide-range column becomes component 1 all by itself.

---

### A5. Debug it

For **Compressing a dataset without losing signal**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Running PCA before scaling, so one wide-range column becomes component 1 all by itself.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
