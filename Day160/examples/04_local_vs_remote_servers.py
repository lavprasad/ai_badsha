"""Day 160 — Model Context Protocol and integrations
Concept 4: Local vs remote servers

Run:  python 04_local_vs_remote_servers.py
"""

REVIEW = [
    'What data does this server receive on each call?',
    'Where does it run — my machine, my VPC, or a vendor?',
    'What credentials does it hold, and with what scope?',
    'Can its responses inject instructions into my agent loop?',
    'Is it pinned to a version, or does it auto-update?',
    'What is logged, where, and for how long?',
]
for i, q in enumerate(REVIEW, 1):
    print(f'{i}. {q}')

# ---------------------------------------------------------------------
# Remember: A tool server's response is untrusted input to your agent. Delimit it and never let it grant permissions.
# Common mistake: Installing a convenient community server with broad credentials and no review of what it sends upstream.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
