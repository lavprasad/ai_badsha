# Day 69 — Answers

Read these **after** you have written your own answers.

---

### A1. What goes wrong

**Text preprocessing pipeline** — the classic failure is:

> Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

It is common precisely because the code still runs. Nothing crashes; the numbers
just quietly stop meaning what you think they mean.

---

### A2. Predict the output

The example for **Stopwords, stemming, lemmatisation** is `examples/03_stopwords_stemming_lemmatisation.py`.
Run it and compare against what you wrote.

The point is not the number it prints. The point is whether your mental model
of what the code does matches what the machine actually does. Where they differ,
your model is wrong — fix the model, not the guess.

Key idea to check yourself against: TF-IDF + logistic regression is the baseline every LLM text classifier must beat to be worth its cost.

---

### A3. Why this rule

Rule: TF-IDF + logistic regression is the baseline every LLM text classifier must beat to be worth its cost.

It exists because of the failure directly underneath it: Reaching for a 7B model to classify support tickets that TF-IDF handles at 94% for free.

Rules in this course are all shaped the same way — each one is a scar from a
specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.

---

### A4. Design decision

**Character n-grams for noisy text** in one line: Before embeddings, text became numbers by counting.

Use it when its assumptions hold and the cost is justified. Reach for something
simpler when they do not — a baseline you understand beats a sophisticated method
you cannot debug at 2am. The right answer names *the assumption*, not the tool.

Watch out for: Reaching for a 7B model to classify support tickets that TF-IDF handles at 94% for free.

---

### A5. Debug it

For **The baseline every LLM must beat**, check in this order:

1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.
2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.
3. **The specific trap for this concept:** Copy-pasting `The baseline every LLM must beat` from a tutorial without knowing what it assumes or when it fails.

Only after those three should you suspect the algorithm itself.

---

### Build task

There is no single right answer. A good submission:

- runs without errors on a clean interpreter,
- uses both concepts for a reason you can state in one sentence each,
- prints something that would change if the logic broke,
- and has no line you cannot explain.
