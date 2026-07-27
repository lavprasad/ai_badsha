"""Day 175 — From notebook to software
Concept 2: Project structure for ML repos

Run:  python 02_project_structure_for_ml_repos.py
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
