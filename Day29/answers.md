# Day 29 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Floating point representation** — the classic failure is:

> Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Overflow and underflow** is `examples/03_overflow_and_underflow.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Compare floats with a tolerance (`np.isclose`), never with `==`.

---

### A3. Why this rule

Rule: Compare floats with a tolerance (`np.isclose`), never with `==`.

It exists because of the failure directly underneath it: Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Deterministic seeds vs true randomness** in one line: Floats are approximations.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

---

### A5. Debug it

For **Debugging a silently wrong computation**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Getting `nan` deep in training and only then discovering an `exp()` overflowed twelve steps earlier.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
