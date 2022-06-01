data = []

# LISA
# JOHNNY
# MARK
lisa = 0
johnny = 0
mark = 0
dialogTest = 0

lisaSentences = ''
johnnySentences = ''
markSentences = ''

scenarioLines = []

with open("TheRoom.txt", "r") as scenario:
    for i in scenario:
        scenarioLines.append(i.replace('\n', ''))

# print(len(scenarioLines))
iterator = 0

while iterator < len(scenarioLines):
    if scenarioLines[iterator] == "LISA":
        lisa = lisa + 1
        lineChecker = 0
        endOfStatement = False
        while true:
            if ()


        if scenarioLines[iterator + 1][0].isupper() and scenarioLines[iterator + 1][1].islower():
            dialogTest = dialogTest + 1
    if scenarioLines[iterator] == "JOHNNY":
        johnny = johnny + 1
    if scenarioLines[iterator] == "MARK":
        mark = mark + 1
    iterator = iterator + 1


# with open("TheRoom.txt", "r") as scenario:
#     for i in scenario:
#
#         if (i == "LISA\n"):
#             lisa = lisa + 1
#             if (scenario[iterator][0].isupper() and scenario[iterator][1].islower()):
#
#
#         if (i == "JOHNNY\n"):
#             johnny = johnny + 1
#         if (i == "MARK\n"):
#             mark = mark + 1
#         iterator = iterator + 1
#         # print(i)
#         # data.append(i.replace('\n', ''))
#
#
print(lisa)
print(johnny)
print(mark)
print(dialogTest)
