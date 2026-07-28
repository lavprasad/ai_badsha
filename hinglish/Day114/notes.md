# Day 114 — OCR and document AI

Aaj ka goal: **OCR and document AI** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Text detection vs text recognition |
| 2 | Tesseract and classical OCR |
| 3 | Deep OCR models |
| 4 | Layout analysis |
| 5 | Table extraction |
| 6 | Handwriting recognition |
| 7 | Document classification |
| 8 | Key-value extraction from forms |
| 9 | Post-processing and validation rules |
| 10 | An invoice extraction pipeline |

---

## 1. Text detection vs text recognition

### Aasaan Bhasha

Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.

### Chhota code

```python
def route_document(has_text_layer, is_scanned, page_count):
    if has_text_layer and not is_scanned:
        return 'direct text extraction (fast, accurate, free)'
    if page_count > 50:
        return 'OCR with a queue — too slow for a request/response path'
    return 'OCR then layout analysis'

for case in [(True, False, 3), (False, True, 3), (False, True, 120)]:
    print(case, '->', route_document(*case))

def validate_invoice(fields):
    checks = {
        'total matches lines': abs(sum(fields['lines']) - fields['total']) < 0.01,
        'date present': bool(fields.get('date')),
    }
    return checks
print(validate_invoice({'lines': [100.0, 50.0], 'total': 150.0, 'date': '2024-03-02'}))
```

**Yaad rakho:** Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.

**Aam galti:** Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.

Practice: `examples/01_text_detection_vs_text_recognition.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Tesseract and classical OCR

### Aasaan Bhasha

Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.

### Chhota code

```python
def route_document(has_text_layer, is_scanned, page_count):
    if has_text_layer and not is_scanned:
        return 'direct text extraction (fast, accurate, free)'
    if page_count > 50:
        return 'OCR with a queue — too slow for a request/response path'
    return 'OCR then layout analysis'

for case in [(True, False, 3), (False, True, 3), (False, True, 120)]:
    print(case, '->', route_document(*case))

def validate_invoice(fields):
    checks = {
        'total matches lines': abs(sum(fields['lines']) - fields['total']) < 0.01,
        'date present': bool(fields.get('date')),
    }
    return checks
print(validate_invoice({'lines': [100.0, 50.0], 'total': 150.0, 'date': '2024-03-02'}))
```

**Yaad rakho:** Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.

**Aam galti:** Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.

Practice: `examples/02_tesseract_and_classical_ocr.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Deep OCR models

### Aasaan Bhasha

Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.

### Chhota code

```python
def route_document(has_text_layer, is_scanned, page_count):
    if has_text_layer and not is_scanned:
        return 'direct text extraction (fast, accurate, free)'
    if page_count > 50:
        return 'OCR with a queue — too slow for a request/response path'
    return 'OCR then layout analysis'

for case in [(True, False, 3), (False, True, 3), (False, True, 120)]:
    print(case, '->', route_document(*case))

def validate_invoice(fields):
    checks = {
        'total matches lines': abs(sum(fields['lines']) - fields['total']) < 0.01,
        'date present': bool(fields.get('date')),
    }
    return checks
print(validate_invoice({'lines': [100.0, 50.0], 'total': 150.0, 'date': '2024-03-02'}))
```

**Yaad rakho:** Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.

**Aam galti:** Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.

Practice: `examples/03_deep_ocr_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Layout analysis

### Aasaan Bhasha

Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.

### Chhota code

```python
def route_document(has_text_layer, is_scanned, page_count):
    if has_text_layer and not is_scanned:
        return 'direct text extraction (fast, accurate, free)'
    if page_count > 50:
        return 'OCR with a queue — too slow for a request/response path'
    return 'OCR then layout analysis'

for case in [(True, False, 3), (False, True, 3), (False, True, 120)]:
    print(case, '->', route_document(*case))

def validate_invoice(fields):
    checks = {
        'total matches lines': abs(sum(fields['lines']) - fields['total']) < 0.01,
        'date present': bool(fields.get('date')),
    }
    return checks
print(validate_invoice({'lines': [100.0, 50.0], 'total': 150.0, 'date': '2024-03-02'}))
```

**Yaad rakho:** Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.

**Aam galti:** Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.

Practice: `examples/04_layout_analysis.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Table extraction

### Aasaan Bhasha

Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.

### Chhota code

```python
def route_document(has_text_layer, is_scanned, page_count):
    if has_text_layer and not is_scanned:
        return 'direct text extraction (fast, accurate, free)'
    if page_count > 50:
        return 'OCR with a queue — too slow for a request/response path'
    return 'OCR then layout analysis'

for case in [(True, False, 3), (False, True, 3), (False, True, 120)]:
    print(case, '->', route_document(*case))

def validate_invoice(fields):
    checks = {
        'total matches lines': abs(sum(fields['lines']) - fields['total']) < 0.01,
        'date present': bool(fields.get('date')),
    }
    return checks
print(validate_invoice({'lines': [100.0, 50.0], 'total': 150.0, 'date': '2024-03-02'}))
```

