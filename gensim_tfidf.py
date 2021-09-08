import gensim
import pprint
from gensim import models
from gensim import corpora
from gensim.utils import simple_preprocess
doc_list = [
   "Hello, how are you?", "How do you do?", 
   "Hey what are you doing? yes you What are you doing?"
]
doc_tokenized = [simple_preprocess(doc) for doc in doc_list]
dictionary = corpora.Dictionary()
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
for doc in BoW_corpus:
   print([[dictionary[id], freq] for id, freq in doc])
import numpy as np
tfidf = models.TfidfModel(BoW_corpus, smartirs='ntc')
for doc in tfidf[BoW_corpus]:
   print([[dictionary[id], np.around(freq,decomal=2)] for id, freq in doc])