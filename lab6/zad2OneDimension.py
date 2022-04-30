import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("iris.data", names=['sepal length', 'sepal width',
                 'petal length', 'petal width', 'target'])

features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values
y = df.loc[:, ['target']].values
x = StandardScaler().fit_transform(x)

# print(x)

pca = PCA(n_components=1)
principalComponents = pca.fit_transform(x)

principalDf = pd.DataFrame(data=principalComponents, columns=[
                           'principal component 1'])
finalDf = pd.concat([principalDf, df[['target']]], axis=1)

# print(pca.explained_variance_ratio_)
# print(pca.explained_variance_)

print("Zachowane zostało: " + str(100 * 0.72770452) + "% informacji")

print("Aby nie stracić powyżej 20% informacji, maksymalnie usunięte mogą zostać 2 kolumny. Gdy usuniemy 3 kolumny strata informacji wyniesie około 28%")
