"""Day 02 — Python essentials refresher
Concept 6: for and while loops

Run:  python 06_for_and_while_loops.py
"""

counts = {'a': 3, 'b': 0}

for key, value in counts.items():
    print(f'{key}: {value:>3d}')      # f-string with alignment

x = 0
print(bool(x), x is not None)          # False True  <- not the same question

print('b' in counts)                   # dict membership: O(1)
print(0 in list(counts.values()))      # list membership: O(n)

# ---------------------------------------------------------------------
# Remember: `if x:` and `if x is not None:` differ for 0, '' and empty containers. Pick deliberately.
# Common mistake: Using `if not value:` to check for a missing field and rejecting a legitimate zero.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
