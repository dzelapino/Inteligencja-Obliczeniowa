from collections import deque
from size import getSize
from countDistance import countDistance

size = getSize()


def solveMaze(maze):
    R, C = len(maze), len(maze[0])
    start = (0, 0)
    visitedPlaces = set()
    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]
    movesToSolve = 0
    while len(queue) != 0:
        coord = queue.pop()
        visitedPlaces.add((coord[0], coord[1]))
        visited[coord[0]][coord[1]] = True

        if maze[coord[0]][coord[1]] == 3:
            return [size**2, movesToSolve, len(visitedPlaces)]

        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == 0 or visited[nr][nc]):
                continue
            queue.appendleft((nr, nc, coord[2]+1))
        movesToSolve = movesToSolve + 1

    movesToSolve = movesToSolve
    return [-countDistance(coord[0], coord[1]), movesToSolve, len(visitedPlaces)]
