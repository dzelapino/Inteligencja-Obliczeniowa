import pygad
import numpy
from size import getSize
from solveMaze import solveMaze
from countZerosAndOnes import *
from countClustersOfOnes import *
from rewardForHorizontalWalls import *
from rewardForVerticalWalls import *
from rednerSolutionImage import *
size = getSize()


gene_space = numpy.arange(0, 1.1, dtype=int)


def fitness_func(solution, solution_idx):
    maze = []
    maze = numpy.reshape(solution, (size, size))
    countResult = countZerosAndOnes(solution)
    maze[0][0] = 2
    maze[-1][-1] = 3
    solveResult = solveMaze(maze)
    clusters = countClustersOfOnes(maze)
    # horizontalWalls = rewardForHorizontalWalls(maze)
    # verticalWalls = rewardForVerticalWalls(maze)
    fitness = countResult + \
        solveResult[0] - clusters/size + solveResult[2]/(size/2)
    # fitness = solveResult[0] + verticalWalls
    # fitness = solveResult[0]*1000 + solveResult[1] + countResult * 1000
    return fitness


fitness_function = fitness_func

sol_per_pop = 100
num_genes = size**2

num_parents_mating = 10
num_generations = 300
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
                       #    stop_criteria=["reach_10000", "saturate_1000"]
                       )

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
ga_instance.plot_fitness()

renderImage(solution)
