# Day 150 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**What LLMs are good and bad at** — the classic failure is:

> Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Task decomposition** is `examples/03_task_decomposition.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Singular values sorted descending tell you how many dimensions actually carry information.

---

### A3. Why this rule

Rule: The model proposes; your code disposes. Never let model output be the last check before an action.

It exists because of the failure directly underneath it: Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Human-in-the-loop design** in one line: Put the stochastic part in the smallest possible box.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

---

### A5. Debug it

For **Writing an LLM system design doc**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Trusting a model's own 'confidence: 0.98' field as if it were a calibrated probability.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
