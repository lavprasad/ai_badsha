# Day 143 — Reasoning and thinking models

Aaj ka goal: **Reasoning and thinking models** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Chain-of-thought prompting |
| 2 | Self-consistency |
| 3 | Extended thinking modes |
| 4 | Tree and graph of thought |
| 5 | Tool use as reasoning support |
| 6 | Verification and self-critique |
| 7 | Where reasoning helps and where it wastes tokens |
| 8 | Reasoning token cost |
| 9 | Reading a reasoning trace critically |
| 10 | Choosing a reasoning budget |

---

## 1. Chain-of-thought prompting

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

Practice: `examples/01_chain_of_thought_prompting.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Self-consistency

### Aasaan Bhasha

Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.

### Chhota code

```python
from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')
```

**Yaad rakho:** Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.

**Aam galti:** Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.

Practice: `examples/02_self_consistency.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Extended thinking modes

### Aasaan Bhasha

Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.

### Chhota code

```python
from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')
```

**Yaad rakho:** Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.

**Aam galti:** Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.

Practice: `examples/03_extended_thinking_modes.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Tree and graph of thought

### Aasaan Bhasha

Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.

### Chhota code

```python
from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')
```

**Yaad rakho:** Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.

**Aam galti:** Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.

Practice: `examples/04_tree_and_graph_of_thought.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Tool use as reasoning support

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

Practice: `examples/05_tool_use_as_reasoning_support.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Verification and self-critique

### Aasaan Bhasha

Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.

### Chhota code

```python
from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')
```

**Yaad rakho:** Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.

**Aam galti:** Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.

Practice: `examples/06_verification_and_self_critique.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Where reasoning helps and where it wastes tokens

### Aasaan Bhasha

Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.

### Chhota code

```python
from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')
```

**Yaad rakho:** Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.

**Aam galti:** Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.

Practice: `examples/07_where_reasoning_helps_and_where_it_waste.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Reasoning token cost

### Aasaan Bhasha

Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.

### Chhota code

```python
from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')
```

**Yaad rakho:** Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.

**Aam galti:** Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.

Practice: `examples/08_reasoning_token_cost.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Reading a reasoning trace critically

### Aasaan Bhasha

Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.

### Chhota code

```python
from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')
```

**Yaad rakho:** Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.

**Aam galti:** Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.

Practice: `examples/09_reading_a_reasoning_trace_critically.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Choosing a reasoning budget

### Aasaan Bhasha

Reasoning modes tokens ke badle accuracy dete hain. Wo multi-step problems par madad karte hain jinka jawab verify ho sakta hai, aur lookup ya formatting tasks par paisa barbaad karte hain. Self-consistency — kai jawab sample karke majority lena — jab jawab compare ho sakte hon to sasta accuracy boost hai.

### Chhota code

```python
from collections import Counter

def self_consistency(samples):
    counts = Counter(samples)
    answer, votes = counts.most_common(1)[0]
    return answer, votes / len(samples)

print(self_consistency(['42', '42', '17', '42', '43']))

USE_REASONING = {
    'multi-step arithmetic / planning': True,
    'code with a failing test to fix': True,
    'reformat this JSON': False,
    'classify sentiment': False,
}
for task, use in USE_REASONING.items():
    print(f'{task:<38} -> {"reason" if use else "direct answer"}')
```

**Yaad rakho:** Reasoning trace koi sabooot nahi hai. Likha hua reasoning galat ho sakta hai jabki jawab sahi ho, aur ulta bhi.

**Aam galti:** Extended thinking globally chaalu kar dena aur un tasks par cost teen guna kar dena jinhe ek reasoning token ki bhi zaroorat nahi thi.

Practice: `examples/10_choosing_a_reasoning_budget.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 143 ke baad aapko ye aana chahiye

- **Chain-of-thought prompting** ko bina notes dekhe kisi dost ko samjha sakna.
- **Self-consistency** ko bina notes dekhe kisi dost ko samjha sakna.
- **Extended thinking modes** ko bina notes dekhe kisi dost ko samjha sakna.
- **Tree and graph of thought** ko bina notes dekhe kisi dost ko samjha sakna.
- **Tool use as reasoning support** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
