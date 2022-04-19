from size import getSize

size = getSize()


def countClustersOfOnes(maze):
    clusters = 0
    i = 0
    while (i < len(maze) - 1):
        j = 0
        while (j < len(maze[i]) - 1):
            if(maze[i][j] == 1 and maze[i+1][j] == 1 and maze[i][j + 1] == 1 and maze[i+1][j+1] == 1):
                clusters = clusters + 1
            j = j + 1
        i = i + 1
    return clusters*size
