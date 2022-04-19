from math import sqrt
from size import getSize

size = getSize()


def countDistance(a, b):
    distance = sqrt((size-a-1)**2 + (size-b-1)**2)
    return distance
