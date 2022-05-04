import pandas as pd
import graphviz
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
                                         random_state=13)

# X = df[['sepallength', 'sepalwidth', "petallength", "petalwidth"]]
# y = df['class']
X = train_set[:, [0, 1, 2, 3]]
y = train_set[:, [4]]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)
dot_data = tree.export_graphviz(clf, out_file=None)

tree.plot_tree(clf)

graph = graphviz.Source(dot_data)
graph.render("iris")

Xtest = test_set[:, [0, 1, 2, 3]]
Ytest = test_set[:, [4]]
print(clf.score(Xtest, Ytest))

predictions = clf.predict(Xtest)

print(confusion_matrix(test_set[:, [4]], predictions))
