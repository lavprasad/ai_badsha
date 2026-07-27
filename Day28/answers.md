# Day 28 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Sets, relations and functions** — the classic failure is:

> A membership test against a list inside a loop, turning a linear job into a quadratic one.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Graphs, nodes and edges** is `examples/03_graphs_nodes_and_edges.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

---

### A3. Why this rule

Rule: Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.

It exists because of the failure directly underneath it: A membership test against a list inside a loop, turning a linear job into a quadratic one.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Complexity of common ML operations** in one line: Complexity decides architecture.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: A membership test against a list inside a loop, turning a linear job into a quadratic one.

---

### A5. Debug it

For **Why complexity decides your architecture**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Assuming a bigger context window is free — attention cost grows with the square of sequence length.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
