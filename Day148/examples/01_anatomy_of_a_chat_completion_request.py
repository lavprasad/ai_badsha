"""Day 148 — LLM APIs in code
Concept 1: Anatomy of a chat completion request

Run:  python 01_anatomy_of_a_chat_completion_request.py
"""

import random, time

def with_retries(call, attempts=4, base=0.5, timeout_s=30):
    last = None
    for i in range(attempts):
        try:
            return call(timeout=timeout_s)
        except Exception as e:                     # narrow this to your client's errors
            last = e
            if i == attempts - 1:
                break
            sleep = base * (2 ** i) + random.random() * 0.1   # backoff + jitter
            print(f'attempt {i + 1} failed ({e}); retrying in {sleep:.2f}s')
            time.sleep(min(sleep, 0.01))          # shortened for the demo
    raise RuntimeError(f'all {attempts} attempts failed') from last

calls = {'n': 0}
def flaky(timeout):
    calls['n'] += 1
    if calls['n'] < 3:
        raise TimeoutError('upstream slow')
    return 'ok'

print(with_retries(flaky))

# ---------------------------------------------------------------------
# Remember: Jitter matters: without it, every client retries at the same instant and re-creates the outage.
# Common mistake: Infinite retries on a 400-class error that will never succeed, hammering the API and your budget.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
