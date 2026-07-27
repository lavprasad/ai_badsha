"""Day 195 — Writing about your work
Concept 3: Explaining the method without jargon

Run:  python 03_explaining_the_method_without_jargon.py
"""

README = '''
# Ticket Router

Routes support tickets to the right team. **Macro F1 0.84** vs 0.61 for the
keyword rules it replaces, measured on 4,000 held-out tickets from Q1.

## Run it
    pip install -r requirements.txt
    python -m router.train --config configs/base.yaml
    python -m router.serve

## How it works
TF-IDF + linear SVM baseline, then a fine-tuned small transformer.
The transformer wins by 0.06 F1 at 12x the inference cost — see `docs/tradeoff.md`.

## Limitations
- Trained on English tickets only; Hinglish accuracy drops to 0.71.
- Degrades on tickets under 10 words (18% of volume).
'''
print(README)

# ---------------------------------------------------------------------
# Remember: Put the number in the first paragraph. If you are hiding it, the reader assumes it is bad.
# Common mistake: A README that explains your architecture for 400 lines and never says what score it achieved.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
