# Day 124 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**RNNs for text** — the classic failure is:

> Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Bidirectional context** is `examples/03_bidirectional_context.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

---

### A3. Why this rule

Rule: RNNs are inherently sequential — they cannot parallelise across time, which is why transformers won.

It exists because of the failure directly underneath it: Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**The context bottleneck** in one line: An RNN carries a hidden state along the sequence, so order matters.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

---

### A5. Debug it

For **What still carries over**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Feeding unsorted variable-length sequences without padding masks, so padding tokens pollute the state.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
