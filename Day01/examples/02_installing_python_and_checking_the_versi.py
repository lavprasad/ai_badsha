"""Day 01 — Setting up your AI workbench
Concept 2: Installing Python and checking the version

Run:  python 02_installing_python_and_checking_the_versi.py
"""

import sys, platform

print('python  ', sys.version.split()[0])
print('binary  ', sys.executable)      # WHICH python is this?
print('platform', platform.system(), platform.machine())

for mod in ('numpy', 'pandas', 'sklearn', 'torch'):
    try:
        m = __import__(mod)
        print(f'{mod:<8} {getattr(m, "__version__", "?")}')
    except ImportError:
        print(f'{mod:<8} not installed')

# ---------------------------------------------------------------------
# Remember: Run this file on day one and whenever anything mysterious breaks — it answers 'which Python?' instantly.
# Common mistake: Installing a package with one Python and importing it with another, then blaming the package.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
