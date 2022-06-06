from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string
import nltk

nltk.download('vader_lexicon')

with open("zad3negative.txt", "r") as textData:
    dataNegative = ''
    for i in textData:
        dataNegative += (i.replace('\n', ' '))

with open("zad3positive.txt", "r") as textData:
    dataPositive = ''
    for i in textData:
        dataPositive += (i.replace('\n', ' '))

print(dataNegative)
print(dataPositive)

punctuations = set(string.punctuation)
stop_words = set(stopwords.words("english"))

tokenizedNegative = sent_tokenize(dataNegative)
tokenizedPositive = sent_tokenize(dataPositive)
print(tokenizedNegative)
print(tokenizedPositive)

for sentence in tokenizedNegative:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print("End of negative sentence")

for sentence in tokenizedPositive:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        # print('{0}: {1}, '.format(k, ss[k]), end='')
        print(k, ss[k])
    print("End of positive sentence")
    