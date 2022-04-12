from math import sqrt
import pygad
import numpy
import os

gene_space = numpy.arange(0, 1.5, dtype=int)

size = 15


def create_zero_vector(size):
    vector = []
    i = 0
    while (i < size+2):
        vector.append(0)
        i = i + 1
    return vector


def fitness_func(solution, solution_idx):
    maze = []
    maze = numpy.reshape(solution, (size, size))
    maze[0][0] = 2
    maze[-1][-1] = 3
    i = 0
    temp_maze = []
    temp_maze.append(create_zero_vector(size))
    while (i < size):
        maze1 = numpy.append(maze[i], [0], axis=0)
        maze2 = numpy.insert(maze1, 0, [0], axis=0)
        temp_maze.append(maze2)
        i = i + 1
    temp_maze.append(create_zero_vector(size))
    maze = temp_maze
    # SOLVE_MAZE

    print(maze[15])

    return 1


fitness_function = fitness_func

sol_per_pop = 1
num_genes = size**2

num_parents_mating = 1
num_generations = 1
keep_parents = 1

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
                       stop_criteria=["reach_0", "saturate_1000"])

ga_instance.run()

# SOLVING MAZES


def countDistance(a, b):
    distance = sqrt((size-a-1)**2 + (size-b-1)**2)
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


def solveMaze(matrix):
    solve_gene_space = numpy.arange(1, 5, 1)

    def solve_fitness_func(solution, solution_idx):
        moves = []
        currentPosition = [0, 0]
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
