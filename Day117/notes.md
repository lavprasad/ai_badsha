# Day 117 — 3D and depth

Today's goal: work through **3D and depth** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Depth from stereo |
| 2 | Monocular depth estimation |
| 3 | Point clouds |
| 4 | Voxels and meshes |
| 5 | PointNet |
| 6 | NeRF and neural rendering |
| 7 | Gaussian splatting |
| 8 | Applications in robotics and AR |
| 9 | Data collection challenges |
| 10 | Evaluating 3D reconstructions |

---

## 1. Depth from stereo

3D data comes as depth maps, point clouds or meshes. Point clouds are unordered sets, so models must be permutation-invariant (that is PointNet's whole idea). NeRF and Gaussian splatting reconstruct a scene from many photos and are compute-hungry but stunning.

```python
import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))
```

**Remember:** Stereo depth error grows with the square of distance — far objects are barely measurable.

**Common mistake:** Feeding a point cloud to a model that depends on point order and getting different answers per run.

## 2. Monocular depth estimation

3D data comes as depth maps, point clouds or meshes. Point clouds are unordered sets, so models must be permutation-invariant (that is PointNet's whole idea). NeRF and Gaussian splatting reconstruct a scene from many photos and are compute-hungry but stunning.

```python
import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))
```

**Remember:** Stereo depth error grows with the square of distance — far objects are barely measurable.

**Common mistake:** Feeding a point cloud to a model that depends on point order and getting different answers per run.

## 3. Point clouds

3D data comes as depth maps, point clouds or meshes. Point clouds are unordered sets, so models must be permutation-invariant (that is PointNet's whole idea). NeRF and Gaussian splatting reconstruct a scene from many photos and are compute-hungry but stunning.

```python
import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))
```

**Remember:** Stereo depth error grows with the square of distance — far objects are barely measurable.

**Common mistake:** Feeding a point cloud to a model that depends on point order and getting different answers per run.

## 4. Voxels and meshes

3D data comes as depth maps, point clouds or meshes. Point clouds are unordered sets, so models must be permutation-invariant (that is PointNet's whole idea). NeRF and Gaussian splatting reconstruct a scene from many photos and are compute-hungry but stunning.

```python
import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))
```

**Remember:** Stereo depth error grows with the square of distance — far objects are barely measurable.

**Common mistake:** Feeding a point cloud to a model that depends on point order and getting different answers per run.

## 5. PointNet

3D data comes as depth maps, point clouds or meshes. Point clouds are unordered sets, so models must be permutation-invariant (that is PointNet's whole idea). NeRF and Gaussian splatting reconstruct a scene from many photos and are compute-hungry but stunning.

```python
import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))
```

**Remember:** Stereo depth error grows with the square of distance — far objects are barely measurable.

**Common mistake:** Feeding a point cloud to a model that depends on point order and getting different answers per run.

## 6. NeRF and neural rendering

3D data comes as depth maps, point clouds or meshes. Point clouds are unordered sets, so models must be permutation-invariant (that is PointNet's whole idea). NeRF and Gaussian splatting reconstruct a scene from many photos and are compute-hungry but stunning.

```python
import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))
```

**Remember:** Stereo depth error grows with the square of distance — far objects are barely measurable.

**Common mistake:** Feeding a point cloud to a model that depends on point order and getting different answers per run.

## 7. Gaussian splatting

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

## 8. Applications in robotics and AR

3D data comes as depth maps, point clouds or meshes. Point clouds are unordered sets, so models must be permutation-invariant (that is PointNet's whole idea). NeRF and Gaussian splatting reconstruct a scene from many photos and are compute-hungry but stunning.

```python
import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))
```

**Remember:** Stereo depth error grows with the square of distance — far objects are barely measurable.

**Common mistake:** Feeding a point cloud to a model that depends on point order and getting different answers per run.

## 9. Data collection challenges

3D data comes as depth maps, point clouds or meshes. Point clouds are unordered sets, so models must be permutation-invariant (that is PointNet's whole idea). NeRF and Gaussian splatting reconstruct a scene from many photos and are compute-hungry but stunning.

```python
import numpy as np

# Depth from stereo disparity: Z = f * B / d
focal_px, baseline_m = 700.0, 0.12
for disparity in (5, 20, 90):
    z = focal_px * baseline_m / disparity
    print(f'disparity {disparity:>3} px -> depth {z:6.2f} m')

# Permutation invariance: max-pool over points, PointNet-style
pts = np.random.default_rng(0).normal(size=(100, 3))
feat_a = pts.max(axis=0)
feat_b = pts[np.random.default_rng(1).permutation(100)].max(axis=0)
print('order-independent feature:', np.allclose(feat_a, feat_b))
```

**Remember:** Stereo depth error grows with the square of distance — far objects are barely measurable.

**Common mistake:** Feeding a point cloud to a model that depends on point order and getting different answers per run.

## 10. Evaluating 3D reconstructions

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

---

## What you should be able to do after Day 117

- Explain **Depth from stereo** to someone else without notes.
- Explain **Monocular depth estimation** to someone else without notes.
- Explain **Point clouds** to someone else without notes.
- Explain **Voxels and meshes** to someone else without notes.
- Explain **PointNet** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
