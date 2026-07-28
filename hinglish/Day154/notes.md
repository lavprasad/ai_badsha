# Day 154 — RAG: chunking and parsing

Aaj ka goal: **RAG: chunking and parsing** ko aasaan Hinglish me samajhna — das concepts, das chalne wale examples, paanch sawaal.

Is din ko padhne ka tarika:
1. Har concept ka **Aasaan Bhasha** section padho.
2. Code sample dekho — pehle predict karo ki output kya aayega.
3. `examples/` me us concept ki file chalao (code English wali hi hai).
4. Uske BAAD hi `questions.md` kholo.

| # | Concept |
|--:|---------|
| 1 | Structure-aware chunking |
| 2 | Heading hierarchy as context |
| 3 | PDF parsing pitfalls |
| 4 | Tables, figures and captions |
| 5 | Code and config files |
| 6 | Contextual chunk headers |
| 7 | Parent-document retrieval |
| 8 | Deduplication in the index |
| 9 | Incremental index updates |
| 10 | Choosing chunk size empirically |

---

## 1. Structure-aware chunking

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/01_structure_aware_chunking.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 2. Heading hierarchy as context

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/02_heading_hierarchy_as_context.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 3. PDF parsing pitfalls

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/03_pdf_parsing_pitfalls.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 4. Tables, figures and captions

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/04_tables_figures_and_captions.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 5. Code and config files

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/05_code_and_config_files.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 6. Contextual chunk headers

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/06_contextual_chunk_headers.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 7. Parent-document retrieval

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/07_parent_document_retrieval.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 8. Deduplication in the index

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/08_deduplication_in_the_index.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 9. Incremental index updates

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/09_incremental_index_updates.py` kholo, output predict karo, ek line badlo, phir se predict karo.

## 10. Choosing chunk size empirically

### Aasaan Bhasha

RAG jawaabon ko aapke documents me jodta hai: chunk karo, embed karo, store karo, sawaal ke liye top-k retrieve karo, aur prompt me daal do. Retrieval ki quality hi poora khel hai — galat teen chunks se perfect model ka jawab bhi galat hi rahega.

### Chhota code

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

**Yaad rakho:** Jawab me har retrieved chunk ka source dikhao taaki users use verify kar sakein.

**Aam galti:** Aankh band karke 1000 characters par chunk karna aur tables aur code blocks ko beech se kaat dena.

Practice: `examples/10_choosing_chunk_size_empirically.py` kholo, output predict karo, ek line badlo, phir se predict karo.

---

## Day 154 ke baad aapko ye aana chahiye

- **Structure-aware chunking** ko bina notes dekhe kisi dost ko samjha sakna.
- **Heading hierarchy as context** ko bina notes dekhe kisi dost ko samjha sakna.
- **PDF parsing pitfalls** ko bina notes dekhe kisi dost ko samjha sakna.
- **Tables, figures and captions** ko bina notes dekhe kisi dost ko samjha sakna.
- **Code and config files** ko bina notes dekhe kisi dost ko samjha sakna.
- `examples/` ki har file chalana — aur chalane se pehle output predict karna.
- `answers.md` kholne se pehle `questions.md` ke sawaal answer karna.

Ab `examples/` kholo, har file chalao, phir use jaan-boojh kar todo aur theek karo.
