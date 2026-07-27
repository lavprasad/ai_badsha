#!/usr/bin/env python3
"""Generate Day001..Day200 lesson packs for ai_badsha.

Each day gets: notes.md, examples/01..10_*.py, questions.md, answers.md
and (for PROJECT/CAPSTONE days) project.md.

Run:  python tools/gen_days.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from curriculum import CURRICULUM  # noqa: E402
from teach import teach  # noqa: E402


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return s[:40] or "concept"


def day_dir(n: int) -> Path:
    return ROOT / f"Day{n:02d}"


# ---------------------------------------------------------------- notes.md

def notes_md(n: int, theme: str, concepts: list[str], lessons: list[dict]) -> str:
    out = [f"# Day {n:02d} — {theme}", ""]
    out.append(f"Today's goal: work through **{theme.lower()}** — ten concepts, ten runnable examples, five questions.")
    out.append("")
    out.append("| # | Concept |")
    out.append("|--:|---------|")
    for i, c in enumerate(concepts, 1):
        out.append(f"| {i} | {c} |")
    out.append("")
    out.append("---")
    out.append("")

    for i, (concept, lesson) in enumerate(zip(concepts, lessons), 1):
        out.append(f"## {i}. {concept}")
        out.append("")
        out.append(lesson["plain"])
        out.append("")
        out.append("```python")
        out.append(lesson["code"])
        out.append("```")
        out.append("")
        out.append(f"**Remember:** {lesson['remember']}")
        out.append("")
        out.append(f"**Common mistake:** {lesson['mistake']}")
        out.append("")

    out.append("---")
    out.append("")
    out.append(f"## What you should be able to do after Day {n:02d}")
    out.append("")
    for c in concepts[:5]:
        out.append(f"- Explain **{c}** to someone else without notes.")
    out.append("- Run every file in `examples/` and predict its output before running it.")
    out.append("- Answer `questions.md` before opening `answers.md`.")
    out.append("")
    out.append("Now open `examples/`, run each file, then break it on purpose and fix it.")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- examples

def example_py(n: int, i: int, concept: str, theme: str, lesson: dict) -> str:
    header = (
        f'"""Day {n:02d} — {theme}\n'
        f"Concept {i}: {concept}\n\n"
        f"Run:  python {i:02d}_{slug(concept)}.py\n"
        f'"""\n'
    )
    footer = (
        "\n\n"
        "# ---------------------------------------------------------------------\n"
        f"# Remember: {lesson['remember']}\n"
        f"# Common mistake: {lesson['mistake']}\n"
        "#\n"
        "# Try it: change one number or one line above, predict the new output,\n"
        "# then run it again. Being wrong here is cheap; being wrong in production\n"
        "# is not.\n"
    )
    return header + "\n" + lesson["code"].rstrip() + footer


# ---------------------------------------------------------------- questions

def questions_md(n: int, theme: str, concepts: list[str], lessons: list[dict]) -> str:
    picks = [0, 2, 4, 6, 9][: len(concepts)]
    out = [f"# Day {n:02d} — 5 Questions", ""]
    out.append("> Answer these **before** opening `answers.md`. Write your answer down first —")
    out.append("> a guess you committed to teaches you far more than one you kept vague.")
    out.append("")
    out.append("---")
    out.append("")

    templates = [
        ("What goes wrong", "Someone writes code for **{c}** and hits a bug in production.\n\nName the single most likely mistake they made, and say exactly what symptom it produces."),
        ("Predict the output", "Read the example for **{c}** in `examples/` without running it.\n\nWrite down what it prints. Then run it. If you were wrong, explain *why* you were wrong —\nthat gap is the actual lesson."),
        ("Why this rule", "For **{c}** the rule is:\n\n> {r}\n\nExplain *why* that rule exists. What specifically breaks if you ignore it?"),
        ("Design decision", "You are building a real system and **{c}** is on the table.\n\nWhen would you use it, and what would you use instead if that condition is not met?\nGive one concrete scenario for each side."),
        ("Debug it", "A colleague's code involving **{c}** produces results that look plausible but are wrong.\n\nList the first three things you would check, in order, and say what each one would rule out."),
    ]

    for qi, (idx, (title, body)) in enumerate(zip(picks, templates), 1):
        c = concepts[idx]
        out.append(f"### Q{qi}. {title}")
        out.append("")
        out.append(body.format(c=c, r=lessons[idx]["remember"]))
        out.append("")
        out.append("---")
        out.append("")

    out.append("### Build task")
    out.append("")
    out.append(f"Pick any two concepts from today and write **one** script that uses both together.")
    out.append("Twenty lines is enough. It must run, and you must be able to explain every line.")
    out.append("")
    return "\n".join(out)


