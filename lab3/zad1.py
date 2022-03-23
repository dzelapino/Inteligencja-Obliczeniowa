import pygad
import numpy
import time
import pandas as pd

S = [1, 2, 3, 6, 10, 17, 25, 29, 30, 41, 51, 60, 70, 79, 80]

# definiujemy parametry chromosomu
# geny to liczby: 0 lub 1
gene_space = [0, 1]

# definiujemy funkcję fitness


def fitness_func(solution, solution_idx):
    sum1 = numpy.sum(solution * S)
    solution_invert = 1 - solution
    sum2 = numpy.sum(solution_invert * S)
    fitness = -numpy.abs(sum1-sum2)
    #lub: fitness = 1.0 / (1.0 + numpy.abs(sum1-sum2))
    return fitness


fitness_function = fitness_func

# ile chromsomów w populacji
# ile genow ma chromosom
sol_per_pop = 10
num_genes = len(S)

# ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
# ile pokolen
# ilu rodzicow zachowac (kilka procent)
num_parents_mating = 5
num_generations = 30
keep_parents = 2

# jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

# w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

# mutacja ma dzialac na ilu procent genow?
# trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 8

# inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
results = []
i = 0
while i < 10:
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
                           stop_criteria=["reach_0", "saturate_30"])
    start = time.time()
    ga_instance.run()
    end = time.time()
    results.append(end - start)
    i = i + 1
    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    if ga_instance.best_solution_generation != -1:
        print("Ilość pokoleń: {best_solution_generation} ".format(
            best_solution_generation=ga_instance.best_solution_generation))

print("Średni czas: " + str(numpy.mean(results)))
