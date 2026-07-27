"""Day 73 — Error analysis
Concept 8: Finding annotation errors in the labels

Run:  python 08_finding_annotation_errors_in_the_labels.py
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(0)
df = pd.DataFrame({
    'segment': rng.choice(['new', 'returning', 'enterprise'], 600, p=[.5, .3, .2]),
    'y': rng.integers(0, 2, 600),
})
df['pred'] = np.where(df.segment == 'enterprise', 1 - df.y, df.y)   # broken on one segment

report = (df.assign(wrong=df.pred != df.y)
            .groupby('segment')
            .agg(n=('wrong', 'size'), errors=('wrong', 'sum')))
report['error_rate'] = (report.errors / report.n).round(3)
report['share_of_all_errors'] = (report.errors / report.errors.sum()).round(3)
print(report.sort_values('share_of_all_errors', ascending=False))

# ---------------------------------------------------------------------
# Remember: Rank error buckets by share of total errors, not by error rate — fix what is actually costing you.
# Common mistake: Optimising overall accuracy while one segment quietly gets 0% and generates every complaint.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
