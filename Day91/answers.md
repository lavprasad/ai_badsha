# Day 91 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why pretrained features transfer** — the classic failure is:

> Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Fine-tuning: unfreeze at a low LR** is `examples/03_fine_tuning_unfreeze_at_a_low_lr.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Fix the random seed and log every trial, or you cannot reproduce your own best model.

---

### A3. Why this rule

Rule: Shuffle every epoch, otherwise the model learns the order of your file.

It exists because of the failure directly underneath it: Leaving the learning rate fixed forever instead of decaying it once the loss plateaus.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Domain gap and when transfer fails** in one line: Almost nobody trains a vision model from scratch.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.

---

### A5. Debug it

For **Fine-tuning on a few hundred images**, check in this order:

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
