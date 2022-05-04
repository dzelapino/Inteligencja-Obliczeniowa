def countClustersOfOnes(maze):
    clusters = 0
    i = 0
    while (i < len(maze) - 1):
        j = 0
        while (j < len(maze[i]) - 1):
            if(maze[i][j] == 1 & maze[i+1][j] == 1 & maze[i][j + 1] == 1 & maze[i+1][j+1] == 1):
                clusters = clusters + 1
            j = j + 1
        i = i + 1
    return clusters


matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
]

matrix2 = [
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0]
]


# print(countClustersOfOnes(matrix))

def rewardForVerticalWalls(maze):
    wallRatio = 0
    j = 0
    while (j < len(maze[0])):
        i = 0
        verticalWallRatio = 2
        verticalWallMultiplier = 1
        breaker = 2
        while (i < len(maze)):
            if (maze[i][j] == 0):
                verticalWallMultiplier = verticalWallMultiplier + 0.1
                verticalWallRatio = verticalWallRatio * verticalWallMultiplier
                if (i == len(maze) - 1):
                    wallRatio = wallRatio + verticalWallRatio/breaker
            else:
                breaker = breaker ** 2
                verticalWallMultiplier = 1
                wallRatio = wallRatio + verticalWallRatio/breaker
            i = i + 1
        j = j + 1
    return wallRatio/4


print(rewardForVerticalWalls(matrix2))


def rewardForHorizontalWalls(maze):
    wallRatio = 0
    i = 0
    while (i < len(maze)):
        j = 0
        horizontalWallRatio = 2
        horizontalWallMultiplier = 1
        breaker = 2
        while (j < len(maze[i])):
            if (maze[i][j] == 0):
                horizontalWallMultiplier = horizontalWallMultiplier + 0.1
                horizontalWallRatio = horizontalWallRatio * horizontalWallMultiplier
                if (j == len(maze[i]) - 1):
                    wallRatio = wallRatio + horizontalWallRatio/breaker
            else:
                breaker = breaker ** 2
                horizontalWallMultiplier = 1
                wallRatio = wallRatio + horizontalWallRatio/breaker
            j = j + 1
        i = i + 1
    return wallRatio/4


print(rewardForHorizontalWalls(matrix2))
