# Day 164 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Defining success for a fuzzy task** — the classic failure is:

> Changing the prompt on Friday with no eval and finding out from customers on Monday.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Deterministic checks first** is `examples/03_deterministic_checks_first.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: 50 real examples you curated beat 5000 synthetic ones nobody checked.

---

### A3. Why this rule

Rule: Alignment optimises a proxy for what humans want; the proxy can always be gamed.

It exists because of the failure directly underneath it: Over-optimising the reward model until outputs are sycophantic and useless — classic reward hacking.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Regression suites in CI** in one line: Vibes do not survive a prompt change.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Changing the prompt on Friday with no eval and finding out from customers on Monday.

---

### A5. Debug it

For **Closing the loop from eval to fix**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Changing the prompt on Friday with no eval and finding out from customers on Monday.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
