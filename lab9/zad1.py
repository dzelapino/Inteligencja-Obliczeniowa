import nltk
import matplotlib.pyplot as plt
import string
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

punctuations = set(string.punctuation)          # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

with open("zad1.txt", "r") as textData:
    data = ''
    for i in textData:
        data += (i.replace('\n', ' '))

# tokenized_text = sent_tokenize(data)
# print(tokenized_text)

### B
tokenized_word = word_tokenize(data)
# print(len(tokenized_word))
#
# fdist = FreqDist(tokenized_word)
# print(fdist)
# print(fdist.most_common(4))

### C + D
stop_words = set(stopwords.words("english"))
stop_words.add("'ll")
stop_words.add("'re")

filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words and w not in punctuations:
        filtered_sent.append(w)
# print("Tokenized Sentence:", tokenized_word)
# print("Filterd Sentence:", filtered_sent)

# fdist.plot(30, cumulative=False)
# plt.show()

### E

ps = PorterStemmer()
lem = WordNetLemmatizer()

stemmed_words=[]
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))


def lematizeFunc(words):
    lematizedWords = []
    for i in words:
        lematizedWords.append(lem.lemmatize(i, 'v'))
    return lematizedWords


lematizedWords = lematizeFunc(stemmed_words)
# print(lematizedWords)

### F
fdist = FreqDist(lematizedWords)
print(len(fdist))
print(fdist.most_common(4))
# fdist.plot(10, cumulative=False)
# plt.show()

# plotData = fdist.most_common(len(fdist))
plotData = fdist.most_common(10)

fig = plt.figure()
# ax = fig.add_axes([0,0,1,1]) to psuje opisy osi
ax = fig.add_subplot(111)
x_val = [x[0] for x in plotData]
y_val = [x[1] for x in plotData]
ax.bar(x_val, y_val)
plt.show()

# plt.figure(figsize=(15,10))
# fdist.most_common(len(fdist)).sort_values(ascending=False).plot.bar()
# plt.xticks(rotation=50)
# plt.xlabel("Country of Origin")
# plt.ylabel("Number of Wines")
# plt.show()

plt.clf()

### G
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

wordcloud = WordCloud().generate(data)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

plt.clf()
