# Day 109 — Face and person understanding

Today's goal: work through **Face and person understanding** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Face detection vs recognition |
| 2 | Face embeddings and verification |
| 3 | Landmark detection |
| 4 | Pose estimation |
| 5 | Person re-identification |
| 6 | Bias in face datasets |
| 7 | Privacy and consent |
| 8 | Legal restrictions by jurisdiction |
| 9 | When to refuse to build it |
| 10 | Safer alternatives to face recognition |

---

## 1. Face detection vs recognition

Face technology is technically routine and legally and ethically loaded. Detection (is there a face) is far less sensitive than recognition (whose face). Many jurisdictions restrict biometric processing outright. Ask whether a non-biometric signal — a badge scan, a session token — answers the same business question.

```python
DECISION = [
    ('Do you need identity, or just presence?', 'presence -> use detection only, never enrol identities'),
    ('Is there a lawful basis and explicit consent?', 'no -> stop'),
    ('Can a badge/QR/login answer this?', 'yes -> use that instead'),
    ('Retention period defined and enforced?', 'no -> stop'),
    ('Error rates measured per demographic group?', 'no -> measure before deploying'),
]
for q, a in DECISION:
    print(f'- {q}\n    -> {a}')
```

**Remember:** Biometric data usually cannot be revoked. Treat it as the most sensitive category you handle.

**Common mistake:** Building face recognition because the API was easy, without a lawful basis or a retention policy.

Practice: open `examples/01_face_detection_vs_recognition.py`, predict the output, change one line, predict again.

## 2. Face embeddings and verification

An embedding maps text to a dense vector where nearby means similar in meaning. Unlike keyword search, 'car trouble' matches 'engine won't start'. Every RAG system is embeddings plus nearest-neighbour lookup.

```python
import numpy as np

# Toy 3-D 'embeddings' to show the mechanics
vecs = {
    'king':  np.array([0.9, 0.8, 0.1]),
    'queen': np.array([0.9, 0.1, 0.8]),
    'man':   np.array([0.4, 0.9, 0.1]),
    'woman': np.array([0.4, 0.1, 0.9]),
}

def cos(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))

analogy = vecs['king'] - vecs['man'] + vecs['woman']
best = max(vecs, key=lambda w: cos(analogy, vecs[w]) if w != 'king' else -1)
print('king - man + woman ~', best)
```

**Remember:** Normalise embeddings, then cosine similarity is just a dot product — much faster at scale.

**Common mistake:** Mixing vectors from two different embedding models in one index; the spaces are unrelated.

Practice: open `examples/02_face_embeddings_and_verification.py`, predict the output, change one line, predict again.

## 3. Landmark detection

Face technology is technically routine and legally and ethically loaded. Detection (is there a face) is far less sensitive than recognition (whose face). Many jurisdictions restrict biometric processing outright. Ask whether a non-biometric signal — a badge scan, a session token — answers the same business question.

```python
DECISION = [
    ('Do you need identity, or just presence?', 'presence -> use detection only, never enrol identities'),
    ('Is there a lawful basis and explicit consent?', 'no -> stop'),
    ('Can a badge/QR/login answer this?', 'yes -> use that instead'),
    ('Retention period defined and enforced?', 'no -> stop'),
    ('Error rates measured per demographic group?', 'no -> measure before deploying'),
]
for q, a in DECISION:
    print(f'- {q}\n    -> {a}')
```

**Remember:** Biometric data usually cannot be revoked. Treat it as the most sensitive category you handle.

**Common mistake:** Building face recognition because the API was easy, without a lawful basis or a retention policy.

Practice: open `examples/03_landmark_detection.py`, predict the output, change one line, predict again.

## 4. Pose estimation

Face technology is technically routine and legally and ethically loaded. Detection (is there a face) is far less sensitive than recognition (whose face). Many jurisdictions restrict biometric processing outright. Ask whether a non-biometric signal — a badge scan, a session token — answers the same business question.

```python
DECISION = [
    ('Do you need identity, or just presence?', 'presence -> use detection only, never enrol identities'),
    ('Is there a lawful basis and explicit consent?', 'no -> stop'),
    ('Can a badge/QR/login answer this?', 'yes -> use that instead'),
    ('Retention period defined and enforced?', 'no -> stop'),
    ('Error rates measured per demographic group?', 'no -> measure before deploying'),
]
for q, a in DECISION:
    print(f'- {q}\n    -> {a}')
```

**Remember:** Biometric data usually cannot be revoked. Treat it as the most sensitive category you handle.

**Common mistake:** Building face recognition because the API was easy, without a lawful basis or a retention policy.

Practice: open `examples/04_pose_estimation.py`, predict the output, change one line, predict again.

## 5. Person re-identification

Face technology is technically routine and legally and ethically loaded. Detection (is there a face) is far less sensitive than recognition (whose face). Many jurisdictions restrict biometric processing outright. Ask whether a non-biometric signal — a badge scan, a session token — answers the same business question.

