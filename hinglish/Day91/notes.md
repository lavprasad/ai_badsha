# Day 91 — Transfer learning

Aaj ka goal: **Transfer learning** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Why pretrained features transfer |
| 2 | Feature extraction: freeze the backbone |
| 3 | Fine-tuning: unfreeze at a low LR |
| 4 | Replacing the classification head |
| 5 | Discriminative learning rates per layer |
| 6 | How much data you need for each strategy |
| 7 | Domain gap and when transfer fails |
| 8 | Matching preprocessing to the pretrained model |
| 9 | Timm and torchvision model zoos |
| 10 | Fine-tuning on a few hundred images |

---

## 1. Why pretrained features transfer

### Aasaan Bhasha

Lagbhag koi bhi vision model scratch se train nahi karta. Laakhon images par pretrained network lo, aakhri layer badlo, aur ya to backbone freeze karo (kam data) ya use kam learning rate par fine-tune karo (zyada data). Applied vision me yahi sabse zyada leverage wala trick hai.

### Chhota code

```python
# Requires torch + torchvision
# import torchvision.models as models, torch.nn as nn
#
# model = models.resnet18(weights='IMAGENET1K_V1')
# for p in model.parameters():
#     p.requires_grad = False          # freeze the backbone
# model.fc = nn.Linear(model.fc.in_features, 3)   # 3 of your classes
# # only model.fc trains -> works with a few hundred images
print('Transfer learning: freeze backbone, replace head, train head, then unfreeze at low LR.')
```

**Yaad rakho:** Wahi normalisation statistics use karo jinke saath pretrained model train hua tha.

**Aam galti:** Poora network 1e-3 par fine-tune karke wo sab bahaa dena jo ImageNet ne sikhaya tha.

Practice: `examples/01_why_pretrained_features_transfer.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Feature extraction: freeze the backbone

### Aasaan Bhasha

Lagbhag koi bhi vision model scratch se train nahi karta. Laakhon images par pretrained network lo, aakhri layer badlo, aur ya to backbone freeze karo (kam data) ya use kam learning rate par fine-tune karo (zyada data). Applied vision me yahi sabse zyada leverage wala trick hai.

### Chhota code

```python
# Requires torch + torchvision
# import torchvision.models as models, torch.nn as nn
#
# model = models.resnet18(weights='IMAGENET1K_V1')
# for p in model.parameters():
#     p.requires_grad = False          # freeze the backbone
# model.fc = nn.Linear(model.fc.in_features, 3)   # 3 of your classes
# # only model.fc trains -> works with a few hundred images
print('Transfer learning: freeze backbone, replace head, train head, then unfreeze at low LR.')
```

**Yaad rakho:** Wahi normalisation statistics use karo jinke saath pretrained model train hua tha.

**Aam galti:** Poora network 1e-3 par fine-tune karke wo sab bahaa dena jo ImageNet ne sikhaya tha.

Practice: `examples/02_feature_extraction_freeze_the_backbone.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Fine-tuning: unfreeze at a low LR

### Aasaan Bhasha

Hyperparameters wo settings hain jo aap chunte ho, seekhi nahi jaatin. Grid search poora chhaanta hai aur barbaad karta hai; random search high dimensions me acche ilaake jaldi dhoondta hai; Bayesian search pichhle trials se seekhta hai. Search hamesha cross-validation ke andar karo.

### Chhota code

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Yaad rakho:** Random seed fix karo aur har trial log karo, warna aap apna hi best model dobara nahi bana paoge.

**Aam galti:** 400 rows par 40 hyperparameters tune karna — ab aap validation set hi fit kar rahe ho.

