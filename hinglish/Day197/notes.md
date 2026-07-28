# Day 197 — The AI job landscape

Aaj ka goal: **The AI job landscape** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Research scientist vs ML engineer vs data scientist |
| 2 | AI engineer and the LLM application role |
| 3 | Data engineer and platform roles |
| 4 | What each role actually does daily |
| 5 | Skills that transfer between them |
| 6 | Domain specialisation as leverage |
| 7 | Startup vs enterprise trade-offs |
| 8 | Building a portfolio for a target role |
| 9 | Open source contributions |
| 10 | Choosing your next two years |

---

## 1. Research scientist vs ML engineer vs data scientist

### Aasaan Bhasha

ML code ko baaki code jaise tests chahiye, plus data tests: schema, ranges, null rates, class balance. Har known failure mode ke liye ek behavioural test jodo — ek test jo pichhli baar ka outage pakad leta, wo 90% coverage se zyada keemti hai.

### Chhota code

```python
import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()
```

**Yaad rakho:** Data contract test karo, sirf function nahi — kharab data kharab code se zyada models todta hai.

**Aam galti:** Sirf happy path test karna, jisse poora-null column chupchap constant model train kar deta hai.

Practice: `examples/01_research_scientist_vs_ml_engineer_vs_dat.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. AI engineer and the LLM application role

### Aasaan Bhasha

Roles algorithms me kam, aur is baat me zyada alag hain ki din kahan jaata hai: research experiments par, ML engineering pipelines aur serving par, AI engineering prompts, retrieval aur evals par, data engineering us plumbing par jis par baaki sab tika hai. Wo din chuno jo aap jeena chahte ho, wo title nahi jo achha lagta ho.

### Chhota code

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Yaad rakho:** Ek project jise aap end-to-end defend kar sako, aapke CV par das tutorials se bhaari hai.

**Aam galti:** Sabse oonchi salary wale title ke peeche bhaag kar aisa kaam lena jo aapko har roz uba deta hai.

Practice: `examples/02_ai_engineer_and_the_llm_application_role.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Data engineer and platform roles

### Aasaan Bhasha

Roles algorithms me kam, aur is baat me zyada alag hain ki din kahan jaata hai: research experiments par, ML engineering pipelines aur serving par, AI engineering prompts, retrieval aur evals par, data engineering us plumbing par jis par baaki sab tika hai. Wo din chuno jo aap jeena chahte ho, wo title nahi jo achha lagta ho.

### Chhota code

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Yaad rakho:** Ek project jise aap end-to-end defend kar sako, aapke CV par das tutorials se bhaari hai.

**Aam galti:** Sabse oonchi salary wale title ke peeche bhaag kar aisa kaam lena jo aapko har roz uba deta hai.

Practice: `examples/03_data_engineer_and_platform_roles.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. What each role actually does daily

### Aasaan Bhasha

Roles algorithms me kam, aur is baat me zyada alag hain ki din kahan jaata hai: research experiments par, ML engineering pipelines aur serving par, AI engineering prompts, retrieval aur evals par, data engineering us plumbing par jis par baaki sab tika hai. Wo din chuno jo aap jeena chahte ho, wo title nahi jo achha lagta ho.

### Chhota code

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Yaad rakho:** Ek project jise aap end-to-end defend kar sako, aapke CV par das tutorials se bhaari hai.

**Aam galti:** Sabse oonchi salary wale title ke peeche bhaag kar aisa kaam lena jo aapko har roz uba deta hai.

Practice: `examples/04_what_each_role_actually_does_daily.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Skills that transfer between them

### Aasaan Bhasha

Roles algorithms me kam, aur is baat me zyada alag hain ki din kahan jaata hai: research experiments par, ML engineering pipelines aur serving par, AI engineering prompts, retrieval aur evals par, data engineering us plumbing par jis par baaki sab tika hai. Wo din chuno jo aap jeena chahte ho, wo title nahi jo achha lagta ho.

### Chhota code

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Yaad rakho:** Ek project jise aap end-to-end defend kar sako, aapke CV par das tutorials se bhaari hai.

**Aam galti:** Sabse oonchi salary wale title ke peeche bhaag kar aisa kaam lena jo aapko har roz uba deta hai.

Practice: `examples/05_skills_that_transfer_between_them.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Domain specialisation as leverage

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

```python
import numpy as np

docs = [
    'Refunds are processed within 5 business days.',
    'Our office is in Pune, open 9am to 6pm.',
    'Enterprise plans include a dedicated support engineer.',
]

def fake_embed(text):                       # stand-in for a real embedding model
    rng = np.random.default_rng(abs(hash(text)) % (2 ** 32))
    v = rng.normal(size=32)
    return v / np.linalg.norm(v)

index = np.array([fake_embed(d) for d in docs])
q = fake_embed('how long do refunds take')
top = int(np.argmax(index @ q))
print('retrieved:', docs[top])
print('\\nReal pipeline: chunk 300-800 tokens with overlap -> embed -> ANN index -> rerank -> prompt.')
```

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/06_domain_specialisation_as_leverage.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Startup vs enterprise trade-offs

### Aasaan Bhasha

Roles algorithms me kam, aur is baat me zyada alag hain ki din kahan jaata hai: research experiments par, ML engineering pipelines aur serving par, AI engineering prompts, retrieval aur evals par, data engineering us plumbing par jis par baaki sab tika hai. Wo din chuno jo aap jeena chahte ho, wo title nahi jo achha lagta ho.

### Chhota code

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Yaad rakho:** Ek project jise aap end-to-end defend kar sako, aapke CV par das tutorials se bhaari hai.

**Aam galti:** Sabse oonchi salary wale title ke peeche bhaag kar aisa kaam lena jo aapko har roz uba deta hai.

Practice: `examples/07_startup_vs_enterprise_trade_offs.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Building a portfolio for a target role

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

Practice: `examples/08_building_a_portfolio_for_a_target_role.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Open source contributions

### Aasaan Bhasha

Roles algorithms me kam, aur is baat me zyada alag hain ki din kahan jaata hai: research experiments par, ML engineering pipelines aur serving par, AI engineering prompts, retrieval aur evals par, data engineering us plumbing par jis par baaki sab tika hai. Wo din chuno jo aap jeena chahte ho, wo title nahi jo achha lagta ho.

### Chhota code

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Yaad rakho:** Ek project jise aap end-to-end defend kar sako, aapke CV par das tutorials se bhaari hai.

**Aam galti:** Sabse oonchi salary wale title ke peeche bhaag kar aisa kaam lena jo aapko har roz uba deta hai.

Practice: `examples/09_open_source_contributions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Choosing your next two years

### Aasaan Bhasha

Roles algorithms me kam, aur is baat me zyada alag hain ki din kahan jaata hai: research experiments par, ML engineering pipelines aur serving par, AI engineering prompts, retrieval aur evals par, data engineering us plumbing par jis par baaki sab tika hai. Wo din chuno jo aap jeena chahte ho, wo title nahi jo achha lagta ho.

### Chhota code

```python
ROLES = {
    'Research scientist': 'novel methods, papers, experiments — mostly large labs',
    'ML engineer':        'training pipelines, serving, monitoring, scale',
    'AI engineer':        'LLM apps: prompts, RAG, agents, evals, product surface',
    'Data engineer':      'ingestion, warehouses, contracts — the foundation',
    'Data scientist':     'analysis, experiments, decisions — often no deployed model',
}
for role, day in ROLES.items():
    print(f'{role:<20} {day}')
```

**Yaad rakho:** Ek project jise aap end-to-end defend kar sako, aapke CV par das tutorials se bhaari hai.

**Aam galti:** Sabse oonchi salary wale title ke peeche bhaag kar aisa kaam lena jo aapko har roz uba deta hai.

Practice: `examples/10_choosing_your_next_two_years.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 197 ke baad aapko ye aana chahiye

- **Research scientist vs ML engineer vs data scientist** ko bina notes dekhe kisi dost ko samjha sakna.
- **AI engineer and the LLM application role** ko bina notes dekhe kisi dost ko samjha sakna.
- **Data engineer and platform roles** ko bina notes dekhe kisi dost ko samjha sakna.
- **What each role actually does daily** ko bina notes dekhe kisi dost ko samjha sakna.
- **Skills that transfer between them** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
