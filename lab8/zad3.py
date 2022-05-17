import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import seaborn as sns

scaler = StandardScaler()
sns.set()

data = pd.read_csv("iris.csv")

target = data[['class']].replace(['setosa','versicolor','virginica'],[0,1,2])

df_norm = data[['sepallength','sepalwidth','petallength','petalwidth']].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

df = pd.concat([df_norm, target], axis=1)
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

scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
y_train_oh = pd.get_dummies(y_train)
y_test_oh = pd.get_dummies(y_test)

print("4-2-1")

mlp = MLPClassifier(hidden_layer_sizes=(2), max_iter=5000)
mlp.fit(X_train, y_train)

predictions_train = mlp.predict(X_train)
print(accuracy_score(predictions_train, y_train))
predictions_test = mlp.predict(X_test)
print(accuracy_score(predictions_test, y_test))

print("4-3-1")

mlp = MLPClassifier(hidden_layer_sizes=(3), max_iter=5000)
mlp.fit(X_train, y_train)

predictions_train = mlp.predict(X_train)
print(accuracy_score(predictions_train, y_train))
predictions_test = mlp.predict(X_test)
print(accuracy_score(predictions_test, y_test))

print("4-3-3-1")

mlp = MLPClassifier(hidden_layer_sizes=(3,3), max_iter=5000)
mlp.fit(X_train, y_train)

predictions_train = mlp.predict(X_train)
print(accuracy_score(predictions_train, y_train))
predictions_test = mlp.predict(X_test)
print(accuracy_score(predictions_test, y_test))

print("4-3-3")

mlp = MLPClassifier(hidden_layer_sizes=(3), max_iter=5000)
mlp.fit(X_train, y_train_oh)

predictions_train = mlp.predict(X_train)
print(accuracy_score(predictions_train, y_train_oh))
predictions_test = mlp.predict(X_test)
print(accuracy_score(predictions_test, y_test_oh))

