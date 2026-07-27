# Day 110 — Video understanding

Today's goal: work through **video understanding** — ten concepts, ten runnable examples, five questions.

| # | Concept |
|--:|---------|
| 1 | Video as a sequence of frames |
| 2 | Frame sampling strategies |
| 3 | Optical flow |
| 4 | Action recognition |
| 5 | 3D convolutions |
| 6 | Temporal models over frame features |
| 7 | Object tracking |
| 8 | Real-time constraints |
| 9 | Storage and throughput planning |
| 10 | A simple activity classifier |

---

## 1. Video as a sequence of frames

Video is frames plus time. Most practical systems sample a few frames per second, embed each with an image model, and put a small temporal model on top — far cheaper than 3D convolutions. Tracking links detections across frames so 'one car seen 90 times' does not become 90 cars.

```python
def sample_frames(total_frames, fps, target_fps=2):
    """Indices of frames to keep — full-rate video is almost never necessary."""
    step = max(1, round(fps / target_fps))
    return list(range(0, total_frames, step))

keep = sample_frames(total_frames=900, fps=30, target_fps=2)
print(f'900 frames at 30fps -> {len(keep)} sampled frames ({len(keep)/900:.1%} of the work)')

def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / ua
print('same object across frames?', iou((10,10,50,50), (12,11,52,51)) > 0.5)
```

**Remember:** Sample frames to the lowest rate that still answers the question — it is the biggest cost lever in video.

**Common mistake:** Processing every frame of 30fps footage when 2fps would have given the same answer for 1/15th the cost.

## 2. Frame sampling strategies

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

## 3. Optical flow

Video is frames plus time. Most practical systems sample a few frames per second, embed each with an image model, and put a small temporal model on top — far cheaper than 3D convolutions. Tracking links detections across frames so 'one car seen 90 times' does not become 90 cars.

```python
def sample_frames(total_frames, fps, target_fps=2):
    """Indices of frames to keep — full-rate video is almost never necessary."""
    step = max(1, round(fps / target_fps))
    return list(range(0, total_frames, step))

keep = sample_frames(total_frames=900, fps=30, target_fps=2)
print(f'900 frames at 30fps -> {len(keep)} sampled frames ({len(keep)/900:.1%} of the work)')

def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / ua
print('same object across frames?', iou((10,10,50,50), (12,11,52,51)) > 0.5)
```

**Remember:** Sample frames to the lowest rate that still answers the question — it is the biggest cost lever in video.

**Common mistake:** Processing every frame of 30fps footage when 2fps would have given the same answer for 1/15th the cost.

## 4. Action recognition

Video is frames plus time. Most practical systems sample a few frames per second, embed each with an image model, and put a small temporal model on top — far cheaper than 3D convolutions. Tracking links detections across frames so 'one car seen 90 times' does not become 90 cars.

```python
def sample_frames(total_frames, fps, target_fps=2):
    """Indices of frames to keep — full-rate video is almost never necessary."""
    step = max(1, round(fps / target_fps))
    return list(range(0, total_frames, step))

keep = sample_frames(total_frames=900, fps=30, target_fps=2)
print(f'900 frames at 30fps -> {len(keep)} sampled frames ({len(keep)/900:.1%} of the work)')

def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / ua
print('same object across frames?', iou((10,10,50,50), (12,11,52,51)) > 0.5)
```

**Remember:** Sample frames to the lowest rate that still answers the question — it is the biggest cost lever in video.

**Common mistake:** Processing every frame of 30fps footage when 2fps would have given the same answer for 1/15th the cost.

## 5. 3D convolutions

A convolution slides a small learned filter over the image, so the same edge detector works anywhere in the frame. That weight sharing is why a CNN needs far fewer parameters than a dense net. Pooling shrinks the map and adds a little translation tolerance.

```python
import numpy as np

image = np.array([
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 1],
], dtype=float)
kernel = np.array([[-1, 1], [-1, 1]], dtype=float)   # vertical edge detector

h, w = image.shape[0] - 1, image.shape[1] - 1
out = np.zeros((h, w))
for i in range(h):
    for j in range(w):
        out[i, j] = float((image[i:i + 2, j:j + 2] * kernel).sum())
print(out)   # the edge column lights up
```

**Remember:** Output size = (in - kernel + 2*pad)/stride + 1. Print shapes when a layer refuses to connect.

**Common mistake:** Forgetting the channel dimension and feeding (H,W) where the layer expects (N,C,H,W).

## 6. Temporal models over frame features

Video is frames plus time. Most practical systems sample a few frames per second, embed each with an image model, and put a small temporal model on top — far cheaper than 3D convolutions. Tracking links detections across frames so 'one car seen 90 times' does not become 90 cars.

```python
def sample_frames(total_frames, fps, target_fps=2):
    """Indices of frames to keep — full-rate video is almost never necessary."""
    step = max(1, round(fps / target_fps))
    return list(range(0, total_frames, step))

keep = sample_frames(total_frames=900, fps=30, target_fps=2)
print(f'900 frames at 30fps -> {len(keep)} sampled frames ({len(keep)/900:.1%} of the work)')

def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / ua
print('same object across frames?', iou((10,10,50,50), (12,11,52,51)) > 0.5)
```

