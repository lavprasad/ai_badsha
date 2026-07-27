# Day 181 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Training/serving skew** — the classic failure is:

> Reloading the model per request and wondering why p99 latency is four seconds.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Offline vs online stores** is `examples/03_offline_vs_online_stores.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

---

### A3. Why this rule

Rule: One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.

It exists because of the failure directly underneath it: A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**When a feature store is overkill** in one line: Training/serving skew is when the feature computed offline differs from the one computed at request time — different code, different window, different timezone.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

---

### A5. Debug it

For **Designing for consistency**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
