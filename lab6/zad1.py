from statistics import median
import numpy as np
import pandas as pd
import math

missing_values = ["n/a", "na", "--", "-", "NA", "nA", "Na"]

irisFile = pd.read_csv(
    "/home/dzelapino/UG22/Inteligencja/INF_Krzysztof_Kolodziejski_274933/lab6/iris_with_errors.csv")
# Musiałem podać pełną ścieżkę pomimo tego że plik znajduje się w tym samym katalogu

irisFile2 = df = pd.read_csv(
    "iris_with_errors.csv", na_values=missing_values)
# A tu o dziwo nie musiałem

# Podpunkt A
print(irisFile2.isnull().sum())

sepLenMean = irisFile2["sepal.length"].mean
sepWidMean = irisFile2["sepal.width"].mean
petLenMean = irisFile2["petal.length"].mean
petWidMean = irisFile2["petal.width"].mean

# Podpunkt B
irisFile2["sepal.length"].fillna(sepLenMean, inplace=True)
irisFile2["sepal.width"].fillna(sepWidMean, inplace=True)
irisFile2["petal.length"].fillna(petLenMean, inplace=True)
irisFile2["petal.width"].fillna(petWidMean, inplace=True)
print(irisFile2.isnull().sum())


# Podpunkt C
def fixVariety():
    i = 0
    for _ in irisFile2.values:
        irisFile2.loc[i, "variety"] = irisFile2["variety"][i].upper()
        i = i + 1


fixVariety()


# Naprawianie nie używając fillna
def fixFile():
    i = 0
    for _ in irisFile.values:

        try:
            if (float(irisFile["sepal.length"][i]) > 0 and float(irisFile["sepal.length"][i]) < 15):
                pass
            else:
                irisFile["sepal.length"][i] = 0
        except:
            irisFile["sepal.length"][i] = 0

        try:
            if (float(irisFile["sepal.width"][i]) > 0 and float(irisFile["sepal.width"][i]) < 15):
                pass
            else:
                irisFile["sepal.width"][i] = 0
        except:
            irisFile["sepal.width"][i] = 0

        try:
            if (float(irisFile["petal.length"][i]) > 0 and float(irisFile["petal.length"][i]) < 15):
                pass
            else:
                irisFile["petal.length"][i] = 0
        except:
            irisFile["petal.length"][i] = 0

        try:
            if (float(irisFile["petal.width"][i]) > 0 and float(irisFile["petal.width"][i]) < 15):
                pass
            else:
                irisFile["petal.width"][i] = 0
        except:
            irisFile["petal.width"][i] = 0

        irisFile.loc[i, "variety"] = irisFile["variety"][i].upper()
        i = i + 1


# fixFile()

print(irisFile2)