def answers_md(n: int, theme: str, concepts: list[str], lessons: list[dict]) -> str:
    picks = [0, 2, 4, 6, 9][: len(concepts)]
    out = [f"# Day {n:02d} — Answers", ""]
    out.append("Read these **after** you have written your own answers.")
    out.append("")
    out.append("---")
    out.append("")

    a1 = concepts[picks[0]]
    out.append("### A1. What goes wrong")
    out.append("")
    out.append(f"**{a1}** — the classic failure is:")
    out.append("")
    out.append(f"> {lessons[picks[0]]['mistake']}")
    out.append("")
    out.append("It is common precisely because the code still runs. Nothing crashes; the numbers")
    out.append("just quietly stop meaning what you think they mean.")
    out.append("")
    out.append("---")
    out.append("")

    a2 = concepts[picks[1]]
    out.append("### A2. Predict the output")
    out.append("")
    out.append(f"The example for **{a2}** is `examples/{picks[1] + 1:02d}_{slug(a2)}.py`.")
    out.append("Run it and compare against what you wrote.")
    out.append("")
    out.append("The point is not the number it prints. The point is whether your mental model")
    out.append("of what the code does matches what the machine actually does. Where they differ,")
    out.append("your model is wrong — fix the model, not the guess.")
    out.append("")
    out.append(f"Key idea to check yourself against: {lessons[picks[1]]['remember']}")
    out.append("")
    out.append("---")
    out.append("")

    a3 = concepts[picks[2]]
    out.append("### A3. Why this rule")
    out.append("")
    out.append(f"Rule: {lessons[picks[2]]['remember']}")
    out.append("")
    out.append(f"It exists because of the failure directly underneath it: {lessons[picks[2]]['mistake']}")
    out.append("")
    out.append("Rules in this course are all shaped the same way — each one is a scar from a")
    out.append("specific bug. Learn the bug and the rule becomes obvious instead of arbitrary.")
    out.append("")
    out.append("---")
    out.append("")

    a4 = concepts[picks[3]]
    out.append("### A4. Design decision")
    out.append("")
    out.append(f"**{a4}** in one line: {lessons[picks[3]]['plain'].split('. ')[0]}.")
    out.append("")
    out.append("Use it when its assumptions hold and the cost is justified. Reach for something")
    out.append("simpler when they do not — a baseline you understand beats a sophisticated method")
    out.append("you cannot debug at 2am. The right answer names *the assumption*, not the tool.")
    out.append("")
    out.append(f"Watch out for: {lessons[picks[3]]['mistake']}")
    out.append("")
    out.append("---")
    out.append("")

    a5 = concepts[picks[4]]
    out.append("### A5. Debug it")
    out.append("")
    out.append(f"For **{a5}**, check in this order:")
    out.append("")
    out.append("1. **The data.** Shapes, dtypes, null counts, value ranges. Most 'model bugs' are data bugs.")
    out.append("2. **The split.** Anything computed before the train/test split can leak and make results look good and be wrong.")
    out.append(f"3. **The specific trap for this concept:** {lessons[picks[4]]['mistake']}")
    out.append("")
    out.append("Only after those three should you suspect the algorithm itself.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("### Build task")
    out.append("")
    out.append("There is no single right answer. A good submission:")
    out.append("")
    out.append("- runs without errors on a clean interpreter,")
    out.append("- uses both concepts for a reason you can state in one sentence each,")
    out.append("- prints something that would change if the logic broke,")
    out.append("- and has no line you cannot explain.")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- project.md

def project_md(n: int, theme: str, concepts: list[str]) -> str:
    name = theme.split(":", 1)[-1].strip() if ":" in theme else theme
    out = [f"# Day {n:02d} PROJECT — {name}", ""]
    out.append("A project is not a bigger exercise. It is the part where nobody tells you the")
    out.append("shape of the answer. Build the thinnest end-to-end version first, then thicken it.")
    out.append("")
    out.append("## Milestones")
    out.append("")
    for i, c in enumerate(concepts, 1):
        out.append(f"{i}. **{c}**")
    out.append("")
    out.append("## Definition of done")
    out.append("")
    out.append("- [ ] Runs end to end from a single command on a clean checkout.")
    out.append("- [ ] Has a README stating the problem, the metric, and the result.")
    out.append("- [ ] Beats a stated baseline — and the baseline number is written down.")
    out.append("- [ ] Every random source is seeded; a rerun reproduces the number.")
    out.append("- [ ] At least one test that fails if the core logic breaks.")
    out.append("- [ ] Limitations section that is honest about what it cannot do.")
    out.append("")
    out.append("## How to avoid the usual trap")
    out.append("")
    out.append("The usual trap is spending week one on infrastructure and week four discovering")
    out.append("the data cannot answer the question. Invert it: on day one, get the dumbest")
    out.append("possible version working end to end — hard-coded paths, one file, terrible")
    out.append("accuracy. That version tells you whether the project is possible at all.")
    out.append("Everything after that is improvement, and improvement is easy to schedule.")
    out.append("")
    out.append("## Stretch goals")
    out.append("")
    out.append("- Serve it behind an HTTP endpoint.")
    out.append("- Add a monitoring script that would catch it silently degrading.")
    out.append("- Write it up as a post someone outside your team could follow.")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- main

def main() -> None:
    written = 0
    fallback_hits = 0
    total_concepts = 0

    for n, theme, concepts in CURRICULUM:
        lessons = [teach(c, theme) for c in concepts]
        for c, lesson in zip(concepts, lessons):
            total_concepts += 1
            if lesson["remember"].startswith("State one assumption"):
                fallback_hits += 1

        d = day_dir(n)
        ex = d / "examples"
        ex.mkdir(parents=True, exist_ok=True)

        (d / "notes.md").write_text(notes_md(n, theme, concepts, lessons), encoding="utf-8")
        (d / "questions.md").write_text(questions_md(n, theme, concepts, lessons), encoding="utf-8")
        (d / "answers.md").write_text(answers_md(n, theme, concepts, lessons), encoding="utf-8")

        if theme.upper().startswith(("PROJECT", "CAPSTONE")):
            (d / "project.md").write_text(project_md(n, theme, concepts), encoding="utf-8")

        for stale in ex.glob("*.py"):
            stale.unlink()
        for i, (c, lesson) in enumerate(zip(concepts, lessons), 1):
            (ex / f"{i:02d}_{slug(c)}.py").write_text(example_py(n, i, c, theme, lesson), encoding="utf-8")

        written += 1

    covered = total_concepts - fallback_hits
    print(f"generated {written} days, {total_concepts} concepts")
    print(f"bank coverage: {covered}/{total_concepts} ({100 * covered / total_concepts:.1f}%)")


if __name__ == "__main__":
    main()
