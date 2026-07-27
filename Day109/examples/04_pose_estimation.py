"""Day 109 — Face and person understanding
Concept 4: Pose estimation

Run:  python 04_pose_estimation.py
"""

DECISION = [
    ('Do you need identity, or just presence?', 'presence -> use detection only, never enrol identities'),
    ('Is there a lawful basis and explicit consent?', 'no -> stop'),
    ('Can a badge/QR/login answer this?', 'yes -> use that instead'),
    ('Retention period defined and enforced?', 'no -> stop'),
    ('Error rates measured per demographic group?', 'no -> measure before deploying'),
]
for q, a in DECISION:
    print(f'- {q}\n    -> {a}')

# ---------------------------------------------------------------------
# Remember: Biometric data usually cannot be revoked. Treat it as the most sensitive category you handle.
# Common mistake: Building face recognition because the API was easy, without a lawful basis or a retention policy.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
