# Day 139 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Tokenisation cost across scripts** — the classic failure is:

> Estimating cost or context usage in words instead of tokens and overflowing the window in production.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Cross-lingual transfer** is `examples/03_cross_lingual_transfer.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Measure tokens per request in your users' actual language, not in English.

---

### A3. Why this rule

Rule: Measure tokens per request in your users' actual language, not in English.

It exists because of the failure directly underneath it: Sizing a context window and a budget from English samples, then launching in a script that costs 4x.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Low-resource language strategies** in one line: Tokenisers are trained mostly on English, so the same sentence in Hindi or Tamil can cost three to five times more tokens — which means more money, less context and worse quality.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Sizing a context window and a budget from English samples, then launching in a script that costs 4x.

---

### A5. Debug it

For **Building for Indian language users**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Six weeks of feature engineering with no baseline to prove any of it helped.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