Practice: `examples/03_fine_tuning_unfreeze_at_a_low_lr.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Replacing the classification head

### Aasaan Bhasha

Lagbhag koi bhi vision model scratch se train nahi karta. Laakhon images par pretrained network lo, aakhri layer badlo, aur ya to backbone freeze karo (kam data) ya use kam learning rate par fine-tune karo (zyada data). Applied vision me yahi sabse zyada leverage wala trick hai.

### Chhota code

```python
# Requires torch + torchvision
# import torchvision.models as models, torch.nn as nn
#
# model = models.resnet18(weights='IMAGENET1K_V1')
# for p in model.parameters():
#     p.requires_grad = False          # freeze the backbone
# model.fc = nn.Linear(model.fc.in_features, 3)   # 3 of your classes
# # only model.fc trains -> works with a few hundred images
print('Transfer learning: freeze backbone, replace head, train head, then unfreeze at low LR.')
```

**Yaad rakho:** Wahi normalisation statistics use karo jinke saath pretrained model train hua tha.

**Aam galti:** Poora network 1e-3 par fine-tune karke wo sab bahaa dena jo ImageNet ne sikhaya tha.

Practice: `examples/04_replacing_the_classification_head.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Discriminative learning rates per layer

### Aasaan Bhasha

Gradient descent baar-baar gradient ke ulte kadam rakhta hai. Full-batch stable par dheema; stochastic shor wala par chhote gaddhon se nikal jaata hai; mini-batch practical beech ka raasta hai. Learning rate wo ek knob hai jise aap sabse zyada ghumaoge.

### Chhota code

```python
import numpy as np

rng = np.random.default_rng(0)
X = rng.normal(size=(1000, 3))
true_w = np.array([1.0, -2.0, 0.5])
y = X @ true_w + rng.normal(scale=0.1, size=1000)

w, lr, batch = np.zeros(3), 0.1, 32
for epoch in range(20):
    idx = rng.permutation(len(X))
    for start in range(0, len(X), batch):
        b = idx[start:start + batch]
        grad = 2 * X[b].T @ (X[b] @ w - y[b]) / len(b)
        w -= lr * grad
print('learned', np.round(w, 3), 'target', true_w)
```

**Yaad rakho:** Har epoch shuffle karo, warna model aapki file ka order seekh lega.

**Aam galti:** Learning rate ko hamesha fix rakhna, loss plateau hone par use decay na karna.

Practice: `examples/05_discriminative_learning_rates_per_layer.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. How much data you need for each strategy

### Aasaan Bhasha

Lagbhag koi bhi vision model scratch se train nahi karta. Laakhon images par pretrained network lo, aakhri layer badlo, aur ya to backbone freeze karo (kam data) ya use kam learning rate par fine-tune karo (zyada data). Applied vision me yahi sabse zyada leverage wala trick hai.

### Chhota code

```python
# Requires torch + torchvision
# import torchvision.models as models, torch.nn as nn
#
# model = models.resnet18(weights='IMAGENET1K_V1')
# for p in model.parameters():
#     p.requires_grad = False          # freeze the backbone
# model.fc = nn.Linear(model.fc.in_features, 3)   # 3 of your classes
# # only model.fc trains -> works with a few hundred images
print('Transfer learning: freeze backbone, replace head, train head, then unfreeze at low LR.')
```

**Yaad rakho:** Wahi normalisation statistics use karo jinke saath pretrained model train hua tha.

**Aam galti:** Poora network 1e-3 par fine-tune karke wo sab bahaa dena jo ImageNet ne sikhaya tha.

Practice: `examples/06_how_much_data_you_need_for_each_strategy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Domain gap and when transfer fails

### Aasaan Bhasha

Lagbhag koi bhi vision model scratch se train nahi karta. Laakhon images par pretrained network lo, aakhri layer badlo, aur ya to backbone freeze karo (kam data) ya use kam learning rate par fine-tune karo (zyada data). Applied vision me yahi sabse zyada leverage wala trick hai.

### Chhota code

```python
# Requires torch + torchvision
# import torchvision.models as models, torch.nn as nn
#
# model = models.resnet18(weights='IMAGENET1K_V1')
# for p in model.parameters():
#     p.requires_grad = False          # freeze the backbone
# model.fc = nn.Linear(model.fc.in_features, 3)   # 3 of your classes
# # only model.fc trains -> works with a few hundred images
print('Transfer learning: freeze backbone, replace head, train head, then unfreeze at low LR.')
```

**Yaad rakho:** Wahi normalisation statistics use karo jinke saath pretrained model train hua tha.

**Aam galti:** Poora network 1e-3 par fine-tune karke wo sab bahaa dena jo ImageNet ne sikhaya tha.

