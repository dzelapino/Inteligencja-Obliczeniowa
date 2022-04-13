from math import sqrt
import pygad
import collections
import numpy
import os

#   SOLVING MAZES

size = 4


def countDistance(a, b):
    distance = sqrt((size-a)**2 + (size-b)**2)
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


def solveMaze(matrixTest):
    def solve_fitness_func(solution, solution_idx):
        matrix = matrixTest
        moves = []
        currentPosition = [1, 1]
        i = 0
        while i < 3 * size:
            lastPosition = currentPosition
            currentPosition = move(
                solution[i], currentPosition[0], currentPosition[1])
            moves.append(currentPosition)
            matrix[lastPosition[0]][lastPosition[1]] = 0
            if(matrix[currentPosition[0]][currentPosition[1]] == 0):
                fitness = -1 * countDistance(lastPosition[0], lastPosition[1])
                return fitness
            elif (matrix[currentPosition[0]][currentPosition[1]] == 3):
                fitness = 10
                # fitness = -1 * \
                #     countDistance(currentPosition[0], currentPosition[1])
                return fitness
            i = i + 1
        fitness = -10
        return fitness

    solve_gene_space = numpy.arange(1, 5, 1)
    solve_num_generations = 30
    solve_num_parents_mating = 5
    solve_fitness_function = solve_fitness_func
    solve_sol_per_pop = 4 * size
    solve_num_genes = 3 * size
    solve_parent_selection_type = "sss"
    solve_keep_parents = 2
    solve_crossover_type = "single_point"
    solve_mutation_type = "random"
    solve_mutation_percent_genes = 20
    solve_instance = pygad.GA(gene_space=solve_gene_space,
                              num_generations=solve_num_generations,
                              num_parents_mating=solve_num_parents_mating,
                              fitness_func=solve_fitness_function,
                              sol_per_pop=solve_sol_per_pop,
                              num_genes=solve_num_genes,
                              parent_selection_type=solve_parent_selection_type,
                              keep_parents=solve_keep_parents,
                              crossover_type=solve_crossover_type,
                              mutation_type=solve_mutation_type,
                              mutation_percent_genes=solve_mutation_percent_genes,
                              stop_criteria=["reach_0", "saturate_1000"])
    solve_instance.run()
    solve_solution, solve_solution_fitness, solve_solution_idx = solve_instance.best_solution()
    print(solve_solution_fitness)
    return solve_solution_fitness

# COUNTING ZEROS AND ONES IN MAZE


def countZerosAndOnes(maze):
    zerosAndOnes = collections.Counter(maze)
    result = 10 * abs(0.5 * zerosAndOnes[0] - 2 * zerosAndOnes[1])
    return result


#   GENERATING MAZES


gene_space = numpy.arange(0, 1.1, dtype=int)


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
    countResult = countZerosAndOnes(solution)
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
    solveResult = solveMaze(maze)
    fitness = -countResult + solveResult
    return fitness


fitness_function = fitness_func

sol_per_pop = 30
num_genes = size**2

num_parents_mating = 5
num_generations = 60
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
                       stop_criteria=["reach_0", "saturate_1000"])

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
ga_instance.plot_fitness()
print(solution)
