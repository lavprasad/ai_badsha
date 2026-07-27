"""Day 36 — Getting data
Concept 8: Personally identifiable information

Run:  python 08_personally_identifiable_information.py
"""

import hashlib, time

def pseudonymise(email, salt='project-salt'):
    return hashlib.sha256((salt + email.lower()).encode()).hexdigest()[:16]

print(pseudonymise('User@Example.com'))

def fetch_pages(fetch, max_pages=5):
    """fetch(page) -> (rows, has_more). Backs off on failure."""
    out, page, delay = [], 1, 1.0
    while page <= max_pages:
        rows, has_more = fetch(page)
        out.extend(rows)
        if not has_more:
            break
        page += 1
    return out

print(fetch_pages(lambda p: ([f'row{p}'], p < 3)))

# ---------------------------------------------------------------------
# Remember: Hash or drop identifiers at ingestion, not at report time — by then copies already exist.
# Common mistake: Scraping a source whose terms forbid it and discovering the problem after the model is in production.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
