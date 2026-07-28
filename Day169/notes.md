# Day 169 — Working with unstructured documents

Today's goal: work through **Working with unstructured documents** — ten concepts, ten runnable examples, five questions.

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

Practice: open `examples/01_document_ingestion_pipeline.py`, predict the output, change one line, predict again.

## 2. Format detection and routing

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

Practice: open `examples/02_format_detection_and_routing.py`, predict the output, change one line, predict again.

## 3. PDF text vs scanned PDF

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

Practice: open `examples/03_pdf_text_vs_scanned_pdf.py`, predict the output, change one line, predict again.

## 4. OCR fallback

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

Practice: open `examples/04_ocr_fallback.py`, predict the output, change one line, predict again.

## 5. Layout and reading order

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

Practice: open `examples/05_layout_and_reading_order.py`, predict the output, change one line, predict again.

## 6. Table extraction strategies

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

Practice: open `examples/06_table_extraction_strategies.py`, predict the output, change one line, predict again.

## 7. Metadata and provenance

Missing data is information, not just noise. Before filling anything, ask *why* it is missing: a sensor that fails only under load is not missing at random. Then choose: drop rows, drop the column, fill with a statistic, or add an explicit 'was missing' indicator column.

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Remember:** Compute the fill statistic on the TRAIN split only, then apply it to test.

**Common mistake:** Filling with the mean computed over the full dataset — that leaks test information into training.

Practice: open `examples/07_metadata_and_provenance.py`, predict the output, change one line, predict again.

## 8. Incremental processing

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

Practice: open `examples/08_incremental_processing.py`, predict the output, change one line, predict again.

## 9. Quality checks on extraction

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

Practice: open `examples/09_quality_checks_on_extraction.py`, predict the output, change one line, predict again.

## 10. A document intelligence service

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

Practice: open `examples/10_a_document_intelligence_service.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 169

- Explain **Document ingestion pipeline** to someone else without notes.
- Explain **Format detection and routing** to someone else without notes.
- Explain **PDF text vs scanned PDF** to someone else without notes.
- Explain **OCR fallback** to someone else without notes.
- Explain **Layout and reading order** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