**Remember:** Sample frames to the lowest rate that still answers the question — it is the biggest cost lever in video.

**Common mistake:** Processing every frame of 30fps footage when 2fps would have given the same answer for 1/15th the cost.

## 7. Object tracking

Video is frames plus time. Most practical systems sample a few frames per second, embed each with an image model, and put a small temporal model on top — far cheaper than 3D convolutions. Tracking links detections across frames so 'one car seen 90 times' does not become 90 cars.

```python
def sample_frames(total_frames, fps, target_fps=2):
    """Indices of frames to keep — full-rate video is almost never necessary."""
    step = max(1, round(fps / target_fps))
    return list(range(0, total_frames, step))

keep = sample_frames(total_frames=900, fps=30, target_fps=2)
print(f'900 frames at 30fps -> {len(keep)} sampled frames ({len(keep)/900:.1%} of the work)')

def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / ua
print('same object across frames?', iou((10,10,50,50), (12,11,52,51)) > 0.5)
```

**Remember:** Sample frames to the lowest rate that still answers the question — it is the biggest cost lever in video.

**Common mistake:** Processing every frame of 30fps footage when 2fps would have given the same answer for 1/15th the cost.

## 8. Real-time constraints

Video is frames plus time. Most practical systems sample a few frames per second, embed each with an image model, and put a small temporal model on top — far cheaper than 3D convolutions. Tracking links detections across frames so 'one car seen 90 times' does not become 90 cars.

```python
def sample_frames(total_frames, fps, target_fps=2):
    """Indices of frames to keep — full-rate video is almost never necessary."""
    step = max(1, round(fps / target_fps))
    return list(range(0, total_frames, step))

keep = sample_frames(total_frames=900, fps=30, target_fps=2)
print(f'900 frames at 30fps -> {len(keep)} sampled frames ({len(keep)/900:.1%} of the work)')

def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / ua
print('same object across frames?', iou((10,10,50,50), (12,11,52,51)) > 0.5)
```

**Remember:** Sample frames to the lowest rate that still answers the question — it is the biggest cost lever in video.

**Common mistake:** Processing every frame of 30fps footage when 2fps would have given the same answer for 1/15th the cost.

## 9. Storage and throughput planning

RAG grounds answers in your documents: chunk, embed, store, retrieve the top-k for the question, and put them in the prompt. Retrieval quality is the whole ballgame — a perfect model answering from the wrong three chunks is still wrong.

```python
import numpy as np

docs = [
    'Refunds are processed within 5 business days.',
    'Our office is in Pune, open 9am to 6pm.',
    'Enterprise plans include a dedicated support engineer.',
]

def fake_embed(text):                       # stand-in for a real embedding model
    rng = np.random.default_rng(abs(hash(text)) % (2 ** 32))
    v = rng.normal(size=32)
    return v / np.linalg.norm(v)

index = np.array([fake_embed(d) for d in docs])
q = fake_embed('how long do refunds take')
top = int(np.argmax(index @ q))
print('retrieved:', docs[top])
print('\\nReal pipeline: chunk 300-800 tokens with overlap -> embed -> ANN index -> rerank -> prompt.')
```

**Remember:** Always show the source of each retrieved chunk in the answer so users can verify it.

**Common mistake:** Chunking blindly at 1000 characters and cutting tables and code blocks in half.

## 10. A simple activity classifier

Video is frames plus time. Most practical systems sample a few frames per second, embed each with an image model, and put a small temporal model on top — far cheaper than 3D convolutions. Tracking links detections across frames so 'one car seen 90 times' does not become 90 cars.

```python
def sample_frames(total_frames, fps, target_fps=2):
    """Indices of frames to keep — full-rate video is almost never necessary."""
    step = max(1, round(fps / target_fps))
    return list(range(0, total_frames, step))

keep = sample_frames(total_frames=900, fps=30, target_fps=2)
print(f'900 frames at 30fps -> {len(keep)} sampled frames ({len(keep)/900:.1%} of the work)')

def iou(a, b):
    x1, y1 = max(a[0], b[0]), max(a[1], b[1])
    x2, y2 = min(a[2], b[2]), min(a[3], b[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    ua = (a[2]-a[0])*(a[3]-a[1]) + (b[2]-b[0])*(b[3]-b[1]) - inter
    return inter / ua
print('same object across frames?', iou((10,10,50,50), (12,11,52,51)) > 0.5)
```

**Remember:** Sample frames to the lowest rate that still answers the question — it is the biggest cost lever in video.

**Common mistake:** Processing every frame of 30fps footage when 2fps would have given the same answer for 1/15th the cost.

---

## What you should be able to do after Day 110

- Explain **Video as a sequence of frames** to someone else without notes.
- Explain **Frame sampling strategies** to someone else without notes.
- Explain **Optical flow** to someone else without notes.
- Explain **Action recognition** to someone else without notes.
- Explain **3D convolutions** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
