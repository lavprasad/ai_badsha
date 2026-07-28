# Day 60 — Dimensionality reduction

Aaj ka goal: **Dimensionality reduction** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why high dimensions hurt |
| 2 | PCA step by step |
| 3 | Explained variance and choosing components |
| 4 | PCA for visualisation vs for modelling |
| 5 | Kernel PCA |
| 6 | t-SNE and its pitfalls |
| 7 | UMAP |
| 8 | Truncated SVD for sparse text |
| 9 | Feature selection vs feature extraction |
| 10 | Compressing a dataset without losing signal |

---

## 1. Why high dimensions hurt

### Aasaan Bhasha

PCA data ko maximum variance wali axes par ghuma deta hai aur baaki chhodne deta hai. Ye linear, tez aur reversible hai. t-SNE aur UMAP sirf visualisation ke liye hain — t-SNE plot me clusters ke beech ki doori ka koi matlab nahi, isliye t-SNE output kabhi model me mat daalo.

### Chhota code

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Yaad rakho:** `n_components=0.95` PCA ko khud variance target se count chunne deta hai.

**Aam galti:** Scaling se pehle PCA chalana, jisse ek chaude range wala column akela component 1 ban jaata hai.

Practice: `examples/01_why_high_dimensions_hurt.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. PCA step by step

### Aasaan Bhasha

PCA data ko maximum variance wali axes par ghuma deta hai aur baaki chhodne deta hai. Ye linear, tez aur reversible hai. t-SNE aur UMAP sirf visualisation ke liye hain — t-SNE plot me clusters ke beech ki doori ka koi matlab nahi, isliye t-SNE output kabhi model me mat daalo.

### Chhota code

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Yaad rakho:** `n_components=0.95` PCA ko khud variance target se count chunne deta hai.

**Aam galti:** Scaling se pehle PCA chalana, jisse ek chaude range wala column akela component 1 ban jaata hai.

Practice: `examples/02_pca_step_by_step.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Explained variance and choosing components

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

Practice: `examples/03_explained_variance_and_choosing_componen.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. PCA for visualisation vs for modelling

### Aasaan Bhasha

Model se pehle plot karo. Histogram skew aur outliers dikhata hai, scatter non-linearity, aur residuals ka plot batata hai ki model systematically galat kahan hai. Paanch minute ka plotting ghanton ki confused tuning bacha deta hai.

### Chhota code

```python
import matplotlib
matplotlib.use('Agg')          # headless-safe for scripts/CI
import matplotlib.pyplot as plt
import numpy as np

x = np.random.default_rng(0).normal(size=500)
fig, ax = plt.subplots()
ax.hist(x, bins=30)
ax.set_title('sample distribution')
fig.savefig('hist.png', dpi=120)
print('wrote hist.png')
```

**Yaad rakho:** Axes par label lagao. Bina label ka plot sajावat hai, evidence nahi.

**Aam galti:** Sirf accuracy number dekh kar model judge karna, data ko kabhi dekhe bina.

Practice: `examples/04_pca_for_visualisation_vs_for_modelling.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Kernel PCA

### Aasaan Bhasha

Notebooks cells ke beech state rakhte hain — exploring ke liye badhiya, reproducibility ke liye bekaar. Notebook ko scratchpad samjho; jab logic pakka ho jaaye to use `.py` module me daal do jise aap import aur test kar sako.

### Chhota code

```python
# In a notebook, cell order != execution order.
# Restart & Run All before you trust any result.
import pandas as pd
df = pd.DataFrame({'x': [1, 2, 3]})
df.head()
```

**Yaad rakho:** 'Restart kernel and run all' hi ek imaandaar test hai ki notebook sach me chalta hai.

**Aam galti:** Aisa notebook dena jiska result das minute pehle delete ki gayi cell par depend karta hai.

Practice: `examples/05_kernel_pca.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. t-SNE and its pitfalls

### Aasaan Bhasha

PCA data ko maximum variance wali axes par ghuma deta hai aur baaki chhodne deta hai. Ye linear, tez aur reversible hai. t-SNE aur UMAP sirf visualisation ke liye hain — t-SNE plot me clusters ke beech ki doori ka koi matlab nahi, isliye t-SNE output kabhi model me mat daalo.

### Chhota code

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Yaad rakho:** `n_components=0.95` PCA ko khud variance target se count chunne deta hai.

**Aam galti:** Scaling se pehle PCA chalana, jisse ek chaude range wala column akela component 1 ban jaata hai.

Practice: `examples/06_t_sne_and_its_pitfalls.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. UMAP

