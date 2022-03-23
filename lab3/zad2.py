import pygad
import numpy
import math


def endurance(x, y, z, u, v, w):
    return math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w)


S = [0.09, 0.06, 0.99, 0.98, 0.1, 0.15]

gene_space = numpy.arange(0.00, 0.99, 0.01)


def fitness_func(solution, solution_idx):
    result = endurance(solution[0], solution[1], solution[2],
                       solution[3], solution[4], solution[5])
    return result


fitness_function = fitness_func

sol_per_pop = 6
num_genes = len(S)

num_parents_mating = 3
num_generations = 30
keep_parents = 1

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 16.67

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

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(
    solution_fitness=solution_fitness))

prediction = numpy.sum(S*solution)
print("Predicted output based on the best solution : {prediction}".format(
    prediction=prediction))

ga_instance.plot_fitness()
