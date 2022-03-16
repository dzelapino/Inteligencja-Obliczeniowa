import pygad
import numpy

S = [("zegar", 100, 7), ("pejzaz", 300, 7), ("portret", 200, 6), ("radio", 40, 2), ("laptop", 500, 5), ("lampka", 70, 6),
     ("sztucce", 100, 1), ("porcelananana", 250, 3), ("figura", 300, 10), ("torebka", 280, 3), ("odkurzacz", 300, 15)]
maxWeight = 25

gene_space = [0, 1]


def fitness_func(solution, solution_idx):
    takes = []
    for (i, v) in enumerate(solution):
        if v == 1:
            takes.append(S[i])
    sumWeight = numpy.sum(v[2] for v in takes)
    sumValue1 = numpy.sum(v[1] for v in takes)
    if (sumWeight > maxWeight):
        fitness = 0
        return fitness
    fitness = sumValue1
    return fitness


fitness_function = fitness_func

sol_per_pop = 10
num_genes = len(S)

num_parents_mating = 4
num_generations = 30
keep_parents = 1

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 8

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
                       mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

ga_instance.plot_fitness()
