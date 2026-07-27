"""Day 113 — CLIP and multimodal vision
Concept 6: Image captioning

Run:  python 06_image_captioning.py
"""

import numpy as np

# CLIP-style zero-shot: embed image and candidate captions, pick the closest
rng = np.random.default_rng(0)
image_vec = rng.normal(size=16)
image_vec /= np.linalg.norm(image_vec)

labels = ['a photo of a dog', 'a photo of a car', 'a photo of a plate of food']
label_vecs = rng.normal(size=(3, 16))
label_vecs /= np.linalg.norm(label_vecs, axis=1, keepdims=True)

scores = label_vecs @ image_vec
print('zero-shot pick:', labels[int(np.argmax(scores))], scores.round(3))

# ---------------------------------------------------------------------
# Remember: Zero-shot quality depends heavily on prompt wording — 'a photo of a {}' beats a bare noun.
# Common mistake: Feeding an image at the wrong resolution or normalisation and getting silent quality loss.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
