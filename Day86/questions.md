# Day 86 — 5 Questions

> Answer these **before** opening `answers.md`. Write your answer down first —
> a guess you committed to teaches you far more than one you kept vague.

---

### Q1. What goes wrong

Someone writes code for **Train and validation phases** and hits a bug in production.

Name the single most likely mistake they made, and say exactly what symptom it produces.

---

### Q2. Predict the output

Read the example for **torch.no_grad() for inference** in `examples/` without running it.

Write down what it prints. Then run it. If you were wrong, explain *why* you were wrong —
that gap is the actual lesson.

---

### Q3. Why this rule

For **Checkpointing and resuming** the rule is:

> `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

Explain *why* that rule exists. What specifically breaks if you ignore it?

---

### Q4. Design decision

You are building a real system and **Gradient clipping** is on the table.

When would you use it, and what would you use instead if that condition is not met?
Give one concrete scenario for each side.

---

### Q5. Debug it

A colleague's code involving **A reusable Trainer you actually own** produces results that look plausible but are wrong.

List the first three things you would check, in order, and say what each one would rule out.

---

### Build task

Pick any two concepts from today and write **one** script that uses both together.
Twenty lines is enough. It must run, and you must be able to explain every line.
