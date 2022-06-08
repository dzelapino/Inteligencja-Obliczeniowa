import text2emotion as te
import pandas as pd
import plotly.express as px
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nrclex import NRCLex

data = []

dialogTest = 0

lisaScript = ''
johnnyScript = ''
markScript = ''
claudetteScript = ''
michelleScript = ''
peterScript = ''

scenarioLines = []

with open("TheRoom.txt", "r") as scenario:
    for i in scenario:
        scenarioLines.append(i.replace('\n', ''))

# print(len(scenarioLines))
iterator = 0


def getPersonLines(name):
    global dialogTest
    personScript = ''
    if scenarioLines[iterator] == name:
        lineIterator = iterator + 1
        while True:
            if "(" in scenarioLines[lineIterator] or ")" in scenarioLines[lineIterator]:
                lineIterator = lineIterator + 1
            elif scenarioLines[lineIterator][0].isupper() and scenarioLines[lineIterator][1].isupper() and \
                    scenarioLines[lineIterator][2].isupper():
                break
            else:
                personScript = personScript + " " + scenarioLines[lineIterator]
                lineIterator = lineIterator + 1
                dialogTest = dialogTest + 1
    return personScript


while iterator < len(scenarioLines) - 8:
    lisaScript = lisaScript + getPersonLines("LISA")
    johnnyScript = johnnyScript + getPersonLines("JOHNNY")
    markScript = markScript + getPersonLines("MARK")
    claudetteScript = claudetteScript + getPersonLines("CLAUDETTE")
    michelleScript = michelleScript + getPersonLines("MICHELLE")
    peterScript = peterScript + getPersonLines("PETER")
    iterator = iterator + 1


def extractEmotionsToFile(fileName, personScript):
    personSentences = sent_tokenize(personScript)
    sid = SentimentIntensityAnalyzer()
    with open(fileName+".csv", "w") as resultFile:
        resultFile.write('Happy,Angry,Surprise,Sad,Fear,VaderNeg,VaderNeu,VaderPos')
        for sentence in personSentences:
            happy = 0
            angry = 0
            surprise = 0
            sad = 0
            fear = 0
            vaderneg = 0
            vaderneu = 0
            vaderpos = 0
            result = te.get_emotion(sentence)
            resultVader = sid.polarity_scores(sentence)
            if result['Happy'] > 0:
                happy = 1
            if result['Angry'] > 0:
                angry = 1
            if result['Surprise'] > 0:
                surprise = 1
            if result['Sad'] > 0:
                sad = 1
            if result['Fear'] > 0:
                fear = 1
            if resultVader['neg'] > 0:
                vaderneg = 1
            if resultVader['neu'] > 0:
                vaderneu = 1
            if resultVader['pos'] > 0:
                vaderpos = 1
            resultFile.write(
                '\n' + str(happy) + "," + str(angry) + "," + str(surprise) + "," + str(sad) + "," + str(fear) + "," + str(vaderneg) + "," + str(vaderneu) + "," + str(vaderpos))
        resultFile.close()


def createEmotionFiles():
    extractEmotionsToFile("lisaEmotions", lisaScript)
    extractEmotionsToFile("johnnyEmotions", johnnyScript)
    extractEmotionsToFile("markEmotions", markScript)
    extractEmotionsToFile("claudetteEmotions", claudetteScript)
    extractEmotionsToFile("michelleEmotions", michelleScript)
    extractEmotionsToFile("peterEmotions", peterScript)


# createEmotionFiles()


def detectEmotionsWithNRC(fileName, personScript):
    nrcResult = NRCLex(personScript)
    nrcRawData = nrcResult.raw_emotion_scores
    # nrcFreqData = nrcResult.affect_frequencies
    # print(nrcFreqData)

    print(nrcResult.affect_dict)
    affect_df = pd.DataFrame.from_dict(nrcResult.affect_dict, orient='index')
    print(affect_df)

    emotion_df = pd.DataFrame.from_dict(nrcRawData, orient='index')
    emotion_df = emotion_df.reset_index()
    emotion_df = emotion_df.rename(columns={'index': 'Emotion Classification', 0: 'Emotion Count'})
    emotion_df = emotion_df.sort_values(by=['Emotion Count'], ascending=False)
    fig = px.bar(emotion_df, x='Emotion Count', y='Emotion Classification', color='Emotion Classification',
                 orientation='h', width=800, height=400)
    fig.write_image(fileName + "NrcImage.png")
    fig.show()


def createNRCPictures():
    detectEmotionsWithNRC("lisa", lisaScript)
    detectEmotionsWithNRC("johnny", johnnyScript)
    detectEmotionsWithNRC("mark", markScript)
    detectEmotionsWithNRC("claudette", claudetteScript)
    detectEmotionsWithNRC("michelle", michelleScript)
    detectEmotionsWithNRC("peter", peterScript)


# createNRCPictures()
