# Day 100 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Actor-critic methods** — the classic failure is:

> Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **PPO and clipped objectives** is `examples/03_ppo_and_clipped_objectives.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.

---

### A3. Why this rule

Rule: Reward shaping decides what the agent actually learns — and it will exploit any loophole you leave.

It exists because of the failure directly underneath it: Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Simulation and the sim-to-real gap** in one line: RL learns from reward instead of labels.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Rewarding a proxy metric and getting an agent that maximises the proxy while failing the real goal.

---

### A5. Debug it

For **A gridworld agent from scratch**, check in this order:

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
