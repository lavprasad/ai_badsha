# Day 152 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Why RAG instead of fine-tuning** — the classic failure is:

> Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Document loading and parsing** is `examples/03_document_loading_and_parsing.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Always show the source of each retrieved chunk in the answer so users can verify it.

---

### A3. Why this rule

Rule: Always show the source of each retrieved chunk in the answer so users can verify it.

It exists because of the failure directly underneath it: Chunking blindly at 1000 characters and cutting tables and code blocks in half.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Storing vectors with metadata** in one line: A vector is a list of numbers with a direction and length.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Comparing raw embeddings with Euclidean distance when only direction carries meaning.

---

### A5. Debug it

For **A minimal RAG in 50 lines**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Chunking blindly at 1000 characters and cutting tables and code blocks in half.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
