import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
import seaborn as sns

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


clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2, 1), random_state=1)
clf.fit(X_train, y_train)
prediction = clf.predict(X_test)

print("Accuraccy: ", metrics.accuracy_score(prediction, y_test) * 100, "%")


clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 1), random_state=1)
clf.fit(X_train, y_train)
prediction = clf.predict(X_test)

print("Accuraccy: ", metrics.accuracy_score(prediction, y_test) * 100, "%")

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 3, 1), random_state=1)
clf.fit(X_train, y_train)
prediction = clf.predict(X_test)

print("Accuraccy: ", metrics.accuracy_score(prediction, y_test) * 100, "%")