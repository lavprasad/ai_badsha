# Day 183 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**What a model incident looks like** — the classic failure is:

> Testing only the happy path, so an all-null column silently trains a constant model.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Immediate mitigation: rollback or disable** is `examples/03_immediate_mitigation_rollback_or_disable.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Test the data contract, not just the function — bad data breaks more models than bad code.

---

### A3. Why this rule

Rule: `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

It exists because of the failure directly underneath it: Preprocessing in a notebook and then forgetting one step when writing the serving code.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Communication with stakeholders** in one line: ML code needs the same tests as any code, plus data tests: schema, ranges, null rates, class balance.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Testing only the happy path, so an all-null column silently trains a constant model.

---

### A5. Debug it

For **Reducing mean time to recovery**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Removing 'outliers' automatically when they are the exact events you were hired to predict.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
