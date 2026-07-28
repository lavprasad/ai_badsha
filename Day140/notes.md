# Day 140 — Speech and audio

Today's goal: work through **Speech and audio** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Waveforms and sampling rates |
| 2 | Spectrograms and mel scale |
| 3 | Automatic speech recognition |
| 4 | Whisper and its trade-offs |
| 5 | Diarisation: who spoke when |
| 6 | Text-to-speech |
| 7 | Voice cloning and its ethics |
| 8 | Real-time streaming ASR |
| 9 | Noise robustness |
| 10 | A meeting transcription pipeline |

---

## 1. Waveforms and sampling rates

A distribution says which values are likely. Gaussian for measurement noise, Bernoulli for yes/no, Poisson for counts per interval. Choosing the right one is choosing your loss function: Gaussian likelihood gives MSE, Bernoulli gives cross-entropy.

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Remember:** Always seed your RNG (`default_rng(0)`) when you want a result someone else can reproduce.

**Common mistake:** Assuming Gaussian for skewed, bounded, or count data and then being surprised by the residuals.

## 2. Spectrograms and mel scale

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

## 3. Automatic speech recognition

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

## 4. Whisper and its trade-offs

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

## 5. Diarisation: who spoke when

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

## 6. Text-to-speech

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

## 7. Voice cloning and its ethics

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

## 8. Real-time streaming ASR

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

## 9. Noise robustness

Audio becomes a spectrogram — time on one axis, frequency on the other — and from there it is an image problem. ASR transcribes speech to text; TTS goes the other way. Watch for accent and background-noise bias in the training data.

```python
import numpy as np

sr = 16_000
t = np.linspace(0, 1, sr, endpoint=False)
signal = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)

spectrum = np.abs(np.fft.rfft(signal))
freqs = np.fft.rfftfreq(len(signal), 1 / sr)
peaks = freqs[np.argsort(-spectrum)[:2]]
print('dominant frequencies (Hz):', np.sort(peaks))   # ~440 and ~880
```

**Remember:** Resample everything to the model's expected sample rate before inference.

**Common mistake:** Evaluating ASR only on clean studio audio, then deploying to a noisy call centre.

## 10. A meeting transcription pipeline

A Pipeline chains preprocessing and the model into one object that fits and predicts as a unit. This is the single best defence against leakage, and it means deployment ships one artefact instead of six loose steps you must remember to repeat.

```python
import numpy as np, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame({'age': [25, np.nan, 40, 33], 'city': ['pune', 'delhi', 'pune', 'delhi']})
y = [0, 1, 0, 1]

pre = ColumnTransformer([
    ('num', Pipeline([('imp', SimpleImputer(strategy='median')), ('sc', StandardScaler())]), ['age']),
    ('cat', OneHotEncoder(handle_unknown='ignore'), ['city']),
])
model = Pipeline([('pre', pre), ('clf', LogisticRegression())]).fit(df, y)
print(model.predict(df))
```

**Remember:** `handle_unknown='ignore'` stops production crashing on a category you never saw in training.

**Common mistake:** Preprocessing in a notebook and then forgetting one step when writing the serving code.

---

## What you should be able to do after Day 140

- Explain **Waveforms and sampling rates** to someone else without notes.
- Explain **Spectrograms and mel scale** to someone else without notes.
- Explain **Automatic speech recognition** to someone else without notes.
- Explain **Whisper and its trade-offs** to someone else without notes.
- Explain **Diarisation: who spoke when** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
