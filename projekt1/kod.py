from math import sqrt
import pygad
import collections
import numpy
import os
from collections import deque

#   SOLVING MAZES

size = 20


def solveMaze(maze):
    R, C = len(maze), len(maze[0])
    start = (1, 1)

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False] * C for _ in range(R)]

    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        if maze[coord[0]][coord[1]] == 3:
            return 100

        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == 0 or visited[nr][nc]):
                continue
            queue.appendleft((nr, nc, coord[2]+1))

    return -10

# COUNTING ZEROS AND ONES IN MAZE


def countZerosAndOnes(maze):
    zerosAndOnes = collections.Counter(maze)
    result = 10 * abs(zerosAndOnes[0] - zerosAndOnes[1])
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
    fitness = -countResult + solveResult
    return fitness


fitness_function = fitness_func

sol_per_pop = 120
num_genes = size**2

num_parents_mating = 5
num_generations = 60
keep_parents = 4

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 25

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
                       stop_criteria=["reach_10", "saturate_1000"])

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
ga_instance.plot_fitness()
print(solution)


# PRINTING SOLUTION MAZE

lenght = len(solution)
z = 0
while (z < lenght):
    if (z % size == 0):
        print("\n" + str(solution[z]), end='')
    else:
        print(solution[z], end='')
    z = z + 1
