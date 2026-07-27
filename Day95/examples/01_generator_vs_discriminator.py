"""Day 95 — Generative adversarial networks
Concept 1: Generator vs discriminator

Run:  python 01_generator_vs_discriminator.py
"""

squares = [x * x for x in range(10)]          # list, all in memory
lazy = (x * x for x in range(10_000_000))    # generator, one at a time

def batches(seq, n):
    buf = []
    for item in seq:
        buf.append(item)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf

print(sum(lazy))
print(next(batches(range(10), 3)))

# ---------------------------------------------------------------------
# Remember: A generator can only be consumed once — re-create it if you need a second pass.
# Common mistake: Calling `len()` on a generator, or iterating it twice and getting nothing the second time.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
