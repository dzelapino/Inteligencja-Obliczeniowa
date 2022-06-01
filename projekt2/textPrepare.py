import text2emotion as te
from nltk.tokenize import sent_tokenize

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

# print(lisaScript)
# print(johnnyScript)
# print(markScript)
print(dialogTest)

# print(te.get_emotion(johnnyScript))
# print(te.get_emotion(lisaScript))


# def emotionsToFile(file, person):



happy = 0
angry = 0
surprise = 0
sad = 0
fear = 0
johnnySentences = sent_tokenize(johnnyScript)
# print(johnnySentences)
# for i in johnnySentences:
#     print(te.get_emotion(i))
    #'Happy': 0, 'Angry': 0, 'Surprise': 0, 'Sad': 0, 'Fear': 0}
    # happy = happy + te.get_emotion(i)['Happy']
    # angry = angry + te.get_emotion(i)['Angry']
    # surprise = surprise + te.get_emotion(i)['Surprise']
    # sad = sad + te.get_emotion(i)['Sad']
    # fear = fear + te.get_emotion(i)['Fear']

with open("emotionsTest.txt", "w") as resultFile:
    resultFile.write('Happy,Angry,Surprise,Sad,Fear\n')
    for sentence in johnnySentences:
        print(sentence)
        result = te.get_emotion(sentence)
        print(result)
        resultFile.write(str(result['Happy']) + "," + str(result['Angry']) + "," + str(result['Surprise']) + "," + str(result['Sad']) + "," + str(result['Fear']) + '\n')
    resultFile.close()

# print(str("{:.2f}".format(happy)))
# print(str("{:.2f}".format(angry)))
# print(str("{:.2f}".format(surprise)))
# print(str("{:.2f}".format(sad)))
# print(str("{:.2f}".format(fear)))
