"""Day 01 — Setting up your AI workbench
Concept 8: Reading a traceback without panic

Run:  python 08_reading_a_traceback_without_panic.py
"""

class DataContractError(ValueError):
    """Raised when input data violates the agreed schema."""

def load_age(raw):
    try:
        age = int(raw)
    except (TypeError, ValueError) as e:
        raise DataContractError(f'age must be an integer, got {raw!r}') from e
    if not 0 <= age <= 130:
        raise DataContractError(f'age out of range: {age}')
    return age

for value in ('42', 'abc', '999'):
    try:
        print(load_age(value))
    except DataContractError as e:
        print('rejected:', e)

# ---------------------------------------------------------------------
# Remember: `raise ... from e` keeps the original cause in the traceback. Never swallow it.
# Common mistake: `except: pass` around a whole pipeline, turning a crash into silently wrong output.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
