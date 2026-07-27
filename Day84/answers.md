# Day 84 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Tensors and dtypes** — the classic failure is:

> Looping over array elements in Python instead of using a vectorised operation.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **CPU and GPU devices** is `examples/03_cpu_and_gpu_devices.py`.
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

**nn.Module and parameters** in one line: PyTorch is NumPy with gradients and a GPU.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

---

### A5. Debug it

For **Common PyTorch error messages**, check in this order:

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
