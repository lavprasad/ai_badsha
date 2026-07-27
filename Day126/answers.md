# Day 126 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Query, key, value projections** — the classic failure is:

> Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Causal and padding masks** is `examples/03_causal_and_padding_masks.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Output size = (in - kernel + 2*pad)/stride + 1. Print shapes when a layer refuses to connect.

---

### A3. Why this rule

Rule: The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

It exists because of the failure directly underneath it: Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Sliding window and sparse attention** in one line: Attention lets every token look at every other token and decide what matters.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

---

### A5. Debug it

For **Implementing multi-head attention**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
