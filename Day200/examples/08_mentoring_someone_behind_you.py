"""Day 200 — Day 200: the road ahead
Concept 8: Mentoring someone behind you

Run:  python 08_mentoring_someone_behind_you.py
"""

DURABLE = ['linear algebra', 'probability and statistics', 'optimisation',
           'honest evaluation and splits', 'leakage detection', 'error analysis',
           'problem framing', 'writing clearly']
EXPIRING = ['this version of the framework API', 'today\'s best model name',
            'current pricing', 'the fashionable agent library']

print('Invest here (10-year shelf life):')
for d in DURABLE:
    print('  +', d)
print('\nLearn just-in-time (18-month shelf life):')
for e in EXPIRING:
    print('  -', e)

# ---------------------------------------------------------------------
# Remember: Rebuild one project from Day 1 knowledge at the end. The gap between the two versions is your progress.
# Common mistake: Measuring your skill by the number of tools you have touched rather than problems you have solved.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
