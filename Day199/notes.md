# Day 199 — Continuous learning system

Today's goal: work through **Continuous learning system** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Choosing sources worth your attention |
| 2 | A weekly learning cadence |
| 3 | Learning by building, not watching |
| 4 | Spaced repetition for fundamentals |
| 5 | Teaching to test understanding |
| 6 | Communities worth joining |
| 7 | Tracking what you learned |
| 8 | Avoiding tutorial hell |
| 9 | Depth-first on one area per quarter |
| 10 | Your personal curriculum for year two |

---

## 1. Choosing sources worth your attention

Attention lets every token look at every other token and decide what matters. Each token emits a query, a key and a value; the query-key dot products become weights over the values. Multiple heads let the model attend to several relationships at once.

```python
import numpy as np

def softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)

rng = np.random.default_rng(0)
seq, d = 4, 8
Q, K, V = (rng.normal(size=(seq, d)) for _ in range(3))

scores = Q @ K.T / np.sqrt(d)             # scale keeps softmax out of saturation
mask = np.triu(np.ones((seq, seq)), k=1) * -1e9   # causal: no peeking ahead
weights = softmax(scores + mask)
print(weights.round(3))
print('output shape', (weights @ V).shape)
```

**Remember:** The 1/sqrt(d) scale is not cosmetic — without it softmax saturates and gradients die.

**Common mistake:** Omitting the causal mask in a decoder, so the model trivially cheats by reading the next token.

## 2. A weekly learning cadence

Tutorial hell is watching, not building. The cure is a cadence: read a little, build something small that could fail, and write down what surprised you. Explaining a concept to someone else is the fastest test of whether you actually understand it.

```python
WEEK = {
    'Mon-Tue': 'Read/learn one concept — 45 min each',
    'Wed-Thu': 'Build something small that uses it and can fail',
    'Fri':     'Write 200 words on what surprised you',
    'Sat':     'Review notes from 1, 2 and 4 weeks ago (spaced repetition)',
    'Sun':     'Rest — consolidation is not optional',
}
for day, task in WEEK.items():
    print(f'{day:<9} {task}')
```

**Remember:** If you cannot explain it without notes, you have not learned it — you have watched it.

**Common mistake:** Finishing a tenth course while having shipped nothing anyone else can run.

## 3. Learning by building, not watching

Projects are where the learning sticks. Build a thin end-to-end slice first — load data, train something dumb, evaluate, serve one prediction — then improve one layer at a time. A working baseline on day one beats a perfect model that never ships.

```python
STEPS = [
    '1. Define the decision the model supports and the metric that measures it',
    '2. Get the data; write the loader; assert the schema',
    '3. Dumb baseline (mean / majority class) -> this is the bar',
    '4. Simple model + honest validation split',
    '5. Error analysis: look at 30 wrong predictions by hand',
    '6. Improve the biggest error bucket, not the leaderboard',
    '7. Serve it, log inputs and outputs, monitor drift',
]
for s in STEPS:
    print(s)
```

**Remember:** Spend an hour looking at wrong predictions before you spend a day tuning hyperparameters.

**Common mistake:** Six weeks of feature engineering with no baseline to prove any of it helped.

## 4. Spaced repetition for fundamentals

Tutorial hell is watching, not building. The cure is a cadence: read a little, build something small that could fail, and write down what surprised you. Explaining a concept to someone else is the fastest test of whether you actually understand it.

```python
WEEK = {
    'Mon-Tue': 'Read/learn one concept — 45 min each',
    'Wed-Thu': 'Build something small that uses it and can fail',
    'Fri':     'Write 200 words on what surprised you',
    'Sat':     'Review notes from 1, 2 and 4 weeks ago (spaced repetition)',
    'Sun':     'Rest — consolidation is not optional',
}
for day, task in WEEK.items():
    print(f'{day:<9} {task}')
```

**Remember:** If you cannot explain it without notes, you have not learned it — you have watched it.

**Common mistake:** Finishing a tenth course while having shipped nothing anyone else can run.

## 5. Teaching to test understanding

Tutorial hell is watching, not building. The cure is a cadence: read a little, build something small that could fail, and write down what surprised you. Explaining a concept to someone else is the fastest test of whether you actually understand it.

```python
WEEK = {
    'Mon-Tue': 'Read/learn one concept — 45 min each',
    'Wed-Thu': 'Build something small that uses it and can fail',
    'Fri':     'Write 200 words on what surprised you',
    'Sat':     'Review notes from 1, 2 and 4 weeks ago (spaced repetition)',
    'Sun':     'Rest — consolidation is not optional',
}
for day, task in WEEK.items():
    print(f'{day:<9} {task}')
```

