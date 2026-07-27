"""Day 140 — Speech and audio
Concept 5: Diarisation: who spoke when

Run:  python 05_diarisation_who_spoke_when.py
"""

import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880

# ---------------------------------------------------------------------
# Remember: Resample everything to the model's expected sample rate before inference.
# Common mistake: Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
