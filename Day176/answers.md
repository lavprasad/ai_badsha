# Day 176 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Unit tests for transforms** — the classic failure is:

> Testing only the happy path, so an all-null column silently trains a constant model.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Model contract tests: shape and range** is `examples/03_model_contract_tests_shape_and_range.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Permutation importance on the TEST set answers 'what does this model rely on to generalise'.

---

### A3. Why this rule

Rule: Every test that touches randomness must pass an explicit seed. Global seeding is not enough under parallelism.

It exists because of the failure directly underneath it: A test suite so slow that CI skips it and bugs reach production anyway.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Testing training runs cheaply** in one line: ML tests come in layers: unit tests on transforms, contract tests on data, metamorphic tests on behaviour (adding an irrelevant feature must not change the prediction), and a tiny end-to-end run on a fixture dataset.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: A test suite so slow that CI skips it and bugs reach production anyway.

---

### A5. Debug it

For **A test suite you actually run**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** A test suite so slow that CI skips it and bugs reach production anyway.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
