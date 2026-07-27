# Day 19 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**The derivative as a rate of change** — the classic failure is:

> Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Partial derivatives** is `examples/03_partial_derivatives.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

---

### A3. Why this rule

Rule: A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

It exists because of the failure directly underneath it: Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**The Jacobian** in one line: The derivative answers: if I nudge this input a little, how much does the output move? The gradient is that answer for every input at once, so it points uphill.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

---

### A5. Debug it

For **Hand-deriving a two-layer gradient**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
