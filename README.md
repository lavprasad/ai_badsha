# AI Badsha — a 200-day AI course

Notes, runnable examples, questions with answers, and projects. One folder per day.

**Website:** https://lavprasad.github.io/ai_badsha/ — read the notes, run the Python in your
browser, take the quiz, track which days you have finished.

```
200 days   2000 concepts   2000 runnable Python examples   1000 questions   12 projects
```

---

## What is in each day

```
Day07/
  notes.md        the ten concepts, explained, with code and the mistake people make
  examples/       01..10 — one runnable .py per concept
  questions.md    5 questions + a build task (no peeking)
  answers.md      the answers (peek after)
  project.md      only on project days

hinglish/Day07/
  notes.md        wahi din, Hinglish me
  questions.md
  answers.md
  project.md
```

**Hinglish:** every day has a full Hinglish mirror under `hinglish/`. On the website use
the **EN English / हिं Hinglish** button in the header — it switches notes, questions and
answers and remembers your choice. Code examples stay English on both sides, because code
is code.

## The road

| Days | Phase | You end up able to |
|-----:|-------|--------------------|
| 1–15 | Python & the data toolkit | Load, clean, reshape and plot any dataset |
| 16–34 | Mathematics for AI | Read a paper's equations without flinching |
| 35–44 | Data work | Build a leak-free pipeline from raw file to model-ready matrix |
| 45–74 | Classical machine learning | Beat a strong baseline on tabular data, honestly |
| 75–104 | Deep learning foundations | Write backprop from scratch, then train real nets in PyTorch |
| 105–119 | Computer vision | Fine-tune, detect, segment, and ship a vision service |
| 120–149 | NLP, transformers, LLMs | Explain and implement attention; fine-tune with LoRA |
| 150–174 | LLM engineering | Build RAG, agents, structured output, evals and guardrails |
| 175–190 | Production AI | Serve, containerise, monitor, and survive an incident |
| 191–200 | Capstones and career | Three defensible projects and a plan for year two |

Projects land on days **15, 34, 44, 74, 104, 119, 149, 174, 190** and the three
capstones on **192, 193, 194**.

## Start here

```bash
git clone https://github.com/lavprasad/ai_badsha
cd ai_badsha
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt

cd Day01
python examples/01_why_python_owns_ai.py
```

Then read `notes.md`, run every example, answer `questions.md`, and only then open
`answers.md`. One day per day. Two hours beats eight hours once a week.

## Run the site locally

```bash
python tools/build_catalog.py
python -m http.server 8000
# open http://localhost:8000
```

The Run button executes Python inside the browser via Pyodide; numpy, pandas,
scikit-learn and matplotlib load on demand the first time an example imports them.
PyTorch does not run in the browser — those examples say so and are meant for your
local environment.

## Regenerating the course

The day folders are generated from two files, so fixing a typo in a concept fixes it
everywhere it appears:

```bash
python tools/curriculum.py       # validate the 200-day plan
python tools/teach.py            # validate the English bank (every snippet must parse)
python tools/teach_hi.py         # validate the Hinglish bank + report translation coverage
python tools/gen_days.py         # write Day01..Day200
python tools/gen_hinglish.py     # write hinglish/Day01..Day200
python tools/build_catalog.py    # rebuild the site index
python tools/smoke_examples.py   # run every unique example, report failures
```

- `tools/curriculum.py` — the 200 days × 10 concepts.
- `tools/teach.py` — the teaching bank: explanation, code, rule, and the mistake, per topic.
- `tools/teach_hi.py` — the same bank in Hinglish, keyed by each English entry's first
  keyword so it stays aligned if the English bank is reordered. Untranslated entries fall
  back to English prose rather than breaking.

## Honest limitations

- Two examples require `pip install torch` and will not run in the browser.
- Search and the glossary index the English notes only. Hinglish days are readable and
  switchable, but searching in Hinglish will return English hits.
- About 2% of concepts fall back to a generic prompt rather than a dedicated lesson;
  they are listed by `tools/gen_days.py` as bank misses and get filled in over time.
- The questions are generated from each day's concepts. They make you think, but they
  are not a substitute for building something nobody assigned you.
