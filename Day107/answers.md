# Day 107 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Detection vs classification** — the classic failure is:

> Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Intersection over union** is `examples/03_intersection_over_union.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: IoU >= 0.5 is the usual 'correct detection' threshold; report mAP, not accuracy.

---

### A3. Why this rule

Rule: Output size = (in - kernel + 2*pad)/stride + 1. Print shapes when a layer refuses to connect.

It exists because of the failure directly underneath it: Forgetting the channel dimension and feeding (H,W) where the layer expects (N,C,H,W).

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Non-maximum suppression** in one line: Classification says what; detection says what and where.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Mixing box formats (xywh vs xyxy) between the model and the evaluation code.

---

### A5. Debug it

For **Fine-tuning a detector**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
