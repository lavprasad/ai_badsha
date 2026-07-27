# Day 193 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Choosing a task LLMs genuinely help with** — the classic failure is:

> Six weeks of feature engineering with no baseline to prove any of it helped.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Retrieval or tools as needed** is `examples/03_retrieval_or_tools_as_needed.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: 50 real examples you curated beat 5000 synthetic ones nobody checked.

---

### A3. Why this rule

Rule: 50 real examples you curated beat 5000 synthetic ones nobody checked.

It exists because of the failure directly underneath it: Changing the prompt on Friday with no eval and finding out from customers on Monday.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Prompt injection hardening** in one line: Retrieved documents, web pages and user files are untrusted input.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Letting a model-chosen tool call run with the caller's full privileges and no allowlist.

---

### A5. Debug it

For **Demo video and documentation**, check in this order:

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
