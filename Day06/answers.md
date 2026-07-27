# Day 06 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why NumPy is fast: contiguous memory** — the classic failure is:

> Copy-pasting `Why NumPy is fast: contiguous memory` from a tutorial without knowing what it assumes or when it fails.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **dtype and memory footprint** is `examples/03_dtype_and_memory_footprint.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: `axis=0` collapses rows (down the columns); `axis=1` collapses columns (across a row).

---

### A3. Why this rule

Rule: Test the data contract, not just the function — bad data breaks more models than bad code.

It exists because of the failure directly underneath it: Testing only the happy path, so an all-null column silently trains a constant model.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Fancy indexing** in one line: NumPy's power is selecting and combining without loops.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

---

### A5. Debug it

For **Timing a vectorised speedup**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Comparing raw embeddings with Euclidean distance when only direction carries meaning.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
