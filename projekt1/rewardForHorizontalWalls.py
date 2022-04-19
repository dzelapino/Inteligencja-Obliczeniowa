from size import getSize

size = getSize()


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
    return wallRatio/size
