# Day 86 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Train and validation phases** — the classic failure is:

> Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **torch.no_grad() for inference** is `examples/03_torch_no_grad_for_inference.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

---

### A3. Why this rule

Rule: `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

It exists because of the failure directly underneath it: Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Gradient clipping** in one line: The derivative answers: if I nudge this input a little, how much does the output move? The gradient is that answer for every input at once, so it points uphill.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

---

### A5. Debug it

For **A reusable Trainer you actually own**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
