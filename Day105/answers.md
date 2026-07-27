# Day 105 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Pixels, channels and bit depth** — the classic failure is:

> Feeding BGR from OpenCV into a model trained on RGB and losing accuracy for no visible reason.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Image file formats and compression** is `examples/03_image_file_formats_and_compression.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: State one assumption `Image file formats and compression` makes about your data before you use it.

---

### A3. Why this rule

Rule: Check the channel order (RGB vs BGR) and the value range (0-255 vs 0-1) before every model call.

It exists because of the failure directly underneath it: Feeding BGR from OpenCV into a model trained on RGB and losing accuracy for no visible reason.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Normalisation for pretrained models** in one line: A vector is a list of numbers with a direction and length.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Comparing raw embeddings with Euclidean distance when only direction carries meaning.

---

### A5. Debug it

For **Building an image loading utility**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Six weeks of feature engineering with no baseline to prove any of it helped.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
