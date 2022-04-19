import collections
from size import getSize

size = getSize()


def countZerosAndOnes(maze):
    zerosAndOnes = collections.Counter(maze)
    result = -(size**2) * abs(zerosAndOnes[0] - zerosAndOnes[1])
    return result
