# Day 82 — Initialisation and normalisation

Aaj ka goal: **Initialisation and normalisation** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why zero initialisation fails |
| 2 | Random initialisation scale |
| 3 | Xavier/Glorot initialisation |
| 4 | He initialisation for ReLU |
| 5 | Batch normalisation |
| 6 | Train vs eval mode |
| 7 | Layer normalisation |
| 8 | Group and RMS normalisation |
| 9 | Where to place normalisation layers |
| 10 | Diagnosing activation blow-up |

---

## 1. Why zero initialisation fails

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/01_why_zero_initialisation_fails.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Random initialisation scale

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/02_random_initialisation_scale.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Xavier/Glorot initialisation

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/03_xavier_glorot_initialisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. He initialisation for ReLU

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/04_he_initialisation_for_relu.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Batch normalisation

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/05_batch_normalisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Train vs eval mode

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/06_train_vs_eval_mode.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Layer normalisation

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/07_layer_normalisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Group and RMS normalisation

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/08_group_and_rms_normalisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Where to place normalisation layers

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/09_where_to_place_normalisation_layers.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Diagnosing activation blow-up

### Aasaan Bhasha

Vector numbers ki list hai jiski ek direction aur lambai hoti hai. Dot product alignment naapta hai: same direction par bada positive, perpendicular par zero. Cosine similarity wahi dot product hai lambai hata kar — isliye wo alag-alag magnitude ke embeddings ko theek se compare karta hai.

### Chhota code

```python
import numpy as np

a = np.array([1.0, 2.0, 3.0])
b = np.array([2.0, 4.0, 6.0])

print('dot   ', a @ b)
print('norm  ', np.linalg.norm(a))
cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print('cosine', cos)   # 1.0 -> same direction
```

**Yaad rakho:** Cosine similarity magnitude ignore karti hai; Euclidean distance nahi. Apne sawaal ke hisaab se chuno.

**Aam galti:** Raw embeddings ko Euclidean distance se compare karna jab sirf direction ka matlab hai.

Practice: `examples/10_diagnosing_activation_blow_up.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 82 ke baad aapko ye aana chahiye

- **Why zero initialisation fails** ko bina notes dekhe kisi dost ko samjha sakna.
- **Random initialisation scale** ko bina notes dekhe kisi dost ko samjha sakna.
- **Xavier/Glorot initialisation** ko bina notes dekhe kisi dost ko samjha sakna.
- **He initialisation for ReLU** ko bina notes dekhe kisi dost ko samjha sakna.
- **Batch normalisation** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
