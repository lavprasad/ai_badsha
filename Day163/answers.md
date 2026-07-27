# Day 163 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Categories of harmful content** — the classic failure is:

> Letting a model-chosen tool call run with the caller's full privileges and no allowlist.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Refusal design that stays useful** is `examples/03_refusal_design_that_stays_useful.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Delimit untrusted content and enforce authorisation in code — a prompt is not a security boundary.

---

### A3. Why this rule

Rule: Delimit untrusted content and enforce authorisation in code — a prompt is not a security boundary.

It exists because of the failure directly underneath it: Letting a model-chosen tool call run with the caller's full privileges and no allowlist.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Red-teaming your own app** in one line: Retrieved documents, web pages and user files are untrusted input.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Letting a model-chosen tool call run with the caller's full privileges and no allowlist.

---

### A5. Debug it

For **Balancing safety and usefulness**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Letting a model-chosen tool call run with the caller's full privileges and no allowlist.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
