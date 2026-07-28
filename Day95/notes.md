# Day 95 — Generative adversarial networks

Today's goal: work through **Generative adversarial networks** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Generator vs discriminator |
| 2 | The minimax objective |
| 3 | Training instability |
| 4 | Mode collapse |
| 5 | DCGAN architecture |
| 6 | Conditional GANs |
| 7 | CycleGAN and unpaired translation |
| 8 | Evaluating generative models |
| 9 | Why diffusion largely replaced GANs |
| 10 | Reading GAN samples, not GAN losses |

---

## 1. Generator vs discriminator

A comprehension builds a list eagerly; a generator produces items one at a time and never holds the whole sequence in memory. For datasets larger than RAM, generators are the difference between working and crashing.

```python
squares = [x * x for x in range(10)]          # list, all in memory
lazy = (x * x for x in range(10_000_000))    # generator, one at a time

def batches(seq, n):
    buf = []
    for item in seq:
        buf.append(item)
        if len(buf) == n:
            yield buf
            buf = []
    if buf:
        yield buf

print(sum(lazy))
print(next(batches(range(10), 3)))
```

**Remember:** A generator can only be consumed once — re-create it if you need a second pass.

**Common mistake:** Calling `len()` on a generator, or iterating it twice and getting nothing the second time.

Practice: open `examples/01_generator_vs_discriminator.py`, predict the output, change one line, predict again.

## 2. The minimax objective

A GAN pits a generator against a discriminator: one fakes data, the other spots fakes, and both improve. Training is famously unstable — mode collapse means the generator found one convincing output and stopped exploring. Diffusion has largely replaced GANs for images.

```python
# Minimax intuition, no framework needed
# generator loss  : make D(fake) high
# discriminator   : D(real) high, D(fake) low
real_score, fake_score = 0.9, 0.2
d_loss = -(0.5 * (real_score) + 0.5 * (1 - fake_score))
g_loss = -(fake_score)
print(f'discriminator loss {d_loss:.3f}  generator loss {g_loss:.3f}')
print('Balance is everything: if D wins outright, G gets no usable gradient.')
```

**Remember:** Watch samples, not the loss curves — GAN losses are not a progress signal.

**Common mistake:** Letting the discriminator get too strong too early, which starves the generator of gradient.

Practice: open `examples/02_the_minimax_objective.py`, predict the output, change one line, predict again.

## 3. Training instability

A GAN pits a generator against a discriminator: one fakes data, the other spots fakes, and both improve. Training is famously unstable — mode collapse means the generator found one convincing output and stopped exploring. Diffusion has largely replaced GANs for images.

```python
# Minimax intuition, no framework needed
# generator loss  : make D(fake) high
# discriminator   : D(real) high, D(fake) low
real_score, fake_score = 0.9, 0.2
d_loss = -(0.5 * (real_score) + 0.5 * (1 - fake_score))
g_loss = -(fake_score)
print(f'discriminator loss {d_loss:.3f}  generator loss {g_loss:.3f}')
print('Balance is everything: if D wins outright, G gets no usable gradient.')
```

**Remember:** Watch samples, not the loss curves — GAN losses are not a progress signal.

**Common mistake:** Letting the discriminator get too strong too early, which starves the generator of gradient.

Practice: open `examples/03_training_instability.py`, predict the output, change one line, predict again.

## 4. Mode collapse

A GAN pits a generator against a discriminator: one fakes data, the other spots fakes, and both improve. Training is famously unstable — mode collapse means the generator found one convincing output and stopped exploring. Diffusion has largely replaced GANs for images.

```python
# Minimax intuition, no framework needed
# generator loss  : make D(fake) high
# discriminator   : D(real) high, D(fake) low
real_score, fake_score = 0.9, 0.2
d_loss = -(0.5 * (real_score) + 0.5 * (1 - fake_score))
g_loss = -(fake_score)
print(f'discriminator loss {d_loss:.3f}  generator loss {g_loss:.3f}')
print('Balance is everything: if D wins outright, G gets no usable gradient.')
```

**Remember:** Watch samples, not the loss curves — GAN losses are not a progress signal.

**Common mistake:** Letting the discriminator get too strong too early, which starves the generator of gradient.

Practice: open `examples/04_mode_collapse.py`, predict the output, change one line, predict again.

## 5. DCGAN architecture

A transformer block is attention + feed-forward, each wrapped in a residual connection and a LayerNorm. Attention alone is order-blind, so positions are injected explicitly. Encoder-only (BERT) is for understanding, decoder-only (GPT) for generation, encoder-decoder (T5) for translation-shaped tasks.

```python
import numpy as np

def positional_encoding(seq_len, d_model):
    pos = np.arange(seq_len)[:, None]
    i = np.arange(d_model)[None, :]
    angle = pos / np.power(10_000, (2 * (i // 2)) / d_model)
    pe = np.zeros((seq_len, d_model))
    pe[:, 0::2] = np.sin(angle[:, 0::2])
    pe[:, 1::2] = np.cos(angle[:, 1::2])
    return pe

pe = positional_encoding(6, 8)
print(pe.round(2))
print('shape', pe.shape)
```

**Remember:** Block = LayerNorm -> Attention -> add residual -> LayerNorm -> MLP -> add residual. Memorise it.

**Common mistake:** Assuming a bigger context window is free — attention cost grows with the square of sequence length.

Practice: open `examples/05_dcgan_architecture.py`, predict the output, change one line, predict again.

## 6. Conditional GANs

