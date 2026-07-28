# Day 59 — Unsupervised learning: clustering

Aaj ka goal: **Unsupervised learning: clustering** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | What clustering can and cannot tell you |
| 2 | K-means and Lloyd's algorithm |
| 3 | Choosing k: elbow and silhouette |
| 4 | K-means++ initialisation |
| 5 | Limitations: shape and scale assumptions |
| 6 | DBSCAN and density clustering |
| 7 | Hierarchical clustering and dendrograms |
| 8 | Gaussian mixture models |
| 9 | Evaluating clusters without labels |
| 10 | Customer segmentation walkthrough |

---

## 1. What clustering can and cannot tell you

### Aasaan Bhasha

Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.

### Chhota code

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')
```

**Yaad rakho:** Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.

**Aam galti:** Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.

Practice: `examples/01_what_clustering_can_and_cannot_tell_you.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. K-means and Lloyd's algorithm

### Aasaan Bhasha

Mean ko outliers kheench lete hain; median ko nahi. Dono report karo, saath me spread bhi. Jab mean aur median me bada farq ho to distribution skewed hai aur average aapse jhooth bol raha hai.

### Chhota code

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Yaad rakho:** Skewed data ke liye median + IQR batao, mean + std sirf roughly symmetric data ke liye.

**Aam galti:** 'Outliers' ko apne aap hata dena jabki wahi events aapko predict karne ke liye rakha gaya tha.

Practice: `examples/02_k_means_and_lloyd_s_algorithm.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Choosing k: elbow and silhouette

### Aasaan Bhasha

Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.

### Chhota code

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')
```

**Yaad rakho:** Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.

**Aam galti:** Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.

Practice: `examples/03_choosing_k_elbow_and_silhouette.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. K-means++ initialisation

### Aasaan Bhasha

Mean ko outliers kheench lete hain; median ko nahi. Dono report karo, saath me spread bhi. Jab mean aur median me bada farq ho to distribution skewed hai aur average aapse jhooth bol raha hai.

### Chhota code

```python
import numpy as np

salaries = np.array([30, 32, 35, 33, 31, 900])   # one founder
print('mean  ', salaries.mean())     # 176.8 — misleading
print('median', np.median(salaries)) # 32.5  — honest
print('p95   ', np.percentile(salaries, 95))

q1, q3 = np.percentile(salaries, [25, 75])
iqr = q3 - q1
print('outliers', salaries[(salaries < q1 - 1.5 * iqr) | (salaries > q3 + 1.5 * iqr)])
```

**Yaad rakho:** Skewed data ke liye median + IQR batao, mean + std sirf roughly symmetric data ke liye.

**Aam galti:** 'Outliers' ko apne aap hata dena jabki wahi events aapko predict karne ke liye rakha gaya tha.

Practice: `examples/04_k_means_initialisation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Limitations: shape and scale assumptions

### Aasaan Bhasha

Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.

### Chhota code

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')
```

**Yaad rakho:** Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.

**Aam galti:** Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.

Practice: `examples/05_limitations_shape_and_scale_assumptions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. DBSCAN and density clustering

### Aasaan Bhasha

Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.

### Chhota code

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')
```

**Yaad rakho:** Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.

**Aam galti:** Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.

Practice: `examples/06_dbscan_and_density_clustering.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Hierarchical clustering and dendrograms

### Aasaan Bhasha

Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.

### Chhota code

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')
```

**Yaad rakho:** Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.

**Aam galti:** Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.

Practice: `examples/07_hierarchical_clustering_and_dendrograms.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Gaussian mixture models

### Aasaan Bhasha

Distribution batati hai kaunsi values likely hain. Measurement noise ke liye Gaussian, haan/na ke liye Bernoulli, per-interval counts ke liye Poisson. Sahi distribution chunna hi apna loss function chunna hai: Gaussian likelihood se MSE aata hai, Bernoulli se cross-entropy.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
normal = rng.normal(loc=0, scale=1, size=10_000)
coin = rng.binomial(n=1, p=0.3, size=10_000)

print('normal mean/std', round(normal.mean(), 3), round(normal.std(), 3))
print('coin heads rate ', coin.mean())
```

**Yaad rakho:** Jab result dobara banana ho to RNG hamesha seed karo (`default_rng(0)`).

**Aam galti:** Skewed, bounded ya count data par Gaussian maan lena aur phir residuals dekh kar hairan hona.

Practice: `examples/08_gaussian_mixture_models.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Evaluating clusters without labels

### Aasaan Bhasha

Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.

### Chhota code

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')
```

**Yaad rakho:** Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.

**Aam galti:** Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.

Practice: `examples/09_evaluating_clusters_without_labels.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Customer segmentation walkthrough

### Aasaan Bhasha

Clustering bina labels ke points ko group karta hai. K-means se aapko k chunna padta hai aur ye gol, ek jaise size ke blobs maan leta hai. DBSCAN kisi bhi shape ke clusters dhoondta hai aur noise mark karta hai par density radius maangta hai. Clusters ko hamesha kisi aisi cheez se validate karo jise aap samajhte ho — clustering shor me bhi khushi se structure bana degi.

### Chhota code

```python
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

X, _ = make_blobs(n_samples=500, centers=4, random_state=0)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(f'k={k}  inertia={km.inertia_:8.1f}  silhouette={silhouette_score(X, km.labels_):.3f}')
```

**Yaad rakho:** Silhouette 1 ke paas matlab tight, alag-alag clusters; 0 ke paas matlab boundaries bemaani hain.

**Aam galti:** Cluster IDs ko matlab wale labels samajh lena — wo arbitrary hain aur har run me badal jaate hain.

Practice: `examples/10_customer_segmentation_walkthrough.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 59 ke baad aapko ye aana chahiye

- **What clustering can and cannot tell you** ko bina notes dekhe kisi dost ko samjha sakna.
- **K-means and Lloyd's algorithm** ko bina notes dekhe kisi dost ko samjha sakna.
- **Choosing k: elbow and silhouette** ko bina notes dekhe kisi dost ko samjha sakna.
- **K-means++ initialisation** ko bina notes dekhe kisi dost ko samjha sakna.
- **Limitations: shape and scale assumptions** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
