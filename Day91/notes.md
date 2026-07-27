# Day 91 — Transfer learning

Today's goal: work through **transfer learning** — ten concepts, ten runnable examples, five questions.

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

Almost nobody trains a vision model from scratch. Take a network pretrained on millions of images, replace the last layer, and either freeze the backbone (small data) or fine-tune it at a low learning rate (more data). This is the highest-leverage trick in applied vision.

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

**Remember:** Use the exact normalisation statistics the pretrained model was trained with.

**Common mistake:** Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.

## 2. Feature extraction: freeze the backbone

Almost nobody trains a vision model from scratch. Take a network pretrained on millions of images, replace the last layer, and either freeze the backbone (small data) or fine-tune it at a low learning rate (more data). This is the highest-leverage trick in applied vision.

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

**Remember:** Use the exact normalisation statistics the pretrained model was trained with.

**Common mistake:** Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.

## 3. Fine-tuning: unfreeze at a low LR

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

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

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

## 4. Replacing the classification head

Almost nobody trains a vision model from scratch. Take a network pretrained on millions of images, replace the last layer, and either freeze the backbone (small data) or fine-tune it at a low learning rate (more data). This is the highest-leverage trick in applied vision.

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

**Remember:** Use the exact normalisation statistics the pretrained model was trained with.

**Common mistake:** Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.

## 5. Discriminative learning rates per layer

Gradient descent repeatedly steps against the gradient. Full-batch is stable but slow; stochastic is noisy but escapes shallow traps; mini-batch is the practical middle. The learning rate is the single most important knob you will ever turn.

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

**Remember:** Shuffle every epoch, otherwise the model learns the order of your file.

**Common mistake:** Leaving the learning rate fixed forever instead of decaying it once the loss plateaus.

## 6. How much data you need for each strategy

Almost nobody trains a vision model from scratch. Take a network pretrained on millions of images, replace the last layer, and either freeze the backbone (small data) or fine-tune it at a low learning rate (more data). This is the highest-leverage trick in applied vision.

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

**Remember:** Use the exact normalisation statistics the pretrained model was trained with.

**Common mistake:** Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.

## 7. Domain gap and when transfer fails

Almost nobody trains a vision model from scratch. Take a network pretrained on millions of images, replace the last layer, and either freeze the backbone (small data) or fine-tune it at a low learning rate (more data). This is the highest-leverage trick in applied vision.

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

**Remember:** Use the exact normalisation statistics the pretrained model was trained with.

**Common mistake:** Fine-tuning the whole network at 1e-3 and washing away everything ImageNet taught it.

## 8. Matching preprocessing to the pretrained model

Accuracy hides everything on imbalanced data. Precision asks 'of the ones I flagged, how many were real'; recall asks 'of the real ones, how many did I catch'. You trade one for the other with the threshold, and the business decides which error hurts more.

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

**Remember:** Tune the decision threshold on validation data; 0.5 is a default, not a decision.

**Common mistake:** Optimising ROC-AUC on a heavily imbalanced problem where precision-recall AUC is the honest metric.

## 9. Timm and torchvision model zoos

PyTorch is NumPy with gradients and a GPU. The training loop is always the same five lines: zero grads, forward, loss, backward, step. Write it out by hand once — every framework wrapper is just hiding these five.

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

**Remember:** `opt.zero_grad()` first, every step. PyTorch accumulates gradients by design.

**Common mistake:** Calling `loss.backward()` twice without `retain_graph` and getting a confusing runtime error.

## 10. Fine-tuning on a few hundred images

Hyperparameters are the settings you choose, not learn. Grid search is exhaustive and wasteful; random search finds good regions faster in high dimensions; Bayesian search learns from previous trials. Always search inside cross-validation.

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

**Remember:** Fix the random seed and log every trial, or you cannot reproduce your own best model.

**Common mistake:** Tuning 40 hyperparameters on 400 rows — you are now fitting the validation set.

---

## What you should be able to do after Day 91

- Explain **Why pretrained features transfer** to someone else without notes.
- Explain **Feature extraction: freeze the backbone** to someone else without notes.
- Explain **Fine-tuning: unfreeze at a low LR** to someone else without notes.
- Explain **Replacing the classification head** to someone else without notes.
- Explain **Discriminative learning rates per layer** to someone else without notes.
- Run every file in `examples/` and predict its output before running it.
- Answer `questions.md` before opening `answers.md`.

Now open `examples/`, run each file, then break it on purpose and fix it.
