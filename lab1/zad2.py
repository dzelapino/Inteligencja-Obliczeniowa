from random import randint


vector1 = [3, 8, 9, 10, 12]
vector2 = [8, 7, 7, 5, 6]


def addAndMultiply(x, y):
    if (len(x) != len(y)):
        return False
    resultSum = []
    resultMult = []
    i = 0
    while(i < len(x)):
        resultSum.append(x[i] + y[i])
        resultMult.append(x[i] * y[i])
        i = i + 1
    return resultSum, resultMult


# print(addAndMultiply(vector1, vector2))


def scalar(x, y):
    if (len(x) != len(y)):
        return False
    resultScalar = 0
    i = 0
    while(i < len(x)):
        resultScalar = resultScalar + (x[i] * y[i])
        i = i + 1
    return resultScalar


# print(scalar(vector1, vector2))


def euklidesLen(x):
    euklidesLen = 0
    i = 0
    while(i < len(x)):
        euklidesLen = euklidesLen + x[i]**2
        i = i + 1
    return euklidesLen**(1/2)


# print(euklidesLen(vector1))


def randomVector():
    i = 0
    vector = []
    while (i < 50):
        vector.append(randint(1, 100))
        i = i + 1
    return vector


# print(randomVector())

def vectorData(x):
    if (len(x) == 0):
        return False
    i = 0
    mean = 0
    vectorMin = x[0]
    vectorMax = x[0]
    while (i < len(x)):
        mean = mean + x[i]
        if (x[i] > vectorMax):
            vectorMax = x[i]
        if (x[i] < vectorMin):
            vectorMin = x[i]
        i = i + 1
    mean = mean / len(x)
    j = 0
    sd = 0
    while (j < len(x)):
        sd = sd + (x[j] - mean)**2
        j = j + 1
    sd = (sd / len(x))**(1/2)
    return mean, sd, vectorMin, vectorMax


# print(vectorData(randomVector()))

def normalizeVector(x):
    if (len(x) == 0):
        return False
    i = 0
    mean = 0
    vectorMin = x[0]
    vectorMax = x[0]
    vectorMaxLocation = 0
    while (i < len(x)):
        mean = mean + x[i]
        if (x[i] > vectorMax):
            vectorMax = x[i]
            vectorMaxLocation = i
        if (x[i] < vectorMin):
            vectorMin = x[i]
        i = i + 1
    mean = mean / len(x)
    normalizedVector = []
    j = 0
    while (j < len(x)):
        normalizedVector.append((x[j] - vectorMin)/(vectorMax - vectorMin))
        j = j + 1
    normalizedVectorMax = 0
    normalizedVectorMaxLocation = 0
    k = 0
    while (k < len(x)):
        if (normalizedVector[k] > normalizedVectorMax):
            normalizedVectorMax = normalizedVector[k]
            normalizedVectorMaxLocation = k
        k = k + 1
    return normalizedVector, vectorMaxLocation, normalizedVectorMaxLocation


print(normalizeVector([1, 5, 2, 3]))
