# Day 80 — 5 Questions

> Answer these **before** opening `answers.md`. Write your answer down first —
> a guess you committed to teaches you far more than one you kept vague.

---

### Q1. What goes wrong

Someone writes code for **Batch, stochastic and mini-batch descent** and hits a bug in production.

Name the single most likely mistake they made, and say exactly what symptom it produces.

---

### Q2. Predict the output

Read the example for **Momentum** in `examples/` without running it.

Write down what it prints. Then run it. If you were wrong, explain *why* you were wrong —
that gap is the actual lesson.

---

### Q3. Why this rule

For **AdaGrad and RMSProp** the rule is:

> Adam's default lr 1e-3 is a good start for scratch training; 1e-5 to 5e-5 for fine-tuning.

Explain *why* that rule exists. What specifically breaks if you ignore it?

---

### Q4. Design decision

You are building a real system and **AdamW and decoupled weight decay** is on the table.

When would you use it, and what would you use instead if that condition is not met?
Give one concrete scenario for each side.

---

### Q5. Debug it

A colleague's code involving **Implementing Adam from scratch** produces results that look plausible but are wrong.

List the first three things you would check, in order, and say what each one would rule out.

---

### Build task

Pick any two concepts from today and write **one** script that uses both together.
Twenty lines is enough. It must run, and you must be able to explain every line.
