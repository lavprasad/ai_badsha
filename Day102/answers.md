# Day 102 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**CPU vs GPU vs TPU** — the classic failure is:

> Keeping the full loss tensor in a list each step — it holds the whole graph and leaks memory.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Batch size and utilisation** is `examples/03_batch_size_and_utilisation.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Profile before you scale. A slow `__getitem__` wastes more money than a small GPU.

---

### A3. Why this rule

Rule: A central difference `(f(x+h)-f(x-h))/2h` is the cheapest way to check a hand-written gradient.

It exists because of the failure directly underneath it: Trusting a derivation you never gradient-checked; a sign error trains slowly instead of failing loudly.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Data loading bottlenecks** in one line: Most training runs are not compute-bound; they are waiting on data.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Renting four GPUs to fix a bottleneck that was a single-threaded JPEG decode.

---

### A5. Debug it

For **Estimating training cost before you start**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Renting four GPUs to fix a bottleneck that was a single-threaded JPEG decode.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
