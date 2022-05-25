import nltk
import matplotlib.pyplot as plt
import string
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

punctuations =  set(string.punctuation)          # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

nltk.download('punkt')
nltk.download('stopwords')

with open("zad1.txt", "r") as textData:
    data = ''
    for i in textData:
        data += (i.replace('\n', ' '))

# tokenized_text = sent_tokenize(data)
# print(tokenized_text)

tokenized_word = word_tokenize(data)
print(len(tokenized_word))

fdist = FreqDist(tokenized_word)
print(fdist)
print(fdist.most_common(4))

stop_words = set(stopwords.words("english"))
stop_words.add("'ll")

filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words and w not in punctuations:
        filtered_sent.append(w)
print("Tokenized Sentence:", tokenized_word)
print("Filterd Sentence:", filtered_sent)

# fdist.plot(30, cumulative=False)
# plt.show()

