# Day 103 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Starting from a known-good architecture** — the classic failure is:

> Assuming a bigger context window is free — attention cost grows with the square of sequence length.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Skip connections by default** is `examples/03_skip_connections_by_default.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Log the gradient norm during training — a sudden spike explains a sudden loss spike.

---

### A3. Why this rule

Rule: Scale features before regularising, or the penalty punishes whichever column happens to use small units.

It exists because of the failure directly underneath it: Tuning `alpha` on the test set — pick it with cross-validation on train only.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Loss matching the output layer** in one line: ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Testing only the happy path, so an all-null column silently trains a constant model.

---

### A5. Debug it

For **Documenting why each choice was made**, check in this order:

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
