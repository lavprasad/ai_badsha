# Start here

> **Hinglish me padhna hai?** Har din ka Hinglish version `hinglish/DayNN/` me hai.
> Website par header ka **EN English / हिं Hinglish** button dabao — notes, sawaal aur
> jawab sab Hinglish me aa jaate hain. Code examples dono taraf English hi rehte hain.

## The daily loop (about 2 hours)

1. **Read `notes.md`** — ten concepts. Do not skim the "Common mistake" lines; those are
   the parts that cost people weeks.
2. **Run every file in `examples/`** — but *predict the output first*. Being wrong on a
   ten-line script is the cheapest learning available to you.
3. **Break one example on purpose.** Change a shape, remove a `.fit()`, drop the seed.
   Read the error. You are training your ability to read errors, which is most of the job.
4. **Answer `questions.md` on paper** before opening `answers.md`.
5. **Do the build task.** Twenty lines. It must run.

## Rules that make this work

- **One day per day.** Cramming ten days on Sunday teaches you almost nothing.
- **Never open `answers.md` first.** A wrong answer you committed to is worth ten correct
  answers you read.
- **Type the code.** Do not copy-paste. The friction is the point.
- **Keep a `notes/` file of your own** — one line per day on what surprised you. At Day 200
  that file is more valuable than the course.
- **If a day feels easy, do the build task twice as hard.** If a day feels impossible,
  do the first three concepts and move on. You will meet them again.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
```

Two examples (Day 102, Day 104) need `pip install torch` as well — everything else
runs on the requirements file.

## If you fall behind

You will. Do not restart from Day 1 — that is the most common way people quit. Pick up
where you stopped. The course does not know you were gone.
