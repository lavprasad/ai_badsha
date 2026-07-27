# Day 114 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Text detection vs text recognition** — the classic failure is:

> Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Deep OCR models** is `examples/03_deep_ocr_models.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

---

### A3. Why this rule

Rule: Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

It exists because of the failure directly underneath it: Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Document classification** in one line: Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

---

### A5. Debug it

For **An invoice extraction pipeline**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
