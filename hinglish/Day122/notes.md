# Day 122 — Classical NLP baselines

Aaj ka goal: **Classical NLP baselines** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Bag of words revisited |
| 2 | TF-IDF for classification |
| 3 | N-gram language models |
| 4 | Naive Bayes for text |
| 5 | Linear SVM for text |
| 6 | Named entity recognition, classically |
| 7 | Rule-based systems that still work |
| 8 | Keyword search and BM25 |
| 9 | Measuring the baseline properly |
| 10 | Deciding whether you need an LLM at all |

---

## 1. Bag of words revisited

### Aasaan Bhasha

Embeddings se pehle text ginti se numbers banta tha. TF-IDF ek word ko is hisaab se weight deta hai ki wo yahan kitni baar aaya aur overall kitna rare hai, isliye 'the' ka score lagbhag zero ho jaata hai. Classification aur keyword search ke liye ye aaj bhi lagbhag muft ka behtareen baseline hai.

### Chhota code

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'the cat sat on the mat',
    'the dog sat on the log',
    'machine learning models learn patterns',
]
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
print(X.toarray().round(2))
```

**Yaad rakho:** TF-IDF + logistic regression wo baseline hai jise har LLM text classifier ko harana padega tabhi wo apni cost layak hai.

**Aam galti:** Support tickets classify karne ke liye 7B model uthana jab TF-IDF muft me 94% de deta hai.

Practice: `examples/01_bag_of_words_revisited.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. TF-IDF for classification

### Aasaan Bhasha

Embeddings se pehle text ginti se numbers banta tha. TF-IDF ek word ko is hisaab se weight deta hai ki wo yahan kitni baar aaya aur overall kitna rare hai, isliye 'the' ka score lagbhag zero ho jaata hai. Classification aur keyword search ke liye ye aaj bhi lagbhag muft ka behtareen baseline hai.

### Chhota code

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'the cat sat on the mat',
    'the dog sat on the log',
    'machine learning models learn patterns',
]
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
print(X.toarray().round(2))
```

**Yaad rakho:** TF-IDF + logistic regression wo baseline hai jise har LLM text classifier ko harana padega tabhi wo apni cost layak hai.

**Aam galti:** Support tickets classify karne ke liye 7B model uthana jab TF-IDF muft me 94% de deta hai.

Practice: `examples/02_tf_idf_for_classification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. N-gram language models

### Aasaan Bhasha

Embeddings se pehle text ginti se numbers banta tha. TF-IDF ek word ko is hisaab se weight deta hai ki wo yahan kitni baar aaya aur overall kitna rare hai, isliye 'the' ka score lagbhag zero ho jaata hai. Classification aur keyword search ke liye ye aaj bhi lagbhag muft ka behtareen baseline hai.

### Chhota code

```python
from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'the cat sat on the mat',
    'the dog sat on the log',
    'machine learning models learn patterns',
]
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
print(X.toarray().round(2))
```

**Yaad rakho:** TF-IDF + logistic regression wo baseline hai jise har LLM text classifier ko harana padega tabhi wo apni cost layak hai.

**Aam galti:** Support tickets classify karne ke liye 7B model uthana jab TF-IDF muft me 94% de deta hai.

Practice: `examples/03_n_gram_language_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Naive Bayes for text

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

Practice: `examples/04_naive_bayes_for_text.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Linear SVM for text

### Aasaan Bhasha

SVM classes ke beech sabse chaudi margin wali boundary dhoondta hai. Kernel trick use tedhi boundaries khinchne deta hai, higher-dimensional space me inner products nikaal kar, bina wo space kabhi banaye. Chhote, saaf, high-dimensional datasets (jaise text) par strong.

### Chhota code

```python
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons
from sklearn.model_selection import cross_val_score

X, y = make_moons(n_samples=500, noise=0.2, random_state=0)
linear = make_pipeline(StandardScaler(), SVC(kernel='linear'))
rbf = make_pipeline(StandardScaler(), SVC(kernel='rbf', C=1.0, gamma='scale'))
print('linear', cross_val_score(linear, X, y, cv=5).mean().round(3))
print('rbf   ', cross_val_score(rbf, X, y, cv=5).mean().round(3))
```

**Yaad rakho:** SVM rows ke saath lagbhag quadratically badhta hai — ~100k samples se upar boosting uthao.

**Aam galti:** Feature scaling chhod dena, jo chupke se RBF kernel barbaad kar deta hai.

Practice: `examples/05_linear_svm_for_text.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Named entity recognition, classically

### Aasaan Bhasha

Har cheez ko model nahi chahiye. Achhe format wale IDs, dates aur codes ke liye regex aur gazetteer aaj bhi fine-tuned model se behtar hain — zero latency aur poori explainability ke saath. BM25 keyword search abhi bhi strong retrieval baseline hai aur hybrid search isi ko embeddings ke saath jodta hai.

### Chhota code

```python
import re
from collections import Counter
import math

text = 'Invoice INV-2024-0031 dated 2024-03-02 for Rs 15,300 to Acme Ltd.'
print('ids  ', re.findall(r'\bINV-\d{4}-\d{4}\b', text))
print('dates', re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))

docs = ['refund policy takes five days', 'office hours in pune', 'refund of enterprise plans']
query = 'refund'
df = sum(query in d for d in docs)
idf = math.log((len(docs) - df + 0.5) / (df + 0.5) + 1)
for d in docs:
    tf = Counter(d.split())[query]
    print(round(idf * tf / (tf + 1.2), 3), '|', d)
