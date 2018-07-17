from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk

data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
stop_words = nltk.corpus.stopwords.words('english')
symbol = ["'", '"', ':', ';', '.', ',', '-', '!', '?', "'s"]
stop_words += symbol
words = word_tokenize(data)
wordsFiltered = []

for w in words:
    if w not in stop_words:
        wordsFiltered.append(w)

print(wordsFiltered)
