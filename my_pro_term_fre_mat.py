import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

f = open('comp.txt').read()
print("Original Text : ",f)

sent_tokens=(sent_tokenize(f))
word_tokens=(word_tokenize(f))

print("Sent_token : ",sent_tokens)
print("word_token : ",word_tokens)
filtered_sent=[]
stop_words=set(stopwords.words("english"))
for w in sent_tokens:
    if w not in stop_words:
        filtered_sent.append(w)

print("filtered sent : ",filtered_sent)