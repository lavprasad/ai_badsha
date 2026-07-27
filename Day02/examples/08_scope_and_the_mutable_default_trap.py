"""Day 02 — Python essentials refresher
Concept 8: Scope and the mutable default trap

Run:  python 08_scope_and_the_mutable_default_trap.py
"""

def bad(item, bucket=[]):        # created ONCE
    bucket.append(item)
    return bucket

def good(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(bad(1), bad(2))     # [1] [1, 2]  <- leaked
print(good(1), good(2))   # [1] [2]     <- correct

# ---------------------------------------------------------------------
# Remember: Default arguments must be immutable. `None` plus a check is the standard fix.
# Common mistake: A `def f(x, cache={})` that silently accumulates state across every call in the process.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
