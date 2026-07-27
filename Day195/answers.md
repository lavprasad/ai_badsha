# Day 195 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Structure of a good technical write-up** — the classic failure is:

> A README that explains your architecture for 400 lines and never says what score it achieved.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Explaining the method without jargon** is `examples/03_explaining_the_method_without_jargon.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.

---

### A3. Why this rule

Rule: Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

It exists because of the failure directly underneath it: Six weeks of feature engineering with no baseline to prove any of it helped.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**README as the front door** in one line: Lead with the result, then the method, then the caveats.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: A README that explains your architecture for 400 lines and never says what score it achieved.

---

### A5. Debug it

For **Publishing on GitHub Pages**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** A README that explains your architecture for 400 lines and never says what score it achieved.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
