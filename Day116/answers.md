# Day 116 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Latency and power constraints** — the classic failure is:

> Scaling the learning rate wrongly when you scale the batch — a larger batch usually needs a larger LR.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Quantised inference** is `examples/03_quantised_inference.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Measure on the target device, warm and under load — not on your laptop, once, cold.

---

### A3. Why this rule

Rule: `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

It exists because of the failure directly underneath it: Preprocessing in a notebook and then forgetting one step when writing the serving code.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Thermal throttling** in one line: Most training runs are not compute-bound; they are waiting on data.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Renting four GPUs to fix a bottleneck that was a single-threaded JPEG decode.

---

### A5. Debug it

For **Deploying a detector to a Raspberry Pi**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Validating latency on a desktop GPU and discovering the phone throttles after 40 seconds.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
