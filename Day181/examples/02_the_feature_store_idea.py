"""Day 181 — Feature stores and data infrastructure
Concept 2: The feature store idea

Run:  python 02_the_feature_store_idea.py
"""

from datetime import datetime, timedelta

def days_since_signup(signup_at, now):
    """ONE definition, imported by both the training job and the API."""
    return (now - signup_at).days

signup = datetime(2024, 1, 1)
train_value = days_since_signup(signup, datetime(2024, 3, 1))     # batch job 'as of' date
serve_value = days_since_signup(signup, datetime(2024, 3, 1))     # request time
print('train', train_value, '| serve', serve_value, '| skew', train_value - serve_value)
print('\nIf these are computed by two different code paths, they WILL drift apart.')

# ---------------------------------------------------------------------
# Remember: One function, imported by both paths, with a test asserting they agree. That is 90% of a feature store.
# Common mistake: A SQL feature in training and a hand-written Python reimplementation in serving, silently disagreeing.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
