import gensim
from gensim import corpora
from pprint import pprint
from gensim import models
import numpy as np

from gensim.utils import simple_preprocess
from smart_open import smart_open

import nltk
#nltk.download('stopwords')  # run once
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

#file opening
textfile = open('comp.txt',encoding='utf-8')
#textfile=["hai i am faisal","hello i am ajwa","i am munnutty"]
#tokenize
#texts = [[text for text in doc.split()] for doc in textfile]
#dictionary creation
#dictionary = corpora.Dictionary(simple_preprocess(line, deacc=True) for line in textfile)
#print(dictionary.token2id)

mydict = corpora.Dictionary([simple_preprocess(line) for line in textfile])
corpus = [mydict.doc2bow(simple_preprocess(line)) for line in textfile]
print(mydict.token2id)
#print(corpus)
# Show the Word Weights in Corpus
for doc in corpus:
    print([[mydict[id], freq] for id, freq in doc])

# Create the TF-IDF model
tfidf = models.TfidfModel(corpus, smartirs='ntc')
# Show the TF-IDF weights
for doc in tfidf[corpus]:
    print([[mydict[id], np.around(freq, decimals=2)] for id, freq in doc])