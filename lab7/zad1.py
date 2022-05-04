import pandas as pd

df = pd.read_csv("iris.csv")
print(df)

print(df.values)

print(df.values[:, 0])
print(df.values[5:11, :])
print(df.values[1, 4])

from sklearn.model_selection import train_test_split

(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=13)

print(test_set)
print(test_set.shape[0])

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]
