data = []

dialogTest = 0

lisaSentences = ''
johnnySentences = ''
markSentences = ''
claudetteSentences = ''
michelleSentences = ''
peterSentences = ''

scenarioLines = []

with open("TheRoom.txt", "r") as scenario:
    for i in scenario:
        scenarioLines.append(i.replace('\n', ''))

# print(len(scenarioLines))
iterator = 0


def getPersonLines(name):
    global dialogTest
    personSentences = ''
    if scenarioLines[iterator] == name:
        lineIterator = iterator + 1
        while True:
            if "(" in scenarioLines[lineIterator] or ")" in scenarioLines[lineIterator]:
                lineIterator = lineIterator + 1
            elif scenarioLines[lineIterator][0].isupper() and scenarioLines[lineIterator][1].isupper() and \
                    scenarioLines[lineIterator][2].isupper():
                break
            else:
                personSentences = personSentences + " " + scenarioLines[lineIterator]
                lineIterator = lineIterator + 1
                dialogTest = dialogTest + 1
    return personSentences


while iterator < len(scenarioLines) - 8:
    lisaSentences = lisaSentences + getPersonLines("LISA")
    johnnySentences = johnnySentences + getPersonLines("JOHNNY")
    markSentences = markSentences + getPersonLines("MARK")
    claudetteSentences = claudetteSentences + getPersonLines("CLAUDETTE")
    michelleSentences = michelleSentences + getPersonLines("MICHELLE")
    peterSentences = peterSentences + getPersonLines("PETER")
    iterator = iterator + 1

# print(lisaSentences)
# print(johnnySentences)
# print(markSentences)
print(dialogTest)
