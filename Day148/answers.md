# Day 148 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Anatomy of a chat completion request** — the classic failure is:

> Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **max_tokens and stop conditions** is `examples/03_max_tokens_and_stop_conditions.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Always set max_tokens and stop sequences. They are the difference between a bug and a bill.

---

### A3. Why this rule

Rule: Jitter matters: without it, every client retries at the same instant and re-creates the outage.

It exists because of the failure directly underneath it: Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Cost tracking per request** in one line: Any network call to a model will eventually time out, get rate-limited, or return malformed output.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

---

### A5. Debug it

For **A resilient API client wrapper**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
