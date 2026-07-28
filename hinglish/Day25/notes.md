# Day 25 — A/B testing and experiment design

Aaj ka goal: **A/B testing and experiment design** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Framing a decision as an experiment |
| 2 | Randomisation and control groups |
| 3 | Choosing a primary metric |
| 4 | Minimum detectable effect |
| 5 | Deciding sample size up front |
| 6 | Peeking and why it inflates false positives |
| 7 | Guardrail metrics |
| 8 | Novelty and seasonality effects |
| 9 | Analysing an A/B result |
| 10 | When an A/B test is the wrong tool |

---

## 1. Framing a decision as an experiment

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/01_framing_a_decision_as_an_experiment.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Randomisation and control groups

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/02_randomisation_and_control_groups.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Choosing a primary metric

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/03_choosing_a_primary_metric.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Minimum detectable effect

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/04_minimum_detectable_effect.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Deciding sample size up front

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/05_deciding_sample_size_up_front.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Peeking and why it inflates false positives

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/06_peeking_and_why_it_inflates_false_positi.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Guardrail metrics

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/07_guardrail_metrics.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Novelty and seasonality effects

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/08_novelty_and_seasonality_effects.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Analysing an A/B result

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/09_analysing_an_a_b_result.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. When an A/B test is the wrong tool

### Aasaan Bhasha

p-value matlab P(itna extreme data | kuch ho hi nahi raha). Ye ye nahi batata ki aapka idea sahi hai. Confidence interval zyada kaam ka hai kyunki wo effect size aur uncertainty saath dikhata hai — 'significant' 0.1% lift shayad ship karne layak hi na ho.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
control = rng.normal(10.0, 2.0, 500)
variant = rng.normal(10.3, 2.0, 500)

diff = variant.mean() - control.mean()
se = np.sqrt(control.var(ddof=1) / 500 + variant.var(ddof=1) / 500)
print(f'lift {diff:.3f}  95% CI [{diff - 1.96 * se:.3f}, {diff + 1.96 * se:.3f}]')
```

**Yaad rakho:** Sample size aur metric data dekhne se PEHLE decide karo.

**Aam galti:** Roz jhaank kar p < 0.05 hote hi test rok dena — isse false positives bahut badh jaate hain.

Practice: `examples/10_when_an_a_b_test_is_the_wrong_tool.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 25 ke baad aapko ye aana chahiye

- **Framing a decision as an experiment** ko bina notes dekhe kisi dost ko samjha sakna.
- **Randomisation and control groups** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing a primary metric** ko bina notes dekhe kisi dost ko samjha sakna.
- **Minimum detectable effect** ko bina notes dekhe kisi dost ko samjha sakna.
- **Deciding sample size up front** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
