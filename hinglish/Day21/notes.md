# Day 21 — Probability foundations

Aaj ka goal: **Probability foundations** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Sample spaces and events |
| 2 | Axioms of probability |
| 3 | Independence and conditional probability |
| 4 | Bayes' rule |
| 5 | Prior, likelihood, posterior |
| 6 | The base rate fallacy |
| 7 | Random variables |
| 8 | Expectation and variance |
| 9 | Law of large numbers |
| 10 | Monte Carlo estimation |

---

## 1. Sample spaces and events

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/01_sample_spaces_and_events.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Axioms of probability

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/02_axioms_of_probability.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Independence and conditional probability

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/03_independence_and_conditional_probability.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Bayes' rule

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/04_bayes_rule.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Prior, likelihood, posterior

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/05_prior_likelihood_posterior.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. The base rate fallacy

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/06_the_base_rate_fallacy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Random variables

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/07_random_variables.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Expectation and variance

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/08_expectation_and_variance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Law of large numbers

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/09_law_of_large_numbers.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Monte Carlo estimation

### Aasaan Bhasha

Bayes rule evidence ke saath belief update karta hai: posterior = likelihood x prior / evidence. Applied ML ki sabse common galti prior ignore karna hai — 10000 me 1 wali bimari ke liye 99% accurate test bhi zyadatar false positives hi deta hai.

### Chhota code

```python
prior = 1 / 10_000          # base rate of the disease
sensitivity = 0.99          # P(positive | sick)
false_positive = 0.01       # P(positive | healthy)

evidence = sensitivity * prior + false_positive * (1 - prior)
posterior = sensitivity * prior / evidence
print(f'P(sick | positive) = {posterior:.4f}')   # ~0.0098
```

**Yaad rakho:** Rare events par precision gir hi jaati hai, chahe classifier accuracy par kitna bhi accha lage.

**Aam galti:** Imbalanced problem par accuracy report karna jahan hamesha 'no' bolne se 99% mil jaata hai.

Practice: `examples/10_monte_carlo_estimation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 21 ke baad aapko ye aana chahiye

- **Sample spaces and events** ko bina notes dekhe kisi dost ko samjha sakna.
- **Axioms of probability** ko bina notes dekhe kisi dost ko samjha sakna.
- **Independence and conditional probability** ko bina notes dekhe kisi dost ko samjha sakna.
- **Bayes' rule** ko bina notes dekhe kisi dost ko samjha sakna.
- **Prior, likelihood, posterior** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
