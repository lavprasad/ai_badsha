# Day 113 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Joint image-text embedding space** — the classic failure is:

> Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Zero-shot classification** is `examples/03_zero_shot_classification.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Put the output format last and show it as an example — models copy the nearest pattern.

---

### A3. Why this rule

Rule: Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

It exists because of the failure directly underneath it: Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Visual question answering** in one line: Multimodal models put images and text in one shared embedding space, so a picture of a dog lands near the words 'a dog'.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

---

### A5. Debug it

For **Building a semantic image search**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Feeding an image at the wrong resolution or normalisation and getting silent quality loss.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
