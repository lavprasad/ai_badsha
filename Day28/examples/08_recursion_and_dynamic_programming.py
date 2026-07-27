"""Day 28 — Discrete maths for AI
Concept 8: Recursion and dynamic programming

Run:  python 08_recursion_and_dynamic_programming.py
"""

import time

def membership_cost(n):
    data_list = list(range(n))
    data_set = set(data_list)
    target = n - 1

    t0 = time.perf_counter(); target in data_list; list_t = time.perf_counter() - t0
    t0 = time.perf_counter(); target in data_set;  set_t = time.perf_counter() - t0
    return list_t, set_t

for n in (10_000, 100_000, 1_000_000):
    l, s = membership_cost(n)
    print(f'n={n:>9,}  list O(n) {l * 1e6:8.1f} us   set O(1) {s * 1e6:6.1f} us')

# ---------------------------------------------------------------------
# Remember: Before optimising constants, check whether you picked an O(n^2) shape for an O(n log n) problem.
# Common mistake: A membership test against a list inside a loop, turning a linear job into a quadratic one.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
