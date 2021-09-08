import nltk
from nltk import sent_tokenize, word_tokenize, PorterStemmer
from nltk.corpus import stopwords


sentences = open("paragraph.txt").read()
tokens = nltk.word_tokenize(sentences)
print(tokens)
totaldocuments=len(tokens)
print(totaldocuments)

#frequency matrix
def _create_frequency_matrix(sentences):
    frequency_matrix = {}
    stopWords = set(stopwords.words("english"))
    ps = PorterStemmer()

    for sent in sentences:
        freq_table = {}
        words = word_tokenize(sent)
        for word in words:
            word = word.lower()
            word = ps.stem(word)
            if word in stopWords:
                continue

            if word in freq_table:
                freq_table[word] += 1
            else:
                freq_table[word] = 1

        frequency_matrix[sent[:15]] = freq_table

    return frequency_matrix

frequencymatrix=_create_frequency_matrix(sentences)
print(frequencymatrix)