**Remember:** If you cannot explain it without notes, you have not learned it — you have watched it.

**Common mistake:** Finishing a tenth course while having shipped nothing anyone else can run.

## 6. Communities worth joining

A DataFrame is a table with labelled columns and an index. Most real ML work is 80% reshaping tables: load, clean, group, join, aggregate. Learn `groupby` and `merge` well and you can answer most data questions without writing loops.

```python
import pandas as pd

df = pd.DataFrame({
    'city': ['pune', 'pune', 'delhi', 'delhi'],
    'sales': [10, 20, 5, 7],
})
print(df.groupby('city')['sales'].sum())

lookup = pd.DataFrame({'city': ['pune', 'delhi'], 'zone': ['west', 'north']})
print(df.merge(lookup, on='city', how='left'))
```

**Remember:** Always check `df.shape` before and after a merge — a silent row explosion means duplicate keys.

**Common mistake:** Chained assignment (`df[df.a > 1]['b'] = 0`) that writes to a copy and changes nothing.

## 7. Tracking what you learned

Tutorial hell is watching, not building. The cure is a cadence: read a little, build something small that could fail, and write down what surprised you. Explaining a concept to someone else is the fastest test of whether you actually understand it.

```python
WEEK = {
    'Mon-Tue': 'Read/learn one concept — 45 min each',
    'Wed-Thu': 'Build something small that uses it and can fail',
    'Fri':     'Write 200 words on what surprised you',
    'Sat':     'Review notes from 1, 2 and 4 weeks ago (spaced repetition)',
    'Sun':     'Rest — consolidation is not optional',
}
for day, task in WEEK.items():
    print(f'{day:<9} {task}')
```

**Remember:** If you cannot explain it without notes, you have not learned it — you have watched it.

**Common mistake:** Finishing a tenth course while having shipped nothing anyone else can run.

## 8. Avoiding tutorial hell

Tutorial hell is watching, not building. The cure is a cadence: read a little, build something small that could fail, and write down what surprised you. Explaining a concept to someone else is the fastest test of whether you actually understand it.

```python
WEEK = {
    'Mon-Tue': 'Read/learn one concept — 45 min each',
    'Wed-Thu': 'Build something small that uses it and can fail',
    'Fri':     'Write 200 words on what surprised you',
    'Sat':     'Review notes from 1, 2 and 4 weeks ago (spaced repetition)',
    'Sun':     'Rest — consolidation is not optional',
}
for day, task in WEEK.items():
    print(f'{day:<9} {task}')
```

**Remember:** If you cannot explain it without notes, you have not learned it — you have watched it.

**Common mistake:** Finishing a tenth course while having shipped nothing anyone else can run.

## 9. Depth-first on one area per quarter

Tutorial hell is watching, not building. The cure is a cadence: read a little, build something small that could fail, and write down what surprised you. Explaining a concept to someone else is the fastest test of whether you actually understand it.

```python
WEEK = {
    'Mon-Tue': 'Read/learn one concept — 45 min each',
    'Wed-Thu': 'Build something small that uses it and can fail',
    'Fri':     'Write 200 words on what surprised you',
    'Sat':     'Review notes from 1, 2 and 4 weeks ago (spaced repetition)',
    'Sun':     'Rest — consolidation is not optional',
}
for day, task in WEEK.items():
    print(f'{day:<9} {task}')
```

**Remember:** If you cannot explain it without notes, you have not learned it — you have watched it.

**Common mistake:** Finishing a tenth course while having shipped nothing anyone else can run.

## 10. Your personal curriculum for year two

Tutorial hell is watching, not building. The cure is a cadence: read a little, build something small that could fail, and write down what surprised you. Explaining a concept to someone else is the fastest test of whether you actually understand it.

```python
WEEK = {
    'Mon-Tue': 'Read/learn one concept — 45 min each',
    'Wed-Thu': 'Build something small that uses it and can fail',
    'Fri':     'Write 200 words on what surprised you',
    'Sat':     'Review notes from 1, 2 and 4 weeks ago (spaced repetition)',
    'Sun':     'Rest — consolidation is not optional',
}
for day, task in WEEK.items():
    print(f'{day:<9} {task}')
```

**Remember:** If you cannot explain it without notes, you have not learned it — you have watched it.

**Common mistake:** Finishing a tenth course while having shipped nothing anyone else can run.

---

## What you should be able to do after Day 199

- Explain **Choosing sources worth your attention** to someone else without notes.
- Explain **A weekly learning cadence** to someone else without notes.
- Explain **Learning by building, not watching** to someone else without notes.
- Explain **Spaced repetition for fundamentals** to someone else without notes.
- Explain **Teaching to test understanding** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
