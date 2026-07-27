# Day 80 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Batch, stochastic and mini-batch descent** — the classic failure is:

> Leaving the learning rate fixed forever instead of decaying it once the loss plateaus.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Momentum** is `examples/03_momentum.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

---

### A3. Why this rule

Rule: Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

It exists because of the failure directly underneath it: Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**AdamW and decoupled weight decay** in one line: Regularisation penalises large weights so the model prefers simpler explanations.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Tuning `alpha` on the test set — pick it with cross-validation on train only.

---

### A5. Debug it

For **Implementing Adam from scratch**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Using the same learning rate for pretraining and fine-tuning and destroying the pretrained weights.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
