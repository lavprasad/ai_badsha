# Day 138 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Turns, roles and system prompts** — the classic failure is:

> Writing a vague prompt, getting vague output, and blaming the model.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Context window management** is `examples/03_context_window_management.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Use temperature 0 for anything you will parse; save randomness for prose.

---

### A3. Why this rule

Rule: A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.

It exists because of the failure directly underneath it: Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Escalation to a human** in one line: Context is not memory.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.

---

### A5. Debug it

For **Building a grounded support bot**, check in this order:

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
