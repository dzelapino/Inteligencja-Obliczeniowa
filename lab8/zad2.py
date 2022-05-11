import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns
from sklearn.naive_bayes import GaussianNB

sns.set()

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=33)

X_test = []
y_test = []
for i in test_set:
    X_test.append([i[0], i[1], i[2], i[3]])
    y_test.append(i[4])

X_train = []
y_train = []
for i in train_set:
    X_train.append([i[0], i[1], i[2], i[3]])
    y_train.append(i[4])


gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print(y_pred)
print("Accuraccy: ", metrics.accuracy_score(y_test, y_pred))