```python
DECISION = [
    ('Do you need identity, or just presence?', 'presence -> use detection only, never enrol identities'),
    ('Is there a lawful basis and explicit consent?', 'no -> stop'),
    ('Can a badge/QR/login answer this?', 'yes -> use that instead'),
    ('Retention period defined and enforced?', 'no -> stop'),
    ('Error rates measured per demographic group?', 'no -> measure before deploying'),
]
for q, a in DECISION:
    print(f'- {q}\n    -> {a}')
```

**Remember:** Biometric data usually cannot be revoked. Treat it as the most sensitive category you handle.

**Common mistake:** Building face recognition because the API was easy, without a lawful basis or a retention policy.

Practice: open `examples/05_person_re_identification.py`, predict the output, change one line, predict again.

## 6. Bias in face datasets

Models learn the bias in their training data and then apply it at scale with a veneer of objectivity. Measure error rates per group, not just overall. Fairness definitions genuinely conflict with each other — you must choose one explicitly and document why.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'group': ['a'] * 100 + ['b'] * 100,
    'y':     [1] * 50 + [0] * 50 + [1] * 50 + [0] * 50,
    'pred':  [1] * 45 + [0] * 55 + [1] * 30 + [0] * 70,
})
for g, sub in df.groupby('group'):
    tpr = ((sub.pred == 1) & (sub.y == 1)).sum() / max((sub.y == 1).sum(), 1)
    rate = (sub.pred == 1).mean()
    print(f'group {g}: selection rate {rate:.2f}  recall {tpr:.2f}')
print('Large gaps here are the finding — investigate before shipping.')
```

**Remember:** Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

**Common mistake:** Auditing fairness once at launch and never again as the data drifts.

Practice: open `examples/06_bias_in_face_datasets.py`, predict the output, change one line, predict again.

## 7. Privacy and consent

Models learn the bias in their training data and then apply it at scale with a veneer of objectivity. Measure error rates per group, not just overall. Fairness definitions genuinely conflict with each other — you must choose one explicitly and document why.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'group': ['a'] * 100 + ['b'] * 100,
    'y':     [1] * 50 + [0] * 50 + [1] * 50 + [0] * 50,
    'pred':  [1] * 45 + [0] * 55 + [1] * 30 + [0] * 70,
})
for g, sub in df.groupby('group'):
    tpr = ((sub.pred == 1) & (sub.y == 1)).sum() / max((sub.y == 1).sum(), 1)
    rate = (sub.pred == 1).mean()
    print(f'group {g}: selection rate {rate:.2f}  recall {tpr:.2f}')
print('Large gaps here are the finding — investigate before shipping.')
```

**Remember:** Dropping the sensitive attribute does not remove bias; proxies (pincode, name) carry it right back in.

**Common mistake:** Auditing fairness once at launch and never again as the data drifts.

Practice: open `examples/07_privacy_and_consent.py`, predict the output, change one line, predict again.

## 8. Legal restrictions by jurisdiction

Face technology is technically routine and legally and ethically loaded. Detection (is there a face) is far less sensitive than recognition (whose face). Many jurisdictions restrict biometric processing outright. Ask whether a non-biometric signal — a badge scan, a session token — answers the same business question.

```python
DECISION = [
    ('Do you need identity, or just presence?', 'presence -> use detection only, never enrol identities'),
    ('Is there a lawful basis and explicit consent?', 'no -> stop'),
    ('Can a badge/QR/login answer this?', 'yes -> use that instead'),
    ('Retention period defined and enforced?', 'no -> stop'),
    ('Error rates measured per demographic group?', 'no -> measure before deploying'),
]
for q, a in DECISION:
    print(f'- {q}\n    -> {a}')
```

**Remember:** Biometric data usually cannot be revoked. Treat it as the most sensitive category you handle.

**Common mistake:** Building face recognition because the API was easy, without a lawful basis or a retention policy.

Practice: open `examples/08_legal_restrictions_by_jurisdiction.py`, predict the output, change one line, predict again.

## 9. When to refuse to build it

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

Practice: open `examples/09_when_to_refuse_to_build_it.py`, predict the output, change one line, predict again.

## 10. Safer alternatives to face recognition

Face technology is technically routine and legally and ethically loaded. Detection (is there a face) is far less sensitive than recognition (whose face). Many jurisdictions restrict biometric processing outright. Ask whether a non-biometric signal — a badge scan, a session token — answers the same business question.

```python
DECISION = [
    ('Do you need identity, or just presence?', 'presence -> use detection only, never enrol identities'),
    ('Is there a lawful basis and explicit consent?', 'no -> stop'),
    ('Can a badge/QR/login answer this?', 'yes -> use that instead'),
    ('Retention period defined and enforced?', 'no -> stop'),
    ('Error rates measured per demographic group?', 'no -> measure before deploying'),
]
for q, a in DECISION:
    print(f'- {q}\n    -> {a}')
```

**Remember:** Biometric data usually cannot be revoked. Treat it as the most sensitive category you handle.

**Common mistake:** Building face recognition because the API was easy, without a lawful basis or a retention policy.

Practice: open `examples/10_safer_alternatives_to_face_recognition.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 109

- Explain **Face detection vs recognition** to someone else without notes.
- Explain **Face embeddings and verification** to someone else without notes.
- Explain **Landmark detection** to someone else without notes.
- Explain **Pose estimation** to someone else without notes.
- Explain **Person re-identification** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