Practice: `examples/07_domain_gap_and_when_transfer_fails.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Matching preprocessing to the pretrained model

### Aasaan Bhasha

Imbalanced data par accuracy sab chhupa leti hai. Precision poochti hai 'jinhe maine flag kiya unme se kitne asli the'; recall poochti hai 'jo asli the unme se kitne maine pakde'. Threshold se aap ek ko doosre ke badle bechte ho, aur kaunsi galti zyada mehngi hai ye business tay karta hai.

### Chhota code

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=0)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, stratify=y, random_state=0)
m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
print(confusion_matrix(yte, m.predict(Xte)))
print(classification_report(yte, m.predict(Xte), digits=3))
print('roc auc', round(roc_auc_score(yte, m.predict_proba(Xte)[:, 1]), 4))
```

**Yaad rakho:** Decision threshold validation data par tune karo; 0.5 ek default hai, decision nahi.

**Aam galti:** Bhaari imbalanced problem par ROC-AUC optimise karna jahan imaandaar metric precision-recall AUC hai.

Practice: `examples/08_matching_preprocessing_to_the_pretrained.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Timm and torchvision model zoos

### Aasaan Bhasha

PyTorch matlab NumPy + gradients + GPU. Training loop hamesha wahi paanch lines hai: zero grads, forward, loss, backward, step. Ek baar haath se likh lo — har framework wrapper inhi paanch ko chhupa raha hota hai.

### Chhota code

```python
# Requires: pip install torch  (does not run inside the browser sandbox)
import torch
import torch.nn as nn

model = nn.Sequential(nn.Linear(4, 16), nn.ReLU(), nn.Linear(16, 1))
opt = torch.optim.AdamW(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

X = torch.randn(64, 4)
y = torch.randn(64, 1)
for step in range(50):
    opt.zero_grad()                # 1. clear old gradients
    pred = model(X)                # 2. forward
    loss = loss_fn(pred, y)        # 3. loss
    loss.backward()                # 4. backward
    opt.step()                     # 5. update
print('final loss', round(loss.item(), 4))
```

**Yaad rakho:** Har step me pehle `opt.zero_grad()`. PyTorch design se hi gradients jodta hai.

**Aam galti:** `retain_graph` ke bina `loss.backward()` do baar call karna aur confusing runtime error paana.

Practice: `examples/09_timm_and_torchvision_model_zoos.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Fine-tuning on a few hundred images

### Aasaan Bhasha

Hyperparameters wo settings hain jo aap chunte ho, seekhi nahi jaatin. Grid search poora chhaanta hai aur barbaad karta hai; random search high dimensions me acche ilaake jaldi dhoondta hai; Bayesian search pichhle trials se seekhta hai. Search hamesha cross-validation ke andar karo.

### Chhota code

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
import numpy as np

X, y = load_breast_cancer(return_X_y=True)
space = {
    'n_estimators': [100, 300, 600],
    'max_depth': [None, 4, 8, 16],
    'min_samples_leaf': [1, 2, 4, 8],
}
search = RandomizedSearchCV(
    RandomForestClassifier(random_state=0, n_jobs=-1),
    space, n_iter=12, cv=5, random_state=0,
).fit(X, y)
print(search.best_params_, round(search.best_score_, 4))
```

**Yaad rakho:** Random seed fix karo aur har trial log karo, warna aap apna hi best model dobara nahi bana paoge.

**Aam galti:** 400 rows par 40 hyperparameters tune karna — ab aap validation set hi fit kar rahe ho.

Practice: `examples/10_fine_tuning_on_a_few_hundred_images.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 91 ke baad aapko ye aana chahiye

- **Why pretrained features transfer** ko bina notes dekhe kisi dost ko samjha sakna.
- **Feature extraction: freeze the backbone** ko bina notes dekhe kisi dost ko samjha sakna.
- **Fine-tuning: unfreeze at a low LR** ko bina notes dekhe kisi dost ko samjha sakna.
- **Replacing the classification head** ko bina notes dekhe kisi dost ko samjha sakna.
- **Discriminative learning rates per layer** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
