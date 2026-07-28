# Day 146 — Prompt engineering foundations

Today's goal: work through **Prompt engineering foundations** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | A prompt is a specification |
| 2 | Role, task, constraints, format |
| 3 | Zero-shot vs few-shot |
| 4 | Example selection matters |
| 5 | Delimiters and structure |
| 6 | Output format specification |
| 7 | Chain-of-thought when useful |
| 8 | Negative instructions and their weakness |
| 9 | Iterating with a test set |
| 10 | Versioning prompts like code |

---

## 1. A prompt is a specification

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

Practice: open `examples/01_a_prompt_is_a_specification.py`, predict the output, change one line, predict again.

## 2. Role, task, constraints, format

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

Practice: open `examples/02_role_task_constraints_format.py`, predict the output, change one line, predict again.

## 3. Zero-shot vs few-shot

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

Practice: open `examples/03_zero_shot_vs_few_shot.py`, predict the output, change one line, predict again.

## 4. Example selection matters

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

Practice: open `examples/04_example_selection_matters.py`, predict the output, change one line, predict again.

## 5. Delimiters and structure

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

Practice: open `examples/05_delimiters_and_structure.py`, predict the output, change one line, predict again.

## 6. Output format specification

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

Practice: open `examples/06_output_format_specification.py`, predict the output, change one line, predict again.

## 7. Chain-of-thought when useful

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

Practice: open `examples/07_chain_of_thought_when_useful.py`, predict the output, change one line, predict again.

## 8. Negative instructions and their weakness

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

Practice: open `examples/08_negative_instructions_and_their_weakness.py`, predict the output, change one line, predict again.

## 9. Iterating with a test set

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

Practice: open `examples/09_iterating_with_a_test_set.py`, predict the output, change one line, predict again.

## 10. Versioning prompts like code

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

Practice: open `examples/10_versioning_prompts_like_code.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 146

- Explain **A prompt is a specification** to someone else without notes.
- Explain **Role, task, constraints, format** to someone else without notes.
- Explain **Zero-shot vs few-shot** to someone else without notes.
- Explain **Example selection matters** to someone else without notes.
- Explain **Delimiters and structure** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