**Yaad rakho:** Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.

**Aam galti:** Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.

Practice: `examples/05_table_extraction.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Handwriting recognition

### Aasaan Bhasha

Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.

### Chhota code

```python
def route_document(has_text_layer, is_scanned, page_count):
    if has_text_layer and not is_scanned:
        return 'direct text extraction (fast, accurate, free)'
    if page_count > 50:
        return 'OCR with a queue — too slow for a request/response path'
    return 'OCR then layout analysis'

for case in [(True, False, 3), (False, True, 3), (False, True, 120)]:
    print(case, '->', route_document(*case))

def validate_invoice(fields):
    checks = {
        'total matches lines': abs(sum(fields['lines']) - fields['total']) < 0.01,
        'date present': bool(fields.get('date')),
    }
    return checks
print(validate_invoice({'lines': [100.0, 50.0], 'total': 150.0, 'date': '2024-03-02'}))
```

**Yaad rakho:** Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.

**Aam galti:** Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.

Practice: `examples/06_handwriting_recognition.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Document classification

### Aasaan Bhasha

Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.

### Chhota code

```python
def route_document(has_text_layer, is_scanned, page_count):
    if has_text_layer and not is_scanned:
        return 'direct text extraction (fast, accurate, free)'
    if page_count > 50:
        return 'OCR with a queue — too slow for a request/response path'
    return 'OCR then layout analysis'

for case in [(True, False, 3), (False, True, 3), (False, True, 120)]:
    print(case, '->', route_document(*case))

def validate_invoice(fields):
    checks = {
        'total matches lines': abs(sum(fields['lines']) - fields['total']) < 0.01,
        'date present': bool(fields.get('date')),
    }
    return checks
print(validate_invoice({'lines': [100.0, 50.0], 'total': 150.0, 'date': '2024-03-02'}))
```

**Yaad rakho:** Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.

**Aam galti:** Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.

Practice: `examples/07_document_classification.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Key-value extraction from forms

### Aasaan Bhasha

Document AI ek pipeline hai, model nahi: pehle dekho ki PDF me text layer hai ya nahi, na ho tabhi OCR karo, reading order aur layout wapas nikaalo, phir schema ke against fields extract karo. Aakhir me validation rules (kya total lines ke sum ke barabar hai?) behtar OCR model se zyada errors pakadte hain.

### Chhota code

```python
def route_document(has_text_layer, is_scanned, page_count):
    if has_text_layer and not is_scanned:
        return 'direct text extraction (fast, accurate, free)'
    if page_count > 50:
        return 'OCR with a queue — too slow for a request/response path'
    return 'OCR then layout analysis'

for case in [(True, False, 3), (False, True, 3), (False, True, 120)]:
    print(case, '->', route_document(*case))

def validate_invoice(fields):
    checks = {
        'total matches lines': abs(sum(fields['lines']) - fields['total']) < 0.01,
        'date present': bool(fields.get('date')),
    }
    return checks
print(validate_invoice({'lines': [100.0, 50.0], 'total': 150.0, 'date': '2024-03-02'}))
```

**Yaad rakho:** Extracted fields par arithmetic aur schema checks wo OCR errors pakadte hain jinhe koi confidence score flag nahi karta.

**Aam galti:** Un PDFs par OCR chalana jinme pehle se perfect text layer tha, jisse cost badhi aur errors aaye.

Practice: `examples/08_key_value_extraction_from_forms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Post-processing and validation rules

### Aasaan Bhasha

Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.

### Chhota code

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Yaad rakho:** Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.

**Aam galti:** Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.

Practice: `examples/09_post_processing_and_validation_rules.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. An invoice extraction pipeline

### Aasaan Bhasha

Pipeline preprocessing aur model ko ek hi object me jod deta hai jo ek unit ki tarah fit aur predict karta hai. Leakage ke khilaaf yahi sabse achhi dhaal hai, aur deployment ko chhe alag steps ke bajaye ek artefact milta hai jise yaad rakhne ki zaroorat nahi.

### Chhota code

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Yaad rakho:** `handle_unknown='ignore'` production ko us category par crash hone se bachata hai jo training me kabhi nahi dikhi.

**Aam galti:** Notebook me preprocess karna aur serving code likhte waqt ek step bhool jaana.

Practice: `examples/10_an_invoice_extraction_pipeline.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 114 ke baad aapko ye aana chahiye

- **Text detection vs text recognition** ko bina notes dekhe kisi dost ko samjha sakna.
- **Tesseract and classical OCR** ko bina notes dekhe kisi dost ko samjha sakna.
- **Deep OCR models** ko bina notes dekhe kisi dost ko samjha sakna.
- **Layout analysis** ko bina notes dekhe kisi dost ko samjha sakna.
- **Table extraction** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