### Aasaan Bhasha

PCA data ko maximum variance wali axes par ghuma deta hai aur baaki chhodne deta hai. Ye linear, tez aur reversible hai. t-SNE aur UMAP sirf visualisation ke liye hain — t-SNE plot me clusters ke beech ki doori ka koi matlab nahi, isliye t-SNE output kabhi model me mat daalo.

### Chhota code

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Yaad rakho:** `n_components=0.95` PCA ko khud variance target se count chunne deta hai.

**Aam galti:** Scaling se pehle PCA chalana, jisse ek chaude range wala column akela component 1 ban jaata hai.

Practice: `examples/07_umap.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Truncated SVD for sparse text

### Aasaan Bhasha

Eigenvectors wo directions hain jinhe matrix sirf khinchta hai, ghumata nahi; eigenvalue khinchne ka factor hai. SVD isi ko har matrix ke liye general kar deta hai aur PCA, low-rank compression aur LoRA adapters ke peeche yahi engine hai.

### Chhota code

```python
import numpy as np

X = np.random.default_rng(0).normal(size=(100, 5))
U, S, Vt = np.linalg.svd(X, full_matrices=False)
print('singular values', np.round(S, 2))

energy = np.cumsum(S ** 2) / np.sum(S ** 2)
print('variance kept by first 2 dims:', round(float(energy[1]), 3))
```

**Yaad rakho:** Descending order me sorted singular values batate hain ki kitne dimensions me sach me information hai.

**Aam galti:** Bina scaling ke PCA/SVD chalana, jisse sabse badi unit wala column har component par chha jaata hai.

Practice: `examples/08_truncated_svd_for_sparse_text.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Feature selection vs feature extraction

### Aasaan Bhasha

Feature engineering wahi jagah hai jahan domain knowledge compute ko harati hai. Ek ratio, ek lag, ek time-since-last-event, ya window par count aksar algorithm badalne se zyada deta hai. Selection phir un features ko hata deta hai jo signal ke bina variance badhate hain.

### Chhota code

```python
import pandas as pd

df = pd.DataFrame({
    'clicks': [10, 5, 0, 30],
    'impressions': [100, 200, 50, 300],
    'ts': pd.to_datetime(['2024-01-01', '2024-01-05', '2024-02-01', '2024-02-10']),
})
df['ctr'] = df['clicks'] / df['impressions'].clip(lower=1)   # ratio beats raw counts
df['days_since_prev'] = df['ts'].diff().dt.days.fillna(0)
df['is_weekend'] = df['ts'].dt.dayofweek.isin([5, 6]).astype(int)
print(df)
```

**Yaad rakho:** Har banaya hua feature prediction ke waqt us data se calculate hona chahiye jo tab sach me maujood hoga.

**Aam galti:** Aise column se feature banana jo us event ke BAAD hi bharta hai jise aap predict kar rahe ho.

Practice: `examples/09_feature_selection_vs_feature_extraction.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Compressing a dataset without losing signal

### Aasaan Bhasha

PCA data ko maximum variance wali axes par ghuma deta hai aur baaki chhodne deta hai. Ye linear, tez aur reversible hai. t-SNE aur UMAP sirf visualisation ke liye hain — t-SNE plot me clusters ke beech ki doori ka koi matlab nahi, isliye t-SNE output kabhi model me mat daalo.

### Chhota code

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits
import numpy as np

X, y = load_digits(return_X_y=True)
Xs = StandardScaler().fit_transform(X)
pca = PCA(n_components=0.95, random_state=0).fit(Xs)   # keep 95% of variance
print(f'{X.shape[1]} dims -> {pca.n_components_} dims, variance kept {pca.explained_variance_ratio_.sum():.3f}')
```

**Yaad rakho:** `n_components=0.95` PCA ko khud variance target se count chunne deta hai.

**Aam galti:** Scaling se pehle PCA chalana, jisse ek chaude range wala column akela component 1 ban jaata hai.

Practice: `examples/10_compressing_a_dataset_without_losing_sig.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 60 ke baad aapko ye aana chahiye

- **Why high dimensions hurt** ko bina notes dekhe kisi dost ko samjha sakna.
- **PCA step by step** ko bina notes dekhe kisi dost ko samjha sakna.
- **Explained variance and choosing components** ko bina notes dekhe kisi dost ko samjha sakna.
- **PCA for visualisation vs for modelling** ko bina notes dekhe kisi dost ko samjha sakna.
- **Kernel PCA** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
