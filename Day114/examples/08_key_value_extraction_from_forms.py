"""Day 114 — OCR and document AI
Concept 8: Key-value extraction from forms

Run:  python 08_key_value_extraction_from_forms.py
"""

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

# ---------------------------------------------------------------------
# Remember: Arithmetic and schema checks on extracted fields catch OCR errors that no confidence score flags.
# Common mistake: Running OCR on PDFs that already had a perfect text layer, adding cost and introducing errors.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
