"""Day 199 — Continuous learning system
Concept 9: Depth-first on one area per quarter

Run:  python 09_depth_first_on_one_area_per_quarter.py
"""

WEEK = {
    'Mon-Tue': 'Read/learn one concept — 45 min each',
    'Wed-Thu': 'Build something small that uses it and can fail',
    'Fri':     'Write 200 words on what surprised you',
    'Sat':     'Review notes from 1, 2 and 4 weeks ago (spaced repetition)',
    'Sun':     'Rest — consolidation is not optional',
}
for day, task in WEEK.items():
    print(f'{day:<9} {task}')

# ---------------------------------------------------------------------
# Remember: If you cannot explain it without notes, you have not learned it — you have watched it.
# Common mistake: Finishing a tenth course while having shipped nothing anyone else can run.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
