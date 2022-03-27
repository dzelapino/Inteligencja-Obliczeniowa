from math import sqrt
import pygad
import numpy
import os
import random

# def showMatrix(matrix, solution):
#     matrixCopy = matrix[:]
#     os.system('clear')
#     draw = ''
#     for row in matrixCopy:
#         for item in row:
#             item = str(item).replace('1', ' ')
#             item = str(item).replace('0', '█')
#             draw += item
#         draw += '\n'
#     print(draw)

# showMatrix(matrix, [])

# gene_space = numpy.array(1, 11)
gene_space = numpy.arange(1, 5, 1)


def countDistance(a, b):
    distance = sqrt((10-a)**2 + (10-b)**2)
    return distance


def move(x, a, b):
    if(x == 1):
        return [a+1, b]
    elif(x == 2):
        return [a-1, b]
    elif(x == 3):
        return [a, b+1]
    else:
        return [a, b-1]


def fitness_func(solution, solution_idx):

    matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 'S', 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
              [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
              [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
              [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
              [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
              [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
              [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
              [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
              [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 'F', 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    moves = []
    currentPosition = [1, 1]
    i = 0
    while i < 30:
        lastPosition = currentPosition
        currentPosition = move(
            solution[i], currentPosition[0], currentPosition[1])
        moves.append(currentPosition)
        matrix[lastPosition[0]][lastPosition[1]] = 0
        if(matrix[currentPosition[0]][currentPosition[1]] == 0):
            fitness = -1 * countDistance(lastPosition[0], lastPosition[1])
            return fitness
        elif (matrix[currentPosition[0]][currentPosition[1]] == 'F'):
            # fitness = 0
            fitness = -1 * \
                countDistance(currentPosition[0], currentPosition[1])
            return fitness
        i = i + 1
    fitness = -10
    return fitness


fitness_function = fitness_func

sol_per_pop = 60
num_genes = 30

num_parents_mating = 8
num_generations = 200
keep_parents = 4

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 10

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
                       stop_criteria=["reach_0", "saturate_200"])

ga_instance.run()


solution, solution_fitness, solution_idx = ga_instance.best_solution()

print(solution)

ga_instance.plot_fitness()


def showResultMatrix(solution):
    matrixCopy = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 'S', 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                  [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
                  [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
                  [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
                  [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
                  [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
                  [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
                  [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
                  [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 'F', 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = [1, 1]
    j = 0
    while j < 30:
        lastPosition = start
        if (matrixCopy[start[0]][start[1]] == 'F'):
            j = 30
        elif (matrixCopy[start[0]][start[1]] == 0):
            j = 30
        else:
            start = move(solution[j], start[0], start[1])
            # print(start)
        matrixCopy[lastPosition[0]][lastPosition[1]] = 7
        j = j + 1

    print("RESULT: \n")
    matrixPrinter(matrixCopy)


def matrixPrinter(matrix):
    matrix[1][1] = 6
    matrix[10][10] = 8
    i = 0
    while i < len(matrix):
        print(str(matrix[i]) + "\n")
        i = i + 1


showResultMatrix(solution)
