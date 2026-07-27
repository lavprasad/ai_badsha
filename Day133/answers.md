# Day 133 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Autoregressive generation** — the classic failure is:

> Leaving max_tokens unbounded on a retry loop and burning a month's budget overnight.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Temperature** is `examples/03_temperature.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Use temperature 0 for anything you will parse; save randomness for prose.

---

### A3. Why this rule

Rule: Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

It exists because of the failure directly underneath it: Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Beam search for constrained tasks** in one line: Generation is a loop: predict a distribution, pick a token, append, repeat.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Leaving max_tokens unbounded on a retry loop and burning a month's budget overnight.

---

### A5. Debug it

For **Choosing decoding settings per task**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Leaving max_tokens unbounded on a retry loop and burning a month's budget overnight.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
