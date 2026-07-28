# Day 148 — LLM APIs in code

Aaj ka goal: **LLM APIs in code** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Anatomy of a chat completion request |
| 2 | System prompts and message roles |
| 3 | max_tokens and stop conditions |
| 4 | Streaming responses |
| 5 | Retries, timeouts and backoff |
| 6 | Rate limits and concurrency |
| 7 | Cost tracking per request |
| 8 | Prompt caching for stable prefixes |
| 9 | Structured outputs and tool schemas |
| 10 | A resilient API client wrapper |

---

## 1. Anatomy of a chat completion request

### Aasaan Bhasha

Model tak jaane wala koi bhi network call kabhi na kabhi timeout hoga, rate-limit hoga, ya kharab output dega. Production client ko timeouts, bounded retries with exponential backoff aur jitter, concurrency cap, aur per-request cost logging chahiye. Ek baar likho aur har jagah use karo.

### Chhota code

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Yaad rakho:** Jitter zaroori hai: uske bina har client ek hi pal me retry karta hai aur outage dobara bana deta hai.

**Aam galti:** 400-class error par infinite retries, jo kabhi safal nahi hoga, aur API aur budget dono par hathoda chalta rehta hai.

Practice: `examples/01_anatomy_of_a_chat_completion_request.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. System prompts and message roles

### Aasaan Bhasha

Prompt English me likha gaya program hai. Role, task, format aur constraints ke baare me specific raho. Few-shot examples format kisi bhi description se behtar sikhaate hain. Reasoning steps maangna multi-step problems par madad karta hai aur simple lookups par tokens barbaad karta hai.

### Chhota code

```python
prompt = '''You are a support triage assistant.

Classify the ticket into exactly one of: BILLING, BUG, FEATURE, OTHER.
Return JSON only: {"label": ..., "confidence": 0.0-1.0}

Examples:
Ticket: "charged twice this month" -> {"label": "BILLING", "confidence": 0.95}
Ticket: "app crashes on upload"    -> {"label": "BUG", "confidence": 0.92}

Ticket: "can you add dark mode?"
'''
print(prompt)
print('Structure: role -> task -> allowed outputs -> format -> examples -> input.')
```

**Yaad rakho:** Output format sabse aakhir me rakho aur use example ki tarah dikhao — models sabse paas wala pattern copy karte hain.

**Aam galti:** Dhundhla prompt likhna, dhundhla output paana, aur model ko dosh dena.

Practice: `examples/02_system_prompts_and_message_roles.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. max_tokens and stop conditions

### Aasaan Bhasha

Generation ek loop hai: distribution predict karo, token chuno, jodo, dohrao. Greedy deterministic aur repetitive hai; sampling variety wala aur risky. Stop sequences aur max_tokens aapke circuit breakers hain — inke bina ek loop tab tak chal sakta hai jab tak aapka budget khatm na ho jaaye.

### Chhota code

```python
import numpy as np

def generate(next_dist, max_tokens=20, stop=('.',), greedy=True, seed=0):
    rng = np.random.default_rng(seed)
    out = []
    for _ in range(max_tokens):
        tokens, probs = next_dist(out)
        tok = tokens[int(np.argmax(probs))] if greedy else rng.choice(tokens, p=probs)
        out.append(tok)
        if tok in stop:
            break
    return ''.join(out)

vocab = list('abc.')
dist = lambda hist: (vocab, np.array([0.4, 0.3, 0.2, 0.1]))
print('greedy :', generate(dist))
print('sampled:', generate(dist, greedy=False))
```

**Yaad rakho:** max_tokens aur stop sequences hamesha set karo. Yahi bug aur bill ke beech ka farq hai.

**Aam galti:** Retry loop par max_tokens unbounded chhod dena aur raat bhar me mahine ka budget jala dena.

Practice: `examples/03_max_tokens_and_stop_conditions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Streaming responses

### Aasaan Bhasha

Temperature 0 lagbhag deterministic hai aur extraction ke liye sahi; zyada values creative kaam ke liye variety deti hain. Top-p sabse chhota set rakhta hai jo probability mass ka p cover kare. Cost per token in aur out hai, isliye prompt chhota karna sabse sasta optimisation hai.

### Chhota code

```python
import numpy as np

def sample(logits, temperature=1.0, top_p=0.9, seed=0):
    z = np.array(logits) / max(temperature, 1e-6)
    p = np.exp(z - z.max())
    p /= p.sum()
    order = np.argsort(-p)
    keep = order[:max(1, int(np.searchsorted(np.cumsum(p[order]), top_p) + 1))]
    p2 = p[keep] / p[keep].sum()
    return int(np.random.default_rng(seed).choice(keep, p=p2))

logits = [3.0, 2.0, 1.0, 0.5]
print('greedy-ish (T=0.1):', sample(logits, temperature=0.1))
print('creative  (T=1.5):', sample(logits, temperature=1.5, seed=3))
```

**Yaad rakho:** Jise aap parse karoge uske liye temperature 0 use karo; randomness prose ke liye bachaao.

**Aam galti:** Temperature 1 par extraction chala kar hafte bhar 'random' JSON failures debug karna.

Practice: `examples/04_streaming_responses.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Retries, timeouts and backoff

### Aasaan Bhasha

Model tak jaane wala koi bhi network call kabhi na kabhi timeout hoga, rate-limit hoga, ya kharab output dega. Production client ko timeouts, bounded retries with exponential backoff aur jitter, concurrency cap, aur per-request cost logging chahiye. Ek baar likho aur har jagah use karo.

### Chhota code

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Yaad rakho:** Jitter zaroori hai: uske bina har client ek hi pal me retry karta hai aur outage dobara bana deta hai.

**Aam galti:** 400-class error par infinite retries, jo kabhi safal nahi hoga, aur API aur budget dono par hathoda chalta rehta hai.

Practice: `examples/05_retries_timeouts_and_backoff.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Rate limits and concurrency

### Aasaan Bhasha

Model tak jaane wala koi bhi network call kabhi na kabhi timeout hoga, rate-limit hoga, ya kharab output dega. Production client ko timeouts, bounded retries with exponential backoff aur jitter, concurrency cap, aur per-request cost logging chahiye. Ek baar likho aur har jagah use karo.

### Chhota code

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Yaad rakho:** Jitter zaroori hai: uske bina har client ek hi pal me retry karta hai aur outage dobara bana deta hai.

**Aam galti:** 400-class error par infinite retries, jo kabhi safal nahi hoga, aur API aur budget dono par hathoda chalta rehta hai.

Practice: `examples/06_rate_limits_and_concurrency.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Cost tracking per request

### Aasaan Bhasha

Model tak jaane wala koi bhi network call kabhi na kabhi timeout hoga, rate-limit hoga, ya kharab output dega. Production client ko timeouts, bounded retries with exponential backoff aur jitter, concurrency cap, aur per-request cost logging chahiye. Ek baar likho aur har jagah use karo.

### Chhota code

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Yaad rakho:** Jitter zaroori hai: uske bina har client ek hi pal me retry karta hai aur outage dobara bana deta hai.

**Aam galti:** 400-class error par infinite retries, jo kabhi safal nahi hoga, aur API aur budget dono par hathoda chalta rehta hai.

Practice: `examples/07_cost_tracking_per_request.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Prompt caching for stable prefixes

### Aasaan Bhasha

Messages API ek system prompt plus alternating user/assistant turns leta hai aur content blocks lautata hai. Stable content (lambi instructions, retrieved corpora) shuru me rakho aur use cacheable mark karo — cache hits latency aur cost dono kaafi kam kar dete hain. Jab insaan intezaar kar raha ho to stream karo.

### Chhota code

```python
# pip install anthropic ; export ANTHROPIC_API_KEY=...
# import anthropic
# client = anthropic.Anthropic()
# resp = client.messages.create(
#     model='claude-sonnet-5',
#     max_tokens=1024,
#     system=[{'type': 'text', 'text': LONG_STABLE_INSTRUCTIONS,
#              'cache_control': {'type': 'ephemeral'}}],
#     messages=[{'role': 'user', 'content': 'Summarise the attached policy.'}],
# )
# print(resp.content[0].text)
print('Stable prefix first + cache_control -> cheaper, faster repeat calls.')
```

**Yaad rakho:** API key kabhi hard-code mat karo. Use environment se padho aur git se door rakho.

**Aam galti:** Har call me prompt ka order badalna, jisse cache kabhi hit hi nahi hota.

Practice: `examples/08_prompt_caching_for_stable_prefixes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Structured outputs and tool schemas

### Aasaan Bhasha

Free text parse karna mushkil hai; iske bajaye schema ke against JSON maango. Tool/function calling ise formal bana deta hai: aap callable functions batate ho, model structured call lautata hai, aapka code use chalata hai aur result wapas deta hai. Output par act karne se pehle hamesha validate karo.

### Chhota code

```python
import json

TOOL = {
    'name': 'get_weather',
    'description': 'Current weather for a city',
    'input_schema': {
        'type': 'object',
        'properties': {'city': {'type': 'string'}, 'unit': {'type': 'string', 'enum': ['c', 'f']}},
        'required': ['city'],
    },
}

model_output = '{"city": "Pune", "unit": "c"}'
try:
    args = json.loads(model_output)
    assert 'city' in args, 'missing required field: city'
    print('validated call ->', TOOL['name'], args)
except (json.JSONDecodeError, AssertionError) as e:
    print('reject and retry:', e)
```

**Yaad rakho:** Model se aaye har payload ko schema ke against validate karo, tab hi wo aapke database tak pahuche.

**Aam galti:** Model output ko seedha `eval`, shell command, ya SQL string me daal dena.

Practice: `examples/09_structured_outputs_and_tool_schemas.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A resilient API client wrapper

### Aasaan Bhasha

Model tak jaane wala koi bhi network call kabhi na kabhi timeout hoga, rate-limit hoga, ya kharab output dega. Production client ko timeouts, bounded retries with exponential backoff aur jitter, concurrency cap, aur per-request cost logging chahiye. Ek baar likho aur har jagah use karo.

### Chhota code

```python
import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))
```

**Yaad rakho:** Jitter zaroori hai: uske bina har client ek hi pal me retry karta hai aur outage dobara bana deta hai.

**Aam galti:** 400-class error par infinite retries, jo kabhi safal nahi hoga, aur API aur budget dono par hathoda chalta rehta hai.

Practice: `examples/10_a_resilient_api_client_wrapper.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 148 ke baad aapko ye aana chahiye

- **Anatomy of a chat completion request** ko bina notes dekhe kisi dost ko samjha sakna.
- **System prompts and message roles** ko bina notes dekhe kisi dost ko samjha sakna.
- **max_tokens and stop conditions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Streaming responses** ko bina notes dekhe kisi dost ko samjha sakna.
- **Retries, timeouts and backoff** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
