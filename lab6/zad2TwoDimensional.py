import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv("iris.data", names=['sepal length', 'sepal width',
                 'petal length', 'petal width', 'target'])

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values
y = df.loc[:, ['target']].values
x = StandardScaler().fit_transform(x)

# print(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data=principalComponents, columns=[
                           'principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, df[['target']]], axis=1)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)
ax.set_xlabel('Principal Component 1', fontsize=15)
ax.set_ylabel('Principal Component 2', fontsize=15)
ax.set_title('2 component PCA', fontsize=20)
targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
colors = ['b', 'c', 'coral']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['target'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
               finalDf.loc[indicesToKeep, 'principal component 2'], c=color, s=50)
ax.legend(targets)
ax.grid()

plt.show()

# print(pca.explained_variance_ratio_)
# print(pca.explained_variance_)

print("Zachowane zostało: " + str(100 * (0.72770452 +
      0.23030523)) + "% informacji")

print("Aby nie stracić powyżej 20% informacji, maksymalnie usunięte mogą zostać 2 kolumny. Gdy usuniemy 3 kolumny strata informacji wyniesie około 28%")
