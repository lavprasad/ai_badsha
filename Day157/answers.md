# Day 157 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**What makes something an agent** — the classic failure is:

> Giving an agent a shell tool with no allowlist and no confirmation step.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Tool definitions and schemas** is `examples/03_tool_definitions_and_schemas.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

---

### A3. Why this rule

Rule: Always bound the loop. An unbounded agent burns money and finds creative ways to fail.

It exists because of the failure directly underneath it: Giving an agent a shell tool with no allowlist and no confirmation step.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**State between steps** in one line: An agent is a loop: the model picks a tool, your code runs it, the result goes back into context, repeat until done.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Giving an agent a shell tool with no allowlist and no confirmation step.

---

### A5. Debug it

For **Building a two-tool agent from scratch**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Giving an agent a shell tool with no allowlist and no confirmation step.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
