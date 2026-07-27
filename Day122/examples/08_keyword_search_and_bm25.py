"""Day 122 — Classical NLP baselines
Concept 8: Keyword search and BM25

Run:  python 08_keyword_search_and_bm25.py
"""

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

# ---------------------------------------------------------------------
# Remember: Try the regex first. If it hits 95% with no infrastructure, the model has to justify replacing it.
# Common mistake: Fine-tuning a transformer to extract dates that `dateutil` already parses correctly.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
