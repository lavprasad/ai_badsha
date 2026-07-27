# Day 07 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Element-wise arithmetic** — the classic failure is:

> Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Reductions: sum, mean, max along an axis** is `examples/03_reductions_sum_mean_max_along_an_axis.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: `axis=0` collapses rows (down the columns); `axis=1` collapses columns (across a row).

---

### A3. Why this rule

Rule: `axis=0` collapses rows (down the columns); `axis=1` collapses columns (across a row).

It exists because of the failure directly underneath it: Looping over array elements in Python instead of using a vectorised operation.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**np.where and conditional logic** in one line: NumPy's power is selecting and combining without loops.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Chaining `arr[mask][0] = 5` and wondering why the original array never changed — you wrote to a copy.

---

### A5. Debug it

For **Common shape errors and how to read them**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Presenting importance as causation — the model found correlation, nothing more.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
