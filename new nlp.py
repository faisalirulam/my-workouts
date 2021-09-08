import nltk
from collections import Counter
import string
from nltk.corpus import stopwords


def get_tokens():
    with open('test.txt') as pearl:
        tokens = nltk.word_tokenize(pearl.read().translate(None, string.punctuation))
    return tokens


if __name__ == "__main__":
    tokens = get_tokens()
    print("tokens[:20]=%s") % (tokens[:20])

    count = Counter(tokens)
    print("before: len(count) = %s") % (len(count))

    filtered = [w for w in tokens if not w in stopwords.words('english')]

    print("filtered tokens[:20]=%s") % (filtered[:20])

    count = Counter(filtered)
    print("after: len(count) = %s") % (len(count))

    print("most_common = %s") % (count.most_common(10))

    tagged = nltk.pos_tag(tokens)
    print("tagged[:20]=%s") % (tagged[:20])