import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import seaborn as sns

sns.set()

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=33)

X_test = []
y_test = []
for i in train_set:
    X_test.append([i[0], i[1], i[2], i[3]])
    y_test.append(i[4])


k_parameters = [1,3,5,7,9,11]

scores = {}
scores_list = []

for k in k_parameters:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_test, y_test)
    y_pred = knn.predict(X_test)
    scores[k] = metrics.accuracy_score(y_test, y_pred)
    scores_list.append(metrics.accuracy_score(y_test, y_pred))

x = k_parameters
default_x_ticks = range(len(x))
plt.plot(default_x_ticks, scores_list, color='blue', marker='o')
plt.xticks(default_x_ticks, x)
plt.show()

print(scores)

