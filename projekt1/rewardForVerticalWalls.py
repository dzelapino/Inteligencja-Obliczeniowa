from size import getSize

size = getSize()


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
                verticalWallMultiplier = verticalWallMultiplier + 0.01
                verticalWallRatio = verticalWallRatio * verticalWallMultiplier
                if (i == len(maze) - 1):
                    wallRatio = wallRatio + verticalWallRatio/breaker
            else:
                breaker = breaker * 2
                verticalWallMultiplier = 1
                wallRatio = wallRatio + verticalWallRatio/breaker
            i = i + 1
        j = j + 1
    return wallRatio/size
