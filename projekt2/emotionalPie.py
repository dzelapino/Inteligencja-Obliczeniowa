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
    while (i < len(file)):
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

genPie(claudette, "claudette")
genPie(johnny, "johnny")
genPie(lisa, "lisa")
genPie(mark, "mark")
genPie(michelle, "michelle")
genPie(peter, "peter")
