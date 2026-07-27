"""Day 144 — Knowledge in language models
Concept 6: Fact verification

Run:  python 06_fact_verification.py
"""

KNOWLEDGE_ROUTING = {
    'current account balance':  'database — never the model',
    'company refund policy':    'retrieval from the policy doc',
    'what is a p-value':        'model weights are fine',
    'yesterday\'s ticket count': 'database aggregate',
    'summarise this email':     'model, with the email in context',
}
for question, source in KNOWLEDGE_ROUTING.items():
    print(f'{question:<28} -> {source}')
print('\nRule: if it can change without a retrain, it must not live in weights.')

# ---------------------------------------------------------------------
# Remember: If a fact can change tomorrow, retrieve it. If it cannot, the weights may hold it.
# Common mistake: Fine-tuning prices into a model and re-running the whole job every time the price list updates.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
