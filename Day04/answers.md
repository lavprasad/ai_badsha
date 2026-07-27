# Day 04 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Reading and writing text files** — the classic failure is:

> `fh.read().split('\n')` on a huge file, which loads it all into RAM and then dies.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **CSV files with the csv module** is `examples/03_csv_files_with_the_csv_module.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

---

### A3. Why this rule

Rule: Use `Path` division (`root / 'data' / 'x.csv'`) instead of string concatenation with slashes.

It exists because of the failure directly underneath it: Committing an API key, then 'removing' it in a later commit where it still lives in history.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Working with large files line by line** in one line: `with open(...)` closes the file even if the body raises — that is what a context manager is for.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: `fh.read().split('\n')` on a huge file, which loads it all into RAM and then dies.

---

### A5. Debug it

For **A tiny dataset downloader script**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Committing an API key, then 'removing' it in a later commit where it still lives in history.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
