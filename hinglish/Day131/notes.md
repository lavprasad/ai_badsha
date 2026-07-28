# Day 131 — Post-training: SFT and alignment

Aaj ka goal: **Post-training: SFT and alignment** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Base models do not follow instructions |
| 2 | Supervised fine-tuning data format |
| 3 | Masking the loss to the response only |
| 4 | Data quality over quantity |
| 5 | Reward models |
| 6 | RLHF with PPO |
| 7 | Direct preference optimisation |
| 8 | Constitutional and rule-based methods |
| 9 | Sycophancy and reward hacking |
| 10 | Evaluating alignment |

---

## 1. Base models do not follow instructions

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/01_base_models_do_not_follow_instructions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Supervised fine-tuning data format

### Aasaan Bhasha

Hyperparameters wo settings hain jo aap chunte ho, seekhi nahi jaatin. Grid search poora chhaanta hai aur barbaad karta hai; random search high dimensions me acche ilaake jaldi dhoondta hai; Bayesian search pichhle trials se seekhta hai. Search hamesha cross-validation ke andar karo.

### Chhota code

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Yaad rakho:** Random seed fix karo aur har trial log karo, warna aap apna hi best model dobara nahi bana paoge.

**Aam galti:** 400 rows par 40 hyperparameters tune karna — ab aap validation set hi fit kar rahe ho.

Practice: `examples/02_supervised_fine_tuning_data_format.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Masking the loss to the response only

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/03_masking_the_loss_to_the_response_only.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Data quality over quantity

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/04_data_quality_over_quantity.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Reward models

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/05_reward_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. RLHF with PPO

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/06_rlhf_with_ppo.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Direct preference optimisation

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/07_direct_preference_optimisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Constitutional and rule-based methods

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/08_constitutional_and_rule_based_methods.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Sycophancy and reward hacking

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/09_sycophancy_and_reward_hacking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Evaluating alignment

### Aasaan Bhasha

Fine-tuning pretrained model ko aapke examples par aur train karta hai. Ye format, tone aur task ki shape naye facts se kahin behtar sikhata hai — facts ke liye retrieval use karo. Kuch sau behtareen examples aksar das hazaar aam examples se behtar hote hain.

### Chhota code

```python
# Typical SFT record: the model learns the assistant turn only.
example = {
    'messages': [
        {'role': 'system', 'content': 'You extract invoice fields as JSON.'},
        {'role': 'user', 'content': 'Invoice 4471, dated 2024-03-02, total Rs 15,300.'},
        {'role': 'assistant', 'content': '{"id": "4471", "date": "2024-03-02", "total": 15300}'},
    ]
}
import json
print(json.dumps(example, indent=2))
print('\\nRule: mask the loss on system+user tokens; train only on the assistant response.')
```

**Yaad rakho:** Behaviour aur format ke liye fine-tune karo. Jo knowledge badalti rehti hai uske liye RAG.

**Aam galti:** Company facts daalne ke liye fine-tune karna, phir har policy document badalne par dobara train karna.

Practice: `examples/10_evaluating_alignment.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 131 ke baad aapko ye aana chahiye

- **Base models do not follow instructions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Supervised fine-tuning data format** ko bina notes dekhe kisi dost ko samjha sakna.
- **Masking the loss to the response only** ko bina notes dekhe kisi dost ko samjha sakna.
- **Data quality over quantity** ko bina notes dekhe kisi dost ko samjha sakna.
- **Reward models** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
