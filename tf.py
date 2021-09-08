import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

def tokenize(text):
    tokens = word_tokenize(text)
    stems = []
    for item in tokens: stems.append(PorterStemmer().stem(item))
    return stems

# your corpus
text = open("text.txt").read()
print(text)
# word tokenize and stem
text = [" ".join(tokenize(text.lower())) for txt in text]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(text).todense()
# transform the matrix to a pandas df
matrix = pd.DataFrame(matrix, columns=vectorizer.get_feature_names())
# sum over each document (axis=0)
top_words = matrix.sum(axis=0).sort_values(ascending=False)
print(matrix)