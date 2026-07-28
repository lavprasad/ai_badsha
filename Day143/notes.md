# Day 143 — Reasoning and thinking models

Today's goal: work through **Reasoning and thinking models** — ten concepts, ten runnable examples, five questions.

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

A prompt is a program written in English. Be specific about role, task, format and constraints. Few-shot examples teach format better than any description. Asking for reasoning steps helps on multi-step problems and wastes tokens on simple lookups.

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

**Remember:** Put the output format last and show it as an example — models copy the nearest pattern.

**Common mistake:** Writing a vague prompt, getting vague output, and blaming the model.

## 2. Self-consistency

Reasoning modes trade tokens for accuracy. They help on multi-step problems with a verifiable answer, and waste money on lookup or formatting tasks. Self-consistency — sample several answers and take the majority — is a cheap accuracy boost when answers are comparable.

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

**Remember:** A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.

**Common mistake:** Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.

## 3. Extended thinking modes

Reasoning modes trade tokens for accuracy. They help on multi-step problems with a verifiable answer, and waste money on lookup or formatting tasks. Self-consistency — sample several answers and take the majority — is a cheap accuracy boost when answers are comparable.

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

**Remember:** A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.

**Common mistake:** Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.

## 4. Tree and graph of thought

Reasoning modes trade tokens for accuracy. They help on multi-step problems with a verifiable answer, and waste money on lookup or formatting tasks. Self-consistency — sample several answers and take the majority — is a cheap accuracy boost when answers are comparable.

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

**Remember:** A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.

**Common mistake:** Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.

## 5. Tool use as reasoning support

Free text is hard to parse; ask for JSON against a schema instead. Tool/function calling formalises this: you describe callable functions, the model returns a structured call, your code executes it and returns the result. Always validate before you act on the output.

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

**Remember:** Validate every model-produced payload against the schema before it reaches your database.

**Common mistake:** Passing model output straight into `eval`, a shell command, or an SQL string.

## 6. Verification and self-critique

Reasoning modes trade tokens for accuracy. They help on multi-step problems with a verifiable answer, and waste money on lookup or formatting tasks. Self-consistency — sample several answers and take the majority — is a cheap accuracy boost when answers are comparable.

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

**Remember:** A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.

**Common mistake:** Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.

## 7. Where reasoning helps and where it wastes tokens

Reasoning modes trade tokens for accuracy. They help on multi-step problems with a verifiable answer, and waste money on lookup or formatting tasks. Self-consistency — sample several answers and take the majority — is a cheap accuracy boost when answers are comparable.

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

**Remember:** A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.

**Common mistake:** Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.

## 8. Reasoning token cost

Reasoning modes trade tokens for accuracy. They help on multi-step problems with a verifiable answer, and waste money on lookup or formatting tasks. Self-consistency — sample several answers and take the majority — is a cheap accuracy boost when answers are comparable.

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

**Remember:** A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.

**Common mistake:** Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.

## 9. Reading a reasoning trace critically

Reasoning modes trade tokens for accuracy. They help on multi-step problems with a verifiable answer, and waste money on lookup or formatting tasks. Self-consistency — sample several answers and take the majority — is a cheap accuracy boost when answers are comparable.

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

**Remember:** A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.

**Common mistake:** Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.

## 10. Choosing a reasoning budget

Reasoning modes trade tokens for accuracy. They help on multi-step problems with a verifiable answer, and waste money on lookup or formatting tasks. Self-consistency — sample several answers and take the majority — is a cheap accuracy boost when answers are comparable.

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

**Remember:** A reasoning trace is not proof. The stated reasoning can be wrong while the answer is right, and vice versa.

**Common mistake:** Enabling extended thinking globally and tripling cost on tasks that never needed a single reasoning token.

---

## What you should be able to do after Day 143

- Explain **Chain-of-thought prompting** to someone else without notes.
- Explain **Self-consistency** to someone else without notes.
- Explain **Extended thinking modes** to someone else without notes.
- Explain **Tree and graph of thought** to someone else without notes.
- Explain **Tool use as reasoning support** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
