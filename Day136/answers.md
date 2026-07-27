# Day 136 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Fluency versus factuality** — the classic failure is:

> Shipping a chatbot with no abstain path, so it invents a policy under pressure.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Grounding in sources** is `examples/03_grounding_in_sources.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: An explicit 'not in my sources' path is worth more than any confidence score.

---

### A3. Why this rule

Rule: Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

It exists because of the failure directly underneath it: Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Abstaining when uncertain** in one line: Today's idea — **Abstaining when uncertain** — sits inside the theme of Text generation quality.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Copy-pasting `Abstaining when uncertain` from a tutorial without knowing what it assumes or when it fails.

---

### A5. Debug it

For **Designing for graceful wrongness**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Copy-pasting `Designing for graceful wrongness` from a tutorial without knowing what it assumes or when it fails.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
