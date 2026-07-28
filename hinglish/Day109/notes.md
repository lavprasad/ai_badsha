# Day 109 — Face and person understanding

Aaj ka goal: **Face and person understanding** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Face technology technically aam hai aur legally aur ethically bhaari. Detection (chehra hai ya nahi) recognition (kiska chehra) se kahin kam sensitive hai. Kai jagah biometric processing par seedhi rok hai. Poochho ki kya koi non-biometric signal — badge scan, session token — wahi business sawaal hal kar deta hai.

### Chhota code

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

**Yaad rakho:** Biometric data aam taur par revoke nahi ho sakta. Use apni sabse sensitive category maano.

**Aam galti:** Face recognition isliye banana ki API aasan tha, bina lawful basis aur bina retention policy ke.

Practice: `examples/01_face_detection_vs_recognition.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Face embeddings and verification

### Aasaan Bhasha

Embedding text ko dense vector me badalta hai jahan paas hona matlab matlab me paas hona. Keyword search ke ulat, 'car trouble' 'engine won't start' se match ho jaata hai. Har RAG system embeddings + nearest-neighbour lookup hi hai.

### Chhota code

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

**Yaad rakho:** Embeddings normalise kar do, phir cosine similarity sirf dot product hai — scale par bahut tez.

**Aam galti:** Ek hi index me do alag embedding models ke vectors mila dena; wo spaces aapas me bilkul unrelated hain.

Practice: `examples/02_face_embeddings_and_verification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Landmark detection

### Aasaan Bhasha

Face technology technically aam hai aur legally aur ethically bhaari. Detection (chehra hai ya nahi) recognition (kiska chehra) se kahin kam sensitive hai. Kai jagah biometric processing par seedhi rok hai. Poochho ki kya koi non-biometric signal — badge scan, session token — wahi business sawaal hal kar deta hai.

### Chhota code

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

**Yaad rakho:** Biometric data aam taur par revoke nahi ho sakta. Use apni sabse sensitive category maano.

**Aam galti:** Face recognition isliye banana ki API aasan tha, bina lawful basis aur bina retention policy ke.

Practice: `examples/03_landmark_detection.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Pose estimation

### Aasaan Bhasha

Face technology technically aam hai aur legally aur ethically bhaari. Detection (chehra hai ya nahi) recognition (kiska chehra) se kahin kam sensitive hai. Kai jagah biometric processing par seedhi rok hai. Poochho ki kya koi non-biometric signal — badge scan, session token — wahi business sawaal hal kar deta hai.

### Chhota code

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

**Yaad rakho:** Biometric data aam taur par revoke nahi ho sakta. Use apni sabse sensitive category maano.

**Aam galti:** Face recognition isliye banana ki API aasan tha, bina lawful basis aur bina retention policy ke.

Practice: `examples/04_pose_estimation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Person re-identification

### Aasaan Bhasha

Face technology technically aam hai aur legally aur ethically bhaari. Detection (chehra hai ya nahi) recognition (kiska chehra) se kahin kam sensitive hai. Kai jagah biometric processing par seedhi rok hai. Poochho ki kya koi non-biometric signal — badge scan, session token — wahi business sawaal hal kar deta hai.

### Chhota code

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

**Yaad rakho:** Biometric data aam taur par revoke nahi ho sakta. Use apni sabse sensitive category maano.

**Aam galti:** Face recognition isliye banana ki API aasan tha, bina lawful basis aur bina retention policy ke.

Practice: `examples/05_person_re_identification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Bias in face datasets

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/06_bias_in_face_datasets.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Privacy and consent

### Aasaan Bhasha

Models apne training data ka bias seekh lete hain aur phir use objectivity ke mulamme ke saath scale par lagu karte hain. Har group ke error rates naapo, sirf overall nahi. Fairness ki definitions ek doosre se sach me takraati hain — aapko ek explicitly chunni padegi aur wajah likhni padegi.

### Chhota code

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

**Yaad rakho:** Sensitive attribute hataane se bias nahi jaata; proxies (pincode, naam) use wapas le aate hain.

**Aam galti:** Fairness ka audit sirf launch par ek baar karna aur data drift hone par dobara kabhi nahi.

Practice: `examples/07_privacy_and_consent.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Legal restrictions by jurisdiction

### Aasaan Bhasha

Face technology technically aam hai aur legally aur ethically bhaari. Detection (chehra hai ya nahi) recognition (kiska chehra) se kahin kam sensitive hai. Kai jagah biometric processing par seedhi rok hai. Poochho ki kya koi non-biometric signal — badge scan, session token — wahi business sawaal hal kar deta hai.

### Chhota code

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

**Yaad rakho:** Biometric data aam taur par revoke nahi ho sakta. Use apni sabse sensitive category maano.

**Aam galti:** Face recognition isliye banana ki API aasan tha, bina lawful basis aur bina retention policy ke.

Practice: `examples/08_legal_restrictions_by_jurisdiction.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. When to refuse to build it

### Aasaan Bhasha

Projects wahi jagah hain jahan seekha hua chipakta hai. Pehle ek patli end-to-end slice banao — data load, kuch bewakoof train, evaluate, ek prediction serve — phir ek-ek layer sudharo. Pehle din chalne wala baseline us perfect model se behtar hai jo kabhi ship hi nahi hota.

### Chhota code

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

**Yaad rakho:** Hyperparameters tune karne me ek din lagane se pehle galat predictions dekhne me ek ghanta lagao.

**Aam galti:** Chhe hafte feature engineering karna bina kisi baseline ke jo sabit kare ki kisi cheez se fayda hua.

Practice: `examples/09_when_to_refuse_to_build_it.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Safer alternatives to face recognition

### Aasaan Bhasha

Face technology technically aam hai aur legally aur ethically bhaari. Detection (chehra hai ya nahi) recognition (kiska chehra) se kahin kam sensitive hai. Kai jagah biometric processing par seedhi rok hai. Poochho ki kya koi non-biometric signal — badge scan, session token — wahi business sawaal hal kar deta hai.

### Chhota code

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

**Yaad rakho:** Biometric data aam taur par revoke nahi ho sakta. Use apni sabse sensitive category maano.

**Aam galti:** Face recognition isliye banana ki API aasan tha, bina lawful basis aur bina retention policy ke.

Practice: `examples/10_safer_alternatives_to_face_recognition.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 109 ke baad aapko ye aana chahiye

- **Face detection vs recognition** ko bina notes dekhe kisi dost ko samjha sakna.
- **Face embeddings and verification** ko bina notes dekhe kisi dost ko samjha sakna.
- **Landmark detection** ko bina notes dekhe kisi dost ko samjha sakna.
- **Pose estimation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Person re-identification** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
