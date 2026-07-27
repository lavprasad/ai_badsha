"""Day 69 — Working with text, classically
Concept 3: Stopwords, stemming, lemmatisation

Run:  python 03_stopwords_stemming_lemmatisation.py
"""

from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    'the cat sat on the mat',
    'the dog sat on the log',
    'machine learning models learn patterns',
]
vec = TfidfVectorizer(stop_words='english')
X = vec.fit_transform(docs)
print(vec.get_feature_names_out())
print(X.toarray().round(2))

# ---------------------------------------------------------------------
# Remember: TF-IDF + logistic regression is the baseline every LLM text classifier must beat to be worth its cost.
# Common mistake: Reaching for a 7B model to classify support tickets that TF-IDF handles at 94% for free.
#
# Try it: change one number or one line above, predict the new output,
# then run it again. Being wrong here is cheap; being wrong in production
# is not.
