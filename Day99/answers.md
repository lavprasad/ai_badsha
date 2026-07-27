# Day 99 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Agent, environment, reward** — the classic failure is:

> Giving an agent a shell tool with no allowlist and no confirmation step.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Policy and value functions** is `examples/03_policy_and_value_functions.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.

---

### A3. Why this rule

Rule: Initialise B to zeros so the adapted model starts exactly equal to the base model.

It exists because of the failure directly underneath it: Setting rank far too high — you lose the efficiency and gain the overfitting.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Q-learning** in one line: RL learns from reward instead of labels.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

---

### A5. Debug it

For **Reward hacking**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
