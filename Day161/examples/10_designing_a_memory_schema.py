"""Day 161 — Memory for AI applications
Concept 10: Designing a memory schema

Run:  python 10_designing_a_memory_schema.py
"""

import time

class Memory:
    def __init__(self, ttl_days=90):
        self.items, self.ttl = [], ttl_days * 86400

    def add(self, key, value, ts):
        self.items = [i for i in self.items if i['key'] != key]   # newest wins
        self.items.append({'key': key, 'value': value, 'ts': ts})

    def recall(self, now):
        return [i for i in self.items if now - i['ts'] < self.ttl]

m = Memory(ttl_days=30)
m.add('preferred_name', 'Sam', ts=0)
m.add('preferred_name', 'Samir', ts=100)      # correction replaces, not appends
print(m.recall(now=200))
print(m.recall(now=30 * 86400 + 200))          # expired

# ---------------------------------------------------------------------
# Remember: A correction must overwrite, not coexist. Two contradictory memories will both get retrieved.
# Common mistake: Appending every stated fact to a vector store forever, so stale and corrected facts compete at retrieval.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
