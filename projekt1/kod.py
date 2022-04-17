from math import sqrt
import pygad
import collections
import numpy
import os
from collections import deque
import cv2

size = 25
#   SOLVING MAZES


def countDistance(a, b):
    distance = sqrt((size-a-1)**2 + (size-b-1)**2)
    return distance


def solveMaze(maze):
    R, C = len(maze), len(maze[0])
    start = (0, 0)
    visitedPlaces = set()
    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]
    moves = 0
    while len(queue) != 0:
        coord = queue.pop()
        visitedPlaces.add((coord[0], coord[1]))
        visited[coord[0]][coord[1]] = True

        if maze[coord[0]][coord[1]] == 3:
            return [40, moves, len(visitedPlaces)]

        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == 0 or visited[nr][nc]):
                continue
            queue.appendleft((nr, nc, coord[2]+1))
        moves = moves + 1
    return [-countDistance(coord[0], coord[1]), moves, len(visitedPlaces)]

# COUNTING ZEROS AND ONES IN MAZE


def countZerosAndOnes(maze):
    zerosAndOnes = collections.Counter(maze)
    result = -size * abs(zerosAndOnes[0] - zerosAndOnes[1])
    return result

#   GENERATING MAZES


gene_space = numpy.arange(0, 1.1, dtype=int)


def fitness_func(solution, solution_idx):
    maze = []
    maze = numpy.reshape(solution, (size, size))
    countResult = countZerosAndOnes(solution)
    maze[0][0] = 2
    maze[-1][-1] = 3
    solveResult = solveMaze(maze)
    fitness = countResult + solveResult[0]*10 + solveResult[2]/(size/2)
    return fitness


fitness_function = fitness_func

sol_per_pop = 100
num_genes = size**2

num_parents_mating = 10
num_generations = 400
keep_parents = 6

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 5

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=["reach_50", "saturate_1000"])

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
ga_instance.plot_fitness()


# PRINTING SOLUTION MAZE
mazeSolution = solution * 70
maze = numpy.reshape(mazeSolution, (size, size))

im_g = cv2.imwrite("GeneratedMaze.jpg", maze)
