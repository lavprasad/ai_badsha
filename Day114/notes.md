# Day 114 — OCR and document AI

Today's goal: work through **OCR and document AI** — ten concepts, ten runnable examples, five questions.

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

Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema. Validation rules at the end (does the total equal the sum of lines?) catch more errors than a better OCR model.

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

**Remember:** Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

**Common mistake:** Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Practice: open `examples/01_text_detection_vs_text_recognition.py`, predict the output, change one line, predict again.

## 2. Tesseract and classical OCR

Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema. Validation rules at the end (does the total equal the sum of lines?) catch more errors than a better OCR model.

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

**Remember:** Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

**Common mistake:** Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Practice: open `examples/02_tesseract_and_classical_ocr.py`, predict the output, change one line, predict again.

## 3. Deep OCR models

Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema. Validation rules at the end (does the total equal the sum of lines?) catch more errors than a better OCR model.

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

**Remember:** Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

**Common mistake:** Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Practice: open `examples/03_deep_ocr_models.py`, predict the output, change one line, predict again.

## 4. Layout analysis

Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema. Validation rules at the end (does the total equal the sum of lines?) catch more errors than a better OCR model.

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

**Remember:** Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

**Common mistake:** Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Practice: open `examples/04_layout_analysis.py`, predict the output, change one line, predict again.

## 5. Table extraction

Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema. Validation rules at the end (does the total equal the sum of lines?) catch more errors than a better OCR model.

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

**Remember:** Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

**Common mistake:** Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Practice: open `examples/05_table_extraction.py`, predict the output, change one line, predict again.

## 6. Handwriting recognition

Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema. Validation rules at the end (does the total equal the sum of lines?) catch more errors than a better OCR model.

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

**Remember:** Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

**Common mistake:** Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Practice: open `examples/06_handwriting_recognition.py`, predict the output, change one line, predict again.

## 7. Document classification

Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema. Validation rules at the end (does the total equal the sum of lines?) catch more errors than a better OCR model.

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

**Remember:** Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

**Common mistake:** Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Practice: open `examples/07_document_classification.py`, predict the output, change one line, predict again.

## 8. Key-value extraction from forms

Document AI is a pipeline, not a model: detect whether the PDF has a text layer, OCR only if it does not, recover reading order and layout, then extract fields against a schema. Validation rules at the end (does the total equal the sum of lines?) catch more errors than a better OCR model.

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

**Remember:** Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.

**Common mistake:** Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.

Practice: open `examples/08_key_value_extraction_from_forms.py`, predict the output, change one line, predict again.

## 9. Post-processing and validation rules

Accuracy hides everything on imbalanced data. Precision asks 'of the ones I flagged, how many were real'; recall asks 'of the real ones, how many did I catch'. You trade one for the other with the threshold, and the business decides which error hurts more.

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

**Remember:** Tune the decision threshold on validation data; 0.5 is a default, not a decision.

**Common mistake:** Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

Practice: open `examples/09_post_processing_and_validation_rules.py`, predict the output, change one line, predict again.

## 10. An invoice extraction pipeline

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

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

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

Practice: open `examples/10_an_invoice_extraction_pipeline.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 114

- Explain **Text detection vs text recognition** to someone else without notes.
- Explain **Tesseract and classical OCR** to someone else without notes.
- Explain **Deep OCR models** to someone else without notes.
- Explain **Layout analysis** to someone else without notes.
- Explain **Table extraction** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
