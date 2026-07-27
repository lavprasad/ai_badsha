# Day 36 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Public dataset sources** — the classic failure is:

> Scraping a source whose terms forbid it and discovering the problem after the model is in production.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Web scraping ethics and robots.txt** is `examples/03_web_scraping_ethics_and_robots_txt.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

---

### A3. Why this rule

Rule: Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

It exists because of the failure directly underneath it: Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Data licensing and terms of use** in one line: Where data comes from decides what you may do with it.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Scraping a source whose terms forbid it and discovering the problem after the model is in production.

---

### A5. Debug it

For **Documenting data provenance**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Filling with the mean computed over the full dataset — that leaks test information into training.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
