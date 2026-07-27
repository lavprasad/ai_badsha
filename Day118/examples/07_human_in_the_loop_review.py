"""Day 118 — Vision system design
Concept 7: Human-in-the-loop review

Run:  python 07_human_in_the_loop_review.py
"""

DESIGN = {
    'decision supported': 'auto-approve low-risk claims',
    'metric + target': 'precision >= 0.98 at >= 40% coverage',
    'fallback': 'route to human queue (must handle 100% of volume)',
    'confidence gate': 'auto-approve only above calibrated p=0.95',
    'human review': '2% random audit + all rejections',
    'cost per inference': 'Rs 0.004 (batch) / Rs 0.02 (realtime)',
    'failure mode': 'model down -> everything to human queue, alert on-call',
    'monitoring': 'daily PSI on inputs, weekly precision on audited sample',
}
for k, v in DESIGN.items():
    print(f'{k:>20}: {v}')

# ---------------------------------------------------------------------
# Remember: The fallback path must handle 100% of traffic. If it cannot, you have built a single point of failure.
# Common mistake: Designing for the happy path and discovering at 3am there is no route for low-confidence cases.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
