import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
f = open('comp.txt').read()
print("Original Text : ",f)

f=re.sub('[^a-z A-Z .]',' ',f)
f=re.sub(r'\s +',' ',f)
#print("without special characters: ",f)
sent_tokens=(sent_tokenize(f))
word_tokens=(word_tokenize(f))

print("\nsentence tokenized :",sent_tokens)
stop_words = set(stopwords.words('english'))

filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []  
for w in word_tokens:
    if w not in stop_words:  
        filtered_sentence.append(w)

stemming=[]
stemmer = PorterStemmer()
for i in filtered_sentence:
    stemming.append(stemmer.stem(i))

print("\nWord tokenized : ",word_tokens)
print("\nFiltered sentence : ",filtered_sentence)
print("\nAfter stemming",stemming)
  

corpus = stemming
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(corpus)
print(matrix)


"""import pandas as pd
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(stemming).todense()
# transform the matrix to a pandas df
matrix = pd.DataFrame(matrix, columns=vectorizer.get_feature_names())
# sum over each document (axis=0)
top_words = matrix.sum(axis=0).sort_values(ascending=False)
print("\nMatrix: ")
print(matrix)
"""