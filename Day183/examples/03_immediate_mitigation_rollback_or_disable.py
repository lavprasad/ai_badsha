"""Day 183 — Incident response for AI systems
Concept 3: Immediate mitigation: rollback or disable

Run:  python 03_immediate_mitigation_rollback_or_disable.py
"""

import numpy as np

def preprocess(x):
    x = np.asarray(x, dtype=float)
    if np.isnan(x).any():
        raise ValueError('NaN in input')
    return (x - x.mean()) / (x.std() + 1e-8)

def test_preprocess():
    out = preprocess([1.0, 2.0, 3.0])
    assert abs(float(out.mean())) < 1e-6, 'should be zero-centred'
    assert abs(float(out.std()) - 1.0) < 1e-6, 'should be unit variance'
    try:
        preprocess([1.0, float('nan')])
    except ValueError:
        pass
    else:
        raise AssertionError('NaN should have raised')
    print('ok')

test_preprocess()

# ---------------------------------------------------------------------
# Remember: Test the data contract, not just the function — bad data breaks more models than bad code.
# Common mistake: Testing only the happy path, so an all-null column silently trains a constant model.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