A GAN pits a generator against a discriminator: one fakes data, the other spots fakes, and both improve. Training is famously unstable — mode collapse means the generator found one convincing output and stopped exploring. Diffusion has largely replaced GANs for images.

```python
# Minimax intuition, no framework needed
# generator loss  : make D(fake) high
# discriminator   : D(real) high, D(fake) low
real_score, fake_score = 0.9, 0.2
d_loss = -(0.5 * (real_score) + 0.5 * (1 - fake_score))
g_loss = -(fake_score)
print(f'discriminator loss {d_loss:.3f}  generator loss {g_loss:.3f}')
print('Balance is everything: if D wins outright, G gets no usable gradient.')
```

**Remember:** Watch samples, not the loss curves — GAN losses are not a progress signal.

**Common mistake:** Letting the discriminator get too strong too early, which starves the generator of gradient.

Practice: open `examples/06_conditional_gans.py`, predict the output, change one line, predict again.

## 7. CycleGAN and unpaired translation

A GAN pits a generator against a discriminator: one fakes data, the other spots fakes, and both improve. Training is famously unstable — mode collapse means the generator found one convincing output and stopped exploring. Diffusion has largely replaced GANs for images.

```python
# Minimax intuition, no framework needed
# generator loss  : make D(fake) high
# discriminator   : D(real) high, D(fake) low
real_score, fake_score = 0.9, 0.2
d_loss = -(0.5 * (real_score) + 0.5 * (1 - fake_score))
g_loss = -(fake_score)
print(f'discriminator loss {d_loss:.3f}  generator loss {g_loss:.3f}')
print('Balance is everything: if D wins outright, G gets no usable gradient.')
```

**Remember:** Watch samples, not the loss curves — GAN losses are not a progress signal.

**Common mistake:** Letting the discriminator get too strong too early, which starves the generator of gradient.

Practice: open `examples/07_cyclegan_and_unpaired_translation.py`, predict the output, change one line, predict again.

## 8. Evaluating generative models

Vibes do not survive a prompt change. Build a small golden set of real inputs with expected outputs, run it on every change, and track the score. Use an LLM judge for open-ended quality, but calibrate the judge against human ratings first.

```python
GOLDEN = [
    {'input': 'charged twice', 'expect': 'BILLING'},
    {'input': 'crashes on upload', 'expect': 'BUG'},
    {'input': 'please add dark mode', 'expect': 'FEATURE'},
]

def classify(text):                      # stand-in for the real model call
    t = text.lower()
    if 'charg' in t or 'bill' in t:
        return 'BILLING'
    if 'crash' in t or 'error' in t:
        return 'BUG'
    return 'FEATURE'

hits = sum(classify(c['input']) == c['expect'] for c in GOLDEN)
print(f'eval score {hits}/{len(GOLDEN)}')
assert hits == len(GOLDEN), 'regression: fix before shipping'
```

**Remember:** 50 real examples you curated beat 5000 synthetic ones nobody checked.

**Common mistake:** Changing the prompt on Friday with no eval and finding out from customers on Monday.

Practice: open `examples/08_evaluating_generative_models.py`, predict the output, change one line, predict again.

## 9. Why diffusion largely replaced GANs

A GAN pits a generator against a discriminator: one fakes data, the other spots fakes, and both improve. Training is famously unstable — mode collapse means the generator found one convincing output and stopped exploring. Diffusion has largely replaced GANs for images.

```python
# Minimax intuition, no framework needed
# generator loss  : make D(fake) high
# discriminator   : D(real) high, D(fake) low
real_score, fake_score = 0.9, 0.2
d_loss = -(0.5 * (real_score) + 0.5 * (1 - fake_score))
g_loss = -(fake_score)
print(f'discriminator loss {d_loss:.3f}  generator loss {g_loss:.3f}')
print('Balance is everything: if D wins outright, G gets no usable gradient.')
```

**Remember:** Watch samples, not the loss curves — GAN losses are not a progress signal.

**Common mistake:** Letting the discriminator get too strong too early, which starves the generator of gradient.

Practice: open `examples/09_why_diffusion_largely_replaced_gans.py`, predict the output, change one line, predict again.

## 10. Reading GAN samples, not GAN losses

A GAN pits a generator against a discriminator: one fakes data, the other spots fakes, and both improve. Training is famously unstable — mode collapse means the generator found one convincing output and stopped exploring. Diffusion has largely replaced GANs for images.

```python
# Minimax intuition, no framework needed
# generator loss  : make D(fake) high
# discriminator   : D(real) high, D(fake) low
real_score, fake_score = 0.9, 0.2
d_loss = -(0.5 * (real_score) + 0.5 * (1 - fake_score))
g_loss = -(fake_score)
print(f'discriminator loss {d_loss:.3f}  generator loss {g_loss:.3f}')
print('Balance is everything: if D wins outright, G gets no usable gradient.')
```

**Remember:** Watch samples, not the loss curves — GAN losses are not a progress signal.

**Common mistake:** Letting the discriminator get too strong too early, which starves the generator of gradient.

Practice: open `examples/10_reading_gan_samples_not_gan_losses.py`, predict the output, change one line, predict again.

---

## What you should be able to do after Day 95

- Explain **Generator vs discriminator** to someone else without notes.
- Explain **The minimax objective** to someone else without notes.
- Explain **Training instability** to someone else without notes.
- Explain **Mode collapse** to someone else without notes.
- Explain **DCGAN architecture** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
