# Day 147 — Advanced prompting patterns

Aaj ka goal: **Advanced prompting patterns** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Decomposition into sub-prompts |
| 2 | Prompt chaining |
| 3 | Self-critique and revision loops |
| 4 | Rubric-based grading prompts |
| 5 | Persona and expertise framing |
| 6 | Handling ambiguity explicitly |
| 7 | Refusal and safe-completion design |
| 8 | Prompt caching for cost |
| 9 | Token budgeting |
| 10 | A prompt library with tests |

---

## 1. Decomposition into sub-prompts

### Aasaan Bhasha

Eigenvectors wo directions hain jinhe matrix sirf khinchta hai, ghumata nahi; eigenvalue khinchne ka factor hai. SVD isi ko har matrix ke liye general kar deta hai aur PCA, low-rank compression aur LoRA adapters ke peeche yahi engine hai.

### Chhota code

```python
import numpy as np

X = np.random.default_rng(0).normal(size=(100, 5))
U, S, Vt = np.linalg.svd(X, full_matrices=False)
print('singular values', np.round(S, 2))

energy = np.cumsum(S ** 2) / np.sum(S ** 2)
print('variance kept by first 2 dims:', round(float(energy[1]), 3))
```

**Yaad rakho:** Descending order me sorted singular values batate hain ki kitne dimensions me sach me information hai.

**Aam galti:** Bina scaling ke PCA/SVD chalana, jisse sabse badi unit wala column har component par chha jaata hai.

Practice: `examples/01_decomposition_into_sub_prompts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Prompt chaining

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

Practice: `examples/02_prompt_chaining.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Self-critique and revision loops

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

Practice: `examples/03_self_critique_and_revision_loops.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Rubric-based grading prompts

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

Practice: `examples/04_rubric_based_grading_prompts.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Persona and expertise framing

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

Practice: `examples/05_persona_and_expertise_framing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Handling ambiguity explicitly

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

Practice: `examples/06_handling_ambiguity_explicitly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Refusal and safe-completion design

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

Practice: `examples/07_refusal_and_safe_completion_design.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Prompt caching for cost

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

Practice: `examples/08_prompt_caching_for_cost.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Token budgeting

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

Practice: `examples/09_token_budgeting.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A prompt library with tests

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

Practice: `examples/10_a_prompt_library_with_tests.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 147 ke baad aapko ye aana chahiye

- **Decomposition into sub-prompts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Prompt chaining** ko bina notes dekhe kisi dost ko samjha sakna.
- **Self-critique and revision loops** ko bina notes dekhe kisi dost ko samjha sakna.
- **Rubric-based grading prompts** ko bina notes dekhe kisi dost ko samjha sakna.
- **Persona and expertise framing** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
