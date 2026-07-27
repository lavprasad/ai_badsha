"""Day 04 — Files, JSON and the filesystem
Concept 1: Reading and writing text files

Run:  python 01_reading_and_writing_text_files.py
"""

from pathlib import Path

p = Path('demo.txt')
with p.open('w', encoding='utf-8') as fh:
    for i in range(5):
        fh.write(f'row {i}\n')

total = 0
with p.open(encoding='utf-8') as fh:
    for line in fh:              # streams; never holds the whole file
        total += 1
print('lines:', total)
p.unlink()

# ---------------------------------------------------------------------
# Remember: Always pass `encoding='utf-8'` explicitly — the platform default differs on Windows.
# Common mistake: `fh.read().split('\n')` on a huge file, which loads it all into RAM and then dies.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
