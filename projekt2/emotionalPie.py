import pandas as pd
import matplotlib.pyplot as plt

claudette = pd.read_csv('claudetteEmotions.csv')
johnny = pd.read_csv('johnnyEmotions.csv')
lisa = pd.read_csv('lisaEmotions.csv')
mark = pd.read_csv('markEmotions.csv')
michelle = pd.read_csv('michelleEmotions.csv')
peter = pd.read_csv('peterEmotions.csv')


def genPie(file, name):
    i = 0
    happy = 0
    angry = 0
    surprise = 0
    sad = 0
    fear = 0
    while i < len(file):
        happy = happy + file["Happy"].values[i]
        angry = angry + file["Angry"].values[i]
        surprise = surprise + file["Surprise"].values[i]
        sad = sad + file["Sad"].values[i]
        fear = fear + file["Fear"].values[i]
        i = i + 1
    labels = 'Happy', 'Angry', 'Surprise', 'Sad', 'Fear'
    sizes = [happy, angry,
             surprise, sad, fear]
    colors = ['lightblue', 'coral', 'purple', 'gold', 'blue']
    explode = (0.2, 0.2, 0.2, 0.2, 0.2)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=None, startangle=150)
    plt.axis('equal')
    plt.savefig(name + 'sEmotionalPie.png')
    plt.clf()


def genVaderPie(file, name):
    i = 0
    vaderneg = 0
    vaderneu = 0
    vaderpos = 0
    while (i < len(file)):
        vaderneg = vaderneg + file["VaderNeg"].values[i]
        vaderneu = vaderneu + file["VaderNeu"].values[i]
        vaderpos = vaderpos + file["VaderPos"].values[i]
        i = i + 1
    labels = 'Negative', 'Neutral', 'Positive'
    sizes = [vaderneg, vaderneu,
             vaderpos]
    colors = ['lightblue', 'coral', 'purple']
    explode = (0.2, 0.2, 0.2)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=None, startangle=150)
    plt.axis('equal')
    plt.savefig(name + 'sVaderEmotionalPie.png')
    plt.clf()

def genBlobPie(file, name):
    i = 0
    blobneg = 0
    blobneu = 0
    blobpos = 0
    while (i < len(file)):
        blobneg = blobneg + file["BlobNeg"].values[i]
        blobneu = blobneu + file["BlobNeu"].values[i]
        blobpos = blobpos + file["BlobPos"].values[i]
        i = i + 1
    labels = 'Negative', 'Neutral', 'Positive'
    sizes = [blobneg, blobneu,
             blobpos]
    colors = ['lightblue', 'coral', 'purple']
    explode = (0.2, 0.2, 0.2)
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=None, startangle=150)
    plt.axis('equal')
    plt.savefig(name + 'sBlobEmotionalPie.png')
    plt.clf()

genPie(claudette, "claudette")
genPie(johnny, "johnny")
genPie(lisa, "lisa")
genPie(mark, "mark")
genPie(michelle, "michelle")
genPie(peter, "peter")

genVaderPie(claudette, "claudette")
genVaderPie(johnny, "johnny")
genVaderPie(lisa, "lisa")
genVaderPie(mark, "mark")
genVaderPie(michelle, "michelle")
genVaderPie(peter, "peter")

genBlobPie(claudette, "claudette")
genBlobPie(johnny, "johnny")
genBlobPie(lisa, "lisa")
genBlobPie(mark, "mark")
genBlobPie(michelle, "michelle")
genBlobPie(peter, "peter")


