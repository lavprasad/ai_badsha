# Day 122 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Bag of words revisited** — the classic failure is:

> Reaching for a 7B model to classify support tickets that TF-IDF handles at 94% for free.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **N-gram language models** is `examples/03_n_gram_language_models.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: TF-IDF + logistic regression is the baseline every LLM text classifier must beat to be worth its cost.

---

### A3. Why this rule

Rule: SVMs scale roughly quadratically with rows — above ~100k samples reach for boosting instead.

It exists because of the failure directly underneath it: Skipping feature scaling, which silently wrecks the RBF kernel.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Rule-based systems that still work** in one line: Not everything needs a model.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Fine-tuning a transformer to extract dates that `dateutil` already parses correctly.

---

### A5. Debug it

For **Deciding whether you need an LLM at all**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Testing only the happy path, so an all-null column silently trains a constant model.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
