# Day 95 — Generative adversarial networks

Aaj ka goal: **Generative adversarial networks** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

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

### Aasaan Bhasha

Comprehension poori list turant bana deti hai; generator ek-ek item deta hai aur puri sequence memory me kabhi nahi rakhta. RAM se badi dataset par generator hi 'chalta hai' aur 'crash' ke beech ka farq hai.

### Chhota code

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

**Yaad rakho:** Generator sirf ek baar consume hota hai — doosre pass ke liye use dobara banao.

**Aam galti:** Generator par `len()` lagana, ya do baar iterate karke doosri baar khaali paana.

Practice: `examples/01_generator_vs_discriminator.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. The minimax objective

### Aasaan Bhasha

GAN generator ko discriminator ke khilaaf khada karta hai: ek nakli data banata hai, doosra nakli pakadta hai, aur dono behtar hote hain. Training mashhoor tor par unstable hai — mode collapse matlab generator ko ek convincing output mil gaya aur usne khojna band kar diya. Images ke liye diffusion ne GANs ko kaafi had tak replace kar diya.

### Chhota code

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

**Yaad rakho:** Loss curves nahi, samples dekho — GAN losses progress ka signal nahi hain.

**Aam galti:** Discriminator ko bahut jaldi bahut strong hone dena, jisse generator ko gradient hi nahi milta.

Practice: `examples/02_the_minimax_objective.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Training instability

### Aasaan Bhasha

GAN generator ko discriminator ke khilaaf khada karta hai: ek nakli data banata hai, doosra nakli pakadta hai, aur dono behtar hote hain. Training mashhoor tor par unstable hai — mode collapse matlab generator ko ek convincing output mil gaya aur usne khojna band kar diya. Images ke liye diffusion ne GANs ko kaafi had tak replace kar diya.

### Chhota code

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

**Yaad rakho:** Loss curves nahi, samples dekho — GAN losses progress ka signal nahi hain.

**Aam galti:** Discriminator ko bahut jaldi bahut strong hone dena, jisse generator ko gradient hi nahi milta.

Practice: `examples/03_training_instability.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Mode collapse

### Aasaan Bhasha

GAN generator ko discriminator ke khilaaf khada karta hai: ek nakli data banata hai, doosra nakli pakadta hai, aur dono behtar hote hain. Training mashhoor tor par unstable hai — mode collapse matlab generator ko ek convincing output mil gaya aur usne khojna band kar diya. Images ke liye diffusion ne GANs ko kaafi had tak replace kar diya.

### Chhota code

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

**Yaad rakho:** Loss curves nahi, samples dekho — GAN losses progress ka signal nahi hain.

**Aam galti:** Discriminator ko bahut jaldi bahut strong hone dena, jisse generator ko gradient hi nahi milta.

Practice: `examples/04_mode_collapse.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. DCGAN architecture

### Aasaan Bhasha

Transformer block = attention + feed-forward, dono residual connection aur LayerNorm me lipte hue. Akeli attention order-blind hai, isliye positions alag se daali jaati hain. Encoder-only (BERT) samajhne ke liye, decoder-only (GPT) generation ke liye, encoder-decoder (T5) translation jaise tasks ke liye.

### Chhota code

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

**Yaad rakho:** Block = LayerNorm -> Attention -> residual add -> LayerNorm -> MLP -> residual add. Ise ratt lo.

**Aam galti:** Yeh maan lena ki bada context window muft hai — attention ka cost sequence length ke square se badhta hai.

Practice: `examples/05_dcgan_architecture.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Conditional GANs

### Aasaan Bhasha

GAN generator ko discriminator ke khilaaf khada karta hai: ek nakli data banata hai, doosra nakli pakadta hai, aur dono behtar hote hain. Training mashhoor tor par unstable hai — mode collapse matlab generator ko ek convincing output mil gaya aur usne khojna band kar diya. Images ke liye diffusion ne GANs ko kaafi had tak replace kar diya.

### Chhota code

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

**Yaad rakho:** Loss curves nahi, samples dekho — GAN losses progress ka signal nahi hain.

**Aam galti:** Discriminator ko bahut jaldi bahut strong hone dena, jisse generator ko gradient hi nahi milta.

Practice: `examples/06_conditional_gans.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. CycleGAN and unpaired translation

### Aasaan Bhasha

GAN generator ko discriminator ke khilaaf khada karta hai: ek nakli data banata hai, doosra nakli pakadta hai, aur dono behtar hote hain. Training mashhoor tor par unstable hai — mode collapse matlab generator ko ek convincing output mil gaya aur usne khojna band kar diya. Images ke liye diffusion ne GANs ko kaafi had tak replace kar diya.

### Chhota code

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

**Yaad rakho:** Loss curves nahi, samples dekho — GAN losses progress ka signal nahi hain.

**Aam galti:** Discriminator ko bahut jaldi bahut strong hone dena, jisse generator ko gradient hi nahi milta.

Practice: `examples/07_cyclegan_and_unpaired_translation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Evaluating generative models

### Aasaan Bhasha

Vibes prompt change se nahi bachte. Asli inputs ka chhota golden set banao expected outputs ke saath, har change par chalao, aur score track karo. Open-ended quality ke liye LLM judge use karo, par pehle judge ko human ratings se calibrate karo.

### Chhota code

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

**Yaad rakho:** Aapke chune hue 50 asli examples 5000 synthetic examples se behtar hain jinhe kisi ne check hi nahi kiya.

**Aam galti:** Shukravaar ko bina eval ke prompt badalna aur somvaar ko customers se pata chalna.

Practice: `examples/08_evaluating_generative_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Why diffusion largely replaced GANs

### Aasaan Bhasha

GAN generator ko discriminator ke khilaaf khada karta hai: ek nakli data banata hai, doosra nakli pakadta hai, aur dono behtar hote hain. Training mashhoor tor par unstable hai — mode collapse matlab generator ko ek convincing output mil gaya aur usne khojna band kar diya. Images ke liye diffusion ne GANs ko kaafi had tak replace kar diya.

### Chhota code

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

**Yaad rakho:** Loss curves nahi, samples dekho — GAN losses progress ka signal nahi hain.

**Aam galti:** Discriminator ko bahut jaldi bahut strong hone dena, jisse generator ko gradient hi nahi milta.

Practice: `examples/09_why_diffusion_largely_replaced_gans.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Reading GAN samples, not GAN losses

### Aasaan Bhasha

GAN generator ko discriminator ke khilaaf khada karta hai: ek nakli data banata hai, doosra nakli pakadta hai, aur dono behtar hote hain. Training mashhoor tor par unstable hai — mode collapse matlab generator ko ek convincing output mil gaya aur usne khojna band kar diya. Images ke liye diffusion ne GANs ko kaafi had tak replace kar diya.

### Chhota code

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

**Yaad rakho:** Loss curves nahi, samples dekho — GAN losses progress ka signal nahi hain.

**Aam galti:** Discriminator ko bahut jaldi bahut strong hone dena, jisse generator ko gradient hi nahi milta.

Practice: `examples/10_reading_gan_samples_not_gan_losses.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 95 ke baad aapko ye aana chahiye

- **Generator vs discriminator** ko bina notes dekhe kisi dost ko samjha sakna.
- **The minimax objective** ko bina notes dekhe kisi dost ko samjha sakna.
- **Training instability** ko bina notes dekhe kisi dost ko samjha sakna.
- **Mode collapse** ko bina notes dekhe kisi dost ko samjha sakna.
- **DCGAN architecture** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
