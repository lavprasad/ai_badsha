"""Day 175 — From notebook to software
Concept 3: Configuration files over hard-coded values

Run:  python 03_configuration_files_over_hard_coded_valu.py
"""

# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()

# ---------------------------------------------------------------------
# Remember: 'Restart kernel and run all' is the only honest test that a notebook works.
# Common mistake: Shipping a notebook whose results depend on a deleted cell you ran ten minutes ago.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
