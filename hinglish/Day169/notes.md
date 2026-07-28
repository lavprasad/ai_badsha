# Day 169 — Working with unstructured documents

Aaj ka goal: **Working with unstructured documents** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Document ingestion pipeline |
| 2 | Format detection and routing |
| 3 | PDF text vs scanned PDF |
| 4 | OCR fallback |
| 5 | Layout and reading order |
| 6 | Table extraction strategies |
| 7 | Metadata and provenance |
| 8 | Incremental processing |
| 9 | Quality checks on extraction |
| 10 | A document intelligence service |

---

## 1. Document ingestion pipeline

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

Practice: `examples/01_document_ingestion_pipeline.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Format detection and routing

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

Practice: `examples/02_format_detection_and_routing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. PDF text vs scanned PDF

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

Practice: `examples/03_pdf_text_vs_scanned_pdf.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. OCR fallback

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

Practice: `examples/04_ocr_fallback.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Layout and reading order

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

Practice: `examples/05_layout_and_reading_order.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Table extraction strategies

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

Practice: `examples/06_table_extraction_strategies.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Metadata and provenance

### Aasaan Bhasha

Missing data information hai, sirf noise nahi. Kuch bharne se pehle poochho ki **kyun** missing hai: jo sensor sirf load par fail hota hai wo randomly missing nahi hai. Phir chuno: rows drop, column drop, statistic se fill, ya ek explicit 'ye missing tha' indicator column.

### Chhota code

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Yaad rakho:** Fill karne wali statistic sirf TRAIN split par nikalo, phir test par lagao.

**Aam galti:** Poore dataset ke mean se fill karna — ye test ki information training me leak kar deta hai.

Practice: `examples/07_metadata_and_provenance.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Incremental processing

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

Practice: `examples/08_incremental_processing.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Quality checks on extraction

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

Practice: `examples/09_quality_checks_on_extraction.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A document intelligence service

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

Practice: `examples/10_a_document_intelligence_service.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 169 ke baad aapko ye aana chahiye

- **Document ingestion pipeline** ko bina notes dekhe kisi dost ko samjha sakna.
- **Format detection and routing** ko bina notes dekhe kisi dost ko samjha sakna.
- **PDF text vs scanned PDF** ko bina notes dekhe kisi dost ko samjha sakna.
- **OCR fallback** ko bina notes dekhe kisi dost ko samjha sakna.
- **Layout and reading order** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
