# Day 101 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why inference cost matters more than training cost** — the classic failure is:

> Running extraction at temperature 1 and debugging 'random' JSON failures for a week.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Post-training vs quantisation-aware training** is `examples/03_post_training_vs_quantisation_aware_trai.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Initialise B to zeros so the adapted model starts exactly equal to the base model.

---

### A3. Why this rule

Rule: Quantise, measure quality on your own eval set, then decide. Published benchmarks are not your task.

It exists because of the failure directly underneath it: Shipping an int4 model because it fits, without ever measuring what accuracy it cost you.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Operator fusion** in one line: Training cost is paid once; inference cost is paid on every request forever.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Shipping an int4 model because it fits, without ever measuring what accuracy it cost you.

---

### A5. Debug it

For **Shrinking a model for edge deployment**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** `COPY . .` before `pip install`, which busts the dependency cache on every code edit.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
