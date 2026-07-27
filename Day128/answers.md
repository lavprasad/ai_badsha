# Day 128 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Encoder-only: BERT** — the classic failure is:

> Assuming a bigger context window is free — attention cost grows with the square of sequence length.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Decoder-only: GPT family** is `examples/03_decoder_only_gpt_family.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Block = LayerNorm -> Attention -> add residual -> LayerNorm -> MLP -> add residual. Memorise it.

---

### A3. Why this rule

Rule: Block = LayerNorm -> Attention -> add residual -> LayerNorm -> MLP -> add residual. Memorise it.

It exists because of the failure directly underneath it: Assuming a bigger context window is free — attention cost grows with the square of sequence length.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Which family for which task** in one line: A transformer block is attention + feed-forward, each wrapped in a residual connection and a LayerNorm.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Assuming a bigger context window is free — attention cost grows with the square of sequence length.

---

### A5. Debug it

For **Reading a model card**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Assuming a bigger context window is free — attention cost grows with the square of sequence length.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
