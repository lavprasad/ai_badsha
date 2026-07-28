# Day 94 — Autoencoders

Today's goal: work through **Autoencoders** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Encoder, bottleneck, decoder |
| 2 | Reconstruction loss |
| 3 | Undercomplete vs overcomplete |
| 4 | Denoising autoencoders |
| 5 | Sparse autoencoders |
| 6 | Autoencoders for anomaly detection |
| 7 | Variational autoencoders |
| 8 | The reparameterisation trick |
| 9 | Latent space arithmetic |
| 10 | Building an anomaly detector with one |

---

## 1. Encoder, bottleneck, decoder

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 2. Reconstruction loss

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 3. Undercomplete vs overcomplete

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 4. Denoising autoencoders

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 5. Sparse autoencoders

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 6. Autoencoders for anomaly detection

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 7. Variational autoencoders

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 8. The reparameterisation trick

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 9. Latent space arithmetic

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

## 10. Building an anomaly detector with one

An autoencoder squeezes input through a narrow bottleneck and reconstructs it, forcing a compact representation. A VAE makes that bottleneck a distribution so you can sample new data from it. Both are useful for anomaly detection: high reconstruction error means 'unlike anything I trained on'.

```python
import numpy as np

# Linear autoencoder == PCA. Reconstruction error flags anomalies.
rng = np.random.default_rng(0)
normal = rng.normal(size=(500, 10))
U, S, Vt = np.linalg.svd(normal - normal.mean(0), full_matrices=False)
code = Vt[:3]                              # 3-D bottleneck

def recon_error(x):
    z = (x - normal.mean(0)) @ code.T
    return float(np.linalg.norm((x - normal.mean(0)) - z @ code))

print('normal point ', round(recon_error(normal[0]), 3))
print('anomaly      ', round(recon_error(np.full(10, 12.0)), 3))
```

**Remember:** Reconstruction error is a ready-made anomaly score — no labels required.

**Common mistake:** Making the bottleneck as wide as the input, so the network learns the identity function.

---

## What you should be able to do after Day 94

- Explain **Encoder, bottleneck, decoder** to someone else without notes.
- Explain **Reconstruction loss** to someone else without notes.
- Explain **Undercomplete vs overcomplete** to someone else without notes.
- Explain **Denoising autoencoders** to someone else without notes.
- Explain **Sparse autoencoders** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
