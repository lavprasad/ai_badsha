"""Day 01 — Setting up your AI workbench
Concept 4: pip install and requirements.txt

Run:  python 04_pip_install_and_requirements_txt.py
"""

import subprocess, sys

# What is actually installed, in requirements.txt format:
out = subprocess.run([sys.executable, '-m', 'pip', 'freeze'],
                     capture_output=True, text=True).stdout
lines = [l for l in out.splitlines() if l and not l.startswith('-e')]
print(f'{len(lines)} pinned packages, first 5:')
for l in lines[:5]:
    print(' ', l)
print('\nSave with:  pip freeze > requirements.txt')
print('Restore with: pip install -r requirements.txt')

# ---------------------------------------------------------------------
# Remember: `numpy>=1.26` is a wish; `numpy==1.26.4` is a promise. Pin exactly for anything you must reproduce.
# Common mistake: Committing code without the requirements file, so nobody can rebuild the environment that produced your numbers.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
