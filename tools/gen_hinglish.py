#!/usr/bin/env python3
"""Generate the Hinglish mirror of Day01..Day200 under hinglish/.

Only prose is mirrored — notes.md, questions.md, answers.md and project.md.
Examples (.py) are NOT mirrored; the hub falls back to the English ones because
code is code.

Run:  python tools/gen_hinglish.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from curriculum import CURRICULUM  # noqa: E402
from gen_days import slug  # noqa: E402
from teach_hi import teach_hi  # noqa: E402

OUT = ROOT / "hinglish"


def notes_md(n: int, theme: str, concepts: list[str], lessons: list[dict]) -> str:
    out = [f"# Day {n:02d} — {theme}", ""]
    out.append(f"Aaj ka goal: **{theme}** ko aasaan Hinglish me samajhna — das concepts, "
               "das chalne wale examples, paanch sawaal.")
    out.append("")
    out.append("Is din ko padhne ka tarika:")
    out.append("1. Har concept ka **Aasaan Bhasha** section padho.")
    out.append("2. Code sample dekho — pehle predict karo ki output kya aayega.")
    out.append("3. `examples/` me us concept ki file chalao (code English wali hi hai).")
    out.append("4. Uske BAAD hi `questions.md` kholo.")
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
        out.append("### Aasaan Bhasha")
        out.append("")
        out.append(lesson["plain"])
        out.append("")
        out.append("### Chhota code")
        out.append("")
        out.append("```python")
        out.append(lesson["code"])
        out.append("```")
        out.append("")
        out.append(f"**Yaad rakho:** {lesson['remember']}")
        out.append("")
        out.append(f"**Aam galti:** {lesson['mistake']}")
        out.append("")
        out.append(f"Practice: `examples/{i:02d}_{slug(concept)}.py` kholo, output predict karo, "
                   "ek line badlo, phir se predict karo.")
        out.append("")

    out.append("---")
    out.append("")
    out.append(f"## Day {n:02d} ke baad aapko ye aana chahiye")
    out.append("")
    for c in concepts[:5]:
        out.append(f"- **{c}** ko bina notes dekhe kisi dost ko samjha sakna.")
    out.append("- `examples/` ki har file chalana — aur chalane se pehle output predict karna.")
    out.append("- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.")
    out.append("")
    out.append("Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.")
    out.append("")
    return "\n".join(out)


def questions_md(n: int, theme: str, concepts: list[str], lessons: list[dict]) -> str:
    picks = [0, 2, 4, 6, 9][: len(concepts)]
    out = [f"# Day {n:02d} — 5 Sawaal", ""]
    out.append("> `answers.md` kholne se **pehle** inka jawab do. Pehle apna jawab likho —")
    out.append("> jis guess par aap tik gaye, wo dhundhle jawab se kahin zyada sikhata hai.")
    out.append("")
    out.append("---")
    out.append("")

    templates = [
        ("Kya galat hoga",
         "Koi **{c}** ke liye code likhta hai aur production me bug aa jaata hai.\n\n"
         "Sabse mumkin galti kaunsi hai, aur uska symptom theek-theek kya dikhega?"),
        ("Output predict karo",
         "`examples/` me **{c}** wali file bina chalaye padho.\n\n"
         "Likho ki wo kya print karegi. Phir chalao. Agar aap galat the, to samjhao ki *kyun* galat the —\n"
         "wahi gap asli seekh hai."),
        ("Ye rule kyun",
         "**{c}** ka rule hai:\n\n> {r}\n\nSamjhao ki ye rule hai hi kyun. Ise ignore karne par theek-theek kya tootta hai?"),
        ("Design faisla",
         "Aap ek asli system bana rahe ho aur **{c}** vichaar me hai.\n\n"
         "Aap ise kab use karoge, aur agar wo shart poori na ho to uski jagah kya use karoge?\n"
         "Dono taraf ke liye ek-ek thos scenario do."),
        ("Debug karo",
         "Aapke colleague ka **{c}** wala code aise results de raha hai jo theek lagte hain par galat hain.\n\n"
         "Aap sabse pehle kaunsi teen cheezein check karoge, kis kram me, aur har ek kya rule out karegi?"),
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
    out.append("Aaj ke koi bhi do concepts chuno aur **ek** script likho jo dono ko saath use kare.")
    out.append("Bees lines kaafi hain. Wo chalni chahiye, aur aapko har line samjha aani chahiye.")
    out.append("")
    return "\n".join(out)


def answers_md(n: int, theme: str, concepts: list[str], lessons: list[dict]) -> str:
    picks = [0, 2, 4, 6, 9][: len(concepts)]
    out = [f"# Day {n:02d} — Jawab", ""]
    out.append("Ye tab padho jab aap apne jawab likh chuke ho.")
    out.append("")
    out.append("---")
    out.append("")

    out.append("### A1. Kya galat hoga")
    out.append("")
    out.append(f"**{concepts[picks[0]]}** — classic failure ye hai:")
    out.append("")
    out.append(f"> {lessons[picks[0]]['mistake']}")
    out.append("")
    out.append("Ye isliye aam hai kyunki code phir bhi chalta rehta hai. Kuch crash nahi hota; bas numbers")
    out.append("chupchap wo matlab dena band kar dete hain jo aap samajh rahe the.")
    out.append("")
    out.append("---")
    out.append("")

    a2 = concepts[picks[1]]
    out.append("### A2. Output predict karo")
    out.append("")
    out.append(f"**{a2}** wali file `examples/{picks[1] + 1:02d}_{slug(a2)}.py` hai.")
    out.append("Use chalao aur apne likhe hue se milao.")
    out.append("")
    out.append("Baat number ki nahi hai. Baat ye hai ki code ke baare me aapka mental model machine")
    out.append("ke asli behaviour se milta hai ya nahi. Jahan wo alag hain, wahan aapka model galat hai —")
    out.append("guess nahi, model theek karo.")
    out.append("")
    out.append(f"Khud ko jis idea par jaanchna hai: {lessons[picks[1]]['remember']}")
    out.append("")
    out.append("---")
    out.append("")

    out.append("### A3. Ye rule kyun")
    out.append("")
    out.append(f"Rule: {lessons[picks[2]]['remember']}")
    out.append("")
    out.append(f"Ye isliye hai kyunki theek uske neeche wali failure hai: {lessons[picks[2]]['mistake']}")
    out.append("")
    out.append("Is course ke saare rules ek hi shakl ke hain — har ek kisi asli bug ka nishaan hai.")
    out.append("Bug samajh lo aur rule arbitrary ke bajaye obvious lagne lagega.")
    out.append("")
    out.append("---")
    out.append("")

    a4 = concepts[picks[3]]
    out.append("### A4. Design faisla")
    out.append("")
    out.append(f"**{a4}** ek line me: {lessons[picks[3]]['plain'].split('. ')[0]}.")
    out.append("")
    out.append("Ise tab use karo jab iski assumptions sach hon aur cost jaayaz ho. Jab na hon to kuch")
    out.append("simple uthao — jo baseline aap samajhte ho wo us fancy method se behtar hai jise aap raat")
    out.append("2 baje debug nahi kar sakte. Sahi jawab *assumption* ka naam leta hai, tool ka nahi.")
    out.append("")
    out.append(f"Dhyaan rakho: {lessons[picks[3]]['mistake']}")
    out.append("")
    out.append("---")
    out.append("")

    out.append("### A5. Debug karo")
    out.append("")
    out.append(f"**{concepts[picks[4]]}** ke liye is kram me check karo:")
    out.append("")
    out.append("1. **Data.** Shapes, dtypes, null counts, value ranges. Zyadatar 'model bugs' data bugs hote hain.")
    out.append("2. **Split.** Train/test split se pehle nikaali gayi koi bhi cheez leak kar sakti hai — result accha dikhega aur galat hoga.")
    out.append(f"3. **Is concept ka khaas jaal:** {lessons[picks[4]]['mistake']}")
    out.append("")
    out.append("In teeno ke baad hi algorithm par shak karo.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("### Build task")
    out.append("")
    out.append("Iska koi ek sahi jawab nahi hai. Achhe submission me:")
    out.append("")
    out.append("- saaf interpreter par bina error chalta hai,")
    out.append("- dono concepts kisi aisi wajah se use hote hain jo aap ek line me bata sako,")
    out.append("- kuch aisa print hota hai jo logic tootne par badal jaaye,")
    out.append("- aur koi line aisi nahi jise aap samjha na sako.")
    out.append("")
    return "\n".join(out)


def project_md(n: int, theme: str, concepts: list[str]) -> str:
    name = theme.split(":", 1)[-1].strip() if ":" in theme else theme
    out = [f"# Day {n:02d} PROJECT — {name}", ""]
    out.append("Project bada exercise nahi hota. Ye wo hissa hai jahan koi aapko jawab ki shakl nahi batata.")
    out.append("Pehle sabse patla end-to-end version banao, phir use mota karo.")
    out.append("")
    out.append("## Milestones")
    out.append("")
    for i, c in enumerate(concepts, 1):
        out.append(f"{i}. **{c}**")
    out.append("")
    out.append("## Kab kaha jaayega ki ho gaya")
    out.append("")
    out.append("- [ ] Saaf checkout par ek hi command se end to end chalta hai.")
    out.append("- [ ] README hai jisme problem, metric aur result likha hai.")
    out.append("- [ ] Ek batayi gayi baseline ko haraata hai — aur baseline ka number likha hua hai.")
    out.append("- [ ] Har random source seeded hai; dobara chalane par wahi number aata hai.")
    out.append("- [ ] Kam se kam ek test jo core logic tootne par fail ho.")
    out.append("- [ ] Limitations section jo imaandaari se batata hai ki ye kya nahi kar sakta.")
    out.append("")
    out.append("## Aam jaal se kaise bacho")
    out.append("")
    out.append("Aam jaal ye hai ki pehla hafta infrastructure me chala jaata hai aur chauthe hafte pata")
    out.append("chalta hai ki data se sawaal ka jawab mil hi nahi sakta. Ise ulta karo: pehle din sabse")
    out.append("bewakoof version end to end chalao — hard-coded paths, ek file, ghatiya accuracy. Wahi")
    out.append("version batata hai ki project mumkin bhi hai ya nahi. Uske baad ka sab sudhaar hai, aur")
    out.append("sudhaar schedule karna aasan hai.")
    out.append("")
    out.append("## Stretch goals")
    out.append("")
    out.append("- Ise HTTP endpoint ke peeche serve karo.")
    out.append("- Ek monitoring script jodo jo ise chupchap kharab hote hue pakad le.")
    out.append("- Ise aisi post ki tarah likho jise aapki team ke bahar ka koi follow kar sake.")
    out.append("")
    return "\n".join(out)


def main() -> None:
    fallback = 0
    total = 0
    for n, theme, concepts in CURRICULUM:
        lessons = [teach_hi(c, theme) for c in concepts]
        for lesson in lessons:
            total += 1
            if lesson["remember"].startswith("`") and "assumption likho" in lesson["remember"]:
                fallback += 1

        d = OUT / f"Day{n:02d}"
        d.mkdir(parents=True, exist_ok=True)
        (d / "notes.md").write_text(notes_md(n, theme, concepts, lessons), encoding="utf-8")
        (d / "questions.md").write_text(questions_md(n, theme, concepts, lessons), encoding="utf-8")
        (d / "answers.md").write_text(answers_md(n, theme, concepts, lessons), encoding="utf-8")
        if theme.upper().startswith(("PROJECT", "CAPSTONE")):
            (d / "project.md").write_text(project_md(n, theme, concepts), encoding="utf-8")

    covered = total - fallback
    print(f"hinglish: {len(CURRICULUM)} days -> {OUT}")
    print(f"bank coverage: {covered}/{total} ({100 * covered / total:.1f}%)")


if __name__ == "__main__":
    main()
