# Day 76 — The artificial neuron

Aaj ka goal: **The artificial neuron** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Inputs, weights, bias |
| 2 | The weighted sum |
| 3 | Activation functions |
| 4 | The perceptron and its limits |
| 5 | XOR and why one layer is not enough |
| 6 | Layers and forward propagation |
| 7 | Matrix form of a layer |
| 8 | Batch dimension |
| 9 | Counting parameters |
| 10 | A forward pass in pure NumPy |

---

## 1. Inputs, weights, bias

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/01_inputs_weights_bias.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. The weighted sum

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/02_the_weighted_sum.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. Activation functions

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/03_activation_functions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. The perceptron and its limits

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/04_the_perceptron_and_its_limits.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. XOR and why one layer is not enough

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/05_xor_and_why_one_layer_is_not_enough.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Layers and forward propagation

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/06_layers_and_forward_propagation.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Matrix form of a layer

### Aasaan Bhasha

Matrix ek linear transformation hai. Matrices ko multiply karna transformations ko jodta hai — neural network ki layers stack karna bilkul yahi hai. Shapes milni chahiye: (m,k) @ (k,n) -> (m,n); andar wale dimensions match hone chahiye aur wahi gayab ho jaate hain.

### Chhota code

```python
import numpy as np

A = np.random.default_rng(0).normal(size=(3, 4))
B = np.random.default_rng(1).normal(size=(4, 2))

print((A @ B).shape)      # (3, 2)
print(A.T.shape)          # (4, 3)
print(np.eye(3) @ A is not A, np.allclose(np.eye(3) @ A, A))
```

**Yaad rakho:** Har shape error ko 'andar wale dimensions match nahi hue' padho aur shapes print kar do.

**Aam galti:** `Ax=b` solve karne ke liye `np.linalg.inv` uthana, jabki `np.linalg.solve` zyada safe hai.

Practice: `examples/07_matrix_form_of_a_layer.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Batch dimension

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/08_batch_dimension.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Counting parameters

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/09_counting_parameters.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. A forward pass in pure NumPy

### Aasaan Bhasha

Ek neuron `activation(w·x + b)` nikaalta hai. Inhe layers me stack karo aur aap koi bhi continuous function approximate kar sakte ho. Non-linear activation ke bina das stacked layers algebra me ek hi linear layer ban jaati hain — non-linearity hi poora point hai.

### Chhota code

```python
import numpy as np

def relu(z):
    return np.maximum(0, z)

rng = np.random.default_rng(0)
x = rng.normal(size=(1, 4))
W1, b1 = rng.normal(size=(4, 8)) * 0.5, np.zeros(8)
W2, b2 = rng.normal(size=(8, 1)) * 0.5, np.zeros(1)

h = relu(x @ W1 + b1)
out = h @ W2 + b2
print('hidden', h.round(3))
print('output', out.round(3))
```

**Yaad rakho:** Bina non-linearity ke depth sirf width hai. Check karo ki har hidden layer par activation lagi hai.

**Aam galti:** Saare weights zero se shuru karna, jisse har neuron ko ek jaisa gradient milta hai aur sab ek hi cheez seekhte hain.

Practice: `examples/10_a_forward_pass_in_pure_numpy.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 76 ke baad aapko ye aana chahiye

- **Inputs, weights, bias** ko bina notes dekhe kisi dost ko samjha sakna.
- **The weighted sum** ko bina notes dekhe kisi dost ko samjha sakna.
- **Activation functions** ko bina notes dekhe kisi dost ko samjha sakna.
- **The perceptron and its limits** ko bina notes dekhe kisi dost ko samjha sakna.
- **XOR and why one layer is not enough** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
