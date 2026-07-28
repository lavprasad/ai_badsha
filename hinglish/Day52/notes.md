# Day 52 — Decision trees

Aaj ka goal: **Decision trees** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Splitting to increase purity |
| 2 | Gini impurity vs entropy |
| 3 | Information gain |
| 4 | Recursive partitioning |
| 5 | Depth, leaf size and pruning |
| 6 | Handling categorical and missing values |
| 7 | Regression trees |
| 8 | Reading a tree as rules |
| 9 | Instability of single trees |
| 10 | Visualising and exporting a tree |

---

## 1. Splitting to increase purity

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/01_splitting_to_increase_purity.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Gini impurity vs entropy

### Aasaan Bhasha

Entropy surprise naapti hai: fair coin me 1 bit, do-headed coin me 0. Cross-entropy naapti hai ki sach dekh kar aapka model kitna chaunka — isiliye wo classifiers aur language models ka loss hai. Perplexity bas exp(cross-entropy) hai, matlab 'kitne effective choices'.

### Chhota code

```python
import numpy as np

def cross_entropy(p_true, p_pred, eps=1e-12):
    p_pred = np.clip(p_pred, eps, 1 - eps)
    return -np.sum(p_true * np.log(p_pred))

truth = np.array([0, 1, 0])              # class 1 is correct
confident = np.array([0.05, 0.90, 0.05])
unsure = np.array([0.33, 0.34, 0.33])
print('confident loss', round(cross_entropy(truth, confident), 3))
print('unsure loss   ', round(cross_entropy(truth, unsure), 3))
print('perplexity    ', round(float(np.exp(cross_entropy(truth, unsure))), 3))
```

**Yaad rakho:** `log` se pehle probabilities clip karo — `log(0)` `-inf` hai aur poora batch kharab kar deta hai.

**Aam galti:** Softmax do baar lagana (ek model me, ek loss me) aur flat, untrainable gradients paana.

Practice: `examples/02_gini_impurity_vs_entropy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Information gain

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/03_information_gain.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Recursive partitioning

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/04_recursive_partitioning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Depth, leaf size and pruning

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/05_depth_leaf_size_and_pruning.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Handling categorical and missing values

### Aasaan Bhasha

Missing data information hai, sirf noise nahi. Kuch bharne se pehle poochho ki **kyun** missing hai: jo sensor sirf load par fail hota hai wo randomly missing nahi hai. Phir chuno: rows drop, column drop, statistic se fill, ya ek explicit 'ye missing tha' indicator column.

### Chhota code

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({'age': [25, np.nan, 40, np.nan]})
print(df.isna().sum())

df['age_missing'] = df['age'].isna().astype(int)   # keep the signal
df['age'] = df['age'].fillna(df['age'].median())    # then fill
print(df)
```

**Yaad rakho:** Fill karne wali statistic sirf TRAIN split par nikalo, phir test par lagao.

**Aam galti:** Poore dataset ke mean se fill karna — ye test ki information training me leak kar deta hai.

Practice: `examples/06_handling_categorical_and_missing_values.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Regression trees

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/07_regression_trees.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Reading a tree as rules

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/08_reading_a_tree_as_rules.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Instability of single trees

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/09_instability_of_single_trees.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Visualising and exporting a tree

### Aasaan Bhasha

Tree haan/na sawaal poochta hai aur split karke har taraf ko purer banata hai. Isse scaling nahi chahiye, ye mixed types sambhal leta hai, aur flowchart jaisa padhta hai. Bina rok-tok chhod do to ye training set ko poora ratt leta hai, isliye depth aur leaf-size limits zaroori hain.

### Chhota code

```python
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)
tree = DecisionTreeClassifier(max_depth=3, min_samples_leaf=5, random_state=0).fit(X, y)
print(export_text(tree, feature_names=load_iris().feature_names))
```

**Yaad rakho:** Ek bina-prune ka tree lagbhag hamesha chhote forest se kharab hota hai — par wo padha ja sakta hai, jo kabhi-kabhi jeet jaata hai.

**Aam galti:** Gehre tree ke feature importances par bharosa karna; wo unstable hain aur high-cardinality columns ki taraf jhukte hain.

Practice: `examples/10_visualising_and_exporting_a_tree.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 52 ke baad aapko ye aana chahiye

- **Splitting to increase purity** ko bina notes dekhe kisi dost ko samjha sakna.
- **Gini impurity vs entropy** ko bina notes dekhe kisi dost ko samjha sakna.
- **Information gain** ko bina notes dekhe kisi dost ko samjha sakna.
- **Recursive partitioning** ko bina notes dekhe kisi dost ko samjha sakna.
- **Depth, leaf size and pruning** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