```

**Yaad rakho:** Pehle regex try karo. Agar wo bina infrastructure ke 95% de deta hai, to model ko use replace karne ki wajah deni padegi.

**Aam galti:** Dates nikaalne ke liye transformer fine-tune karna jinhe `dateutil` pehle se sahi parse kar leta hai.

Practice: `examples/06_named_entity_recognition_classically.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Rule-based systems that still work

### Aasaan Bhasha

Har cheez ko model nahi chahiye. Achhe format wale IDs, dates aur codes ke liye regex aur gazetteer aaj bhi fine-tuned model se behtar hain — zero latency aur poori explainability ke saath. BM25 keyword search abhi bhi strong retrieval baseline hai aur hybrid search isi ko embeddings ke saath jodta hai.

### Chhota code

```python
import re
from collections import Counter
import math

text = 'Invoice INV-2024-0031 dated 2024-03-02 for Rs 15,300 to Acme Ltd.'
print('ids  ', re.findall(r'\bINV-\d{4}-\d{4}\b', text))
print('dates', re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))

docs = ['refund policy takes five days', 'office hours in pune', 'refund of enterprise plans']
query = 'refund'
df = sum(query in d for d in docs)
idf = math.log((len(docs) - df + 0.5) / (df + 0.5) + 1)
for d in docs:
    tf = Counter(d.split())[query]
    print(round(idf * tf / (tf + 1.2), 3), '|', d)
```

**Yaad rakho:** Pehle regex try karo. Agar wo bina infrastructure ke 95% de deta hai, to model ko use replace karne ki wajah deni padegi.

**Aam galti:** Dates nikaalne ke liye transformer fine-tune karna jinhe `dateutil` pehle se sahi parse kar leta hai.

Practice: `examples/07_rule_based_systems_that_still_work.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Keyword search and BM25

### Aasaan Bhasha

Har cheez ko model nahi chahiye. Achhe format wale IDs, dates aur codes ke liye regex aur gazetteer aaj bhi fine-tuned model se behtar hain — zero latency aur poori explainability ke saath. BM25 keyword search abhi bhi strong retrieval baseline hai aur hybrid search isi ko embeddings ke saath jodta hai.

### Chhota code

```python
import re
from collections import Counter
import math

text = 'Invoice INV-2024-0031 dated 2024-03-02 for Rs 15,300 to Acme Ltd.'
print('ids  ', re.findall(r'\bINV-\d{4}-\d{4}\b', text))
print('dates', re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))

docs = ['refund policy takes five days', 'office hours in pune', 'refund of enterprise plans']
query = 'refund'
df = sum(query in d for d in docs)
idf = math.log((len(docs) - df + 0.5) / (df + 0.5) + 1)
for d in docs:
    tf = Counter(d.split())[query]
    print(round(idf * tf / (tf + 1.2), 3), '|', d)
```

**Yaad rakho:** Pehle regex try karo. Agar wo bina infrastructure ke 95% de deta hai, to model ko use replace karne ki wajah deni padegi.

**Aam galti:** Dates nikaalne ke liye transformer fine-tune karna jinhe `dateutil` pehle se sahi parse kar leta hai.

Practice: `examples/08_keyword_search_and_bm25.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Measuring the baseline properly

### Aasaan Bhasha

Har cheez ko model nahi chahiye. Achhe format wale IDs, dates aur codes ke liye regex aur gazetteer aaj bhi fine-tuned model se behtar hain — zero latency aur poori explainability ke saath. BM25 keyword search abhi bhi strong retrieval baseline hai aur hybrid search isi ko embeddings ke saath jodta hai.

### Chhota code

```python
import re
from collections import Counter
import math

text = 'Invoice INV-2024-0031 dated 2024-03-02 for Rs 15,300 to Acme Ltd.'
print('ids  ', re.findall(r'\bINV-\d{4}-\d{4}\b', text))
print('dates', re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text))

docs = ['refund policy takes five days', 'office hours in pune', 'refund of enterprise plans']
query = 'refund'
df = sum(query in d for d in docs)
idf = math.log((len(docs) - df + 0.5) / (df + 0.5) + 1)
for d in docs:
    tf = Counter(d.split())[query]
    print(round(idf * tf / (tf + 1.2), 3), '|', d)
```

**Yaad rakho:** Pehle regex try karo. Agar wo bina infrastructure ke 95% de deta hai, to model ko use replace karne ki wajah deni padegi.

**Aam galti:** Dates nikaalne ke liye transformer fine-tune karna jinhe `dateutil` pehle se sahi parse kar leta hai.

Practice: `examples/09_measuring_the_baseline_properly.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Deciding whether you need an LLM at all

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

Practice: `examples/10_deciding_whether_you_need_an_llm_at_all.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 122 ke baad aapko ye aana chahiye

- **Bag of words revisited** ko bina notes dekhe kisi dost ko samjha sakna.
- **TF-IDF for classification** ko bina notes dekhe kisi dost ko samjha sakna.
- **N-gram language models** ko bina notes dekhe kisi dost ko samjha sakna.
- **Naive Bayes for text** ko bina notes dekhe kisi dost ko samjha sakna.
- **Linear SVM for text** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
