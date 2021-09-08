import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
f = open('test.txt').read()
print("Original Text : ",f)

sent_tokens=(sent_tokenize(f))

word_tokens=(word_tokenize(f))

stop_words = set(stopwords.words('english'))

filtered_sentence = [w for w in word_tokens if not w in stop_words]    
filtered_sentence = []  
  
for w in word_tokens:  
    if w not in stop_words:  
        filtered_sentence.append(w)  
  
print("Word tokenized : ",word_tokens)

print("Filtered sentence : ",filtered_sentence) 




 
  

