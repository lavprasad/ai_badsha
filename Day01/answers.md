# Day 01 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why Python owns AI** — the classic failure is:

> Installing a package with one Python and importing it with another, then blaming the package.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Virtual environments with venv** is `examples/03_virtual_environments_with_venv.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: If `pip install` worked but the import fails, you installed into a different interpreter.

---

### A3. Why this rule

Rule: `breakpoint()` is built in. You never need to add print statements to inspect a value again.

It exists because of the failure directly underneath it: Debugging a nested pipeline with print statements you then forget to remove.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Google Colab and free GPUs** in one line: Colab gives you a free GPU in a browser, which removes the biggest barrier to starting deep learning.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Training for four hours in Colab with no checkpointing and losing everything to a disconnect.

---

### A5. Debug it

For **How to use this 200-day course**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Installing a package with one Python and importing it with another, then blaming the package.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
