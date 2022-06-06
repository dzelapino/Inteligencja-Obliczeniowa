import numpy
import pyswarms as ps
import matplotlib.pyplot as plt
from pyswarms.utils.plotters import plot_cost_history
from size import getSize
from solveMaze import solveMaze
from countZerosAndOnes import *
from countClustersOfOnes import *
from rewardForHorizontalWalls import *
from rewardForVerticalWalls import *
from rednerSolutionImage import *
size = getSize()


def fitness_func(solution):
    maze = []
    maze = numpy.reshape(solution, (size, size))
    countResult = countZerosAndOnes(solution)
    maze[0][0] = 2
    maze[-1][-1] = 3
    solveResult = solveMaze(maze)
    clusters = countClustersOfOnes(maze)
    # horizontalWalls = rewardForHorizontalWalls(maze)
    # verticalWalls = rewardForVerticalWalls(maze)
    # CORRECT FITNESS
    fitness = countResult + \
        solveResult[0] - clusters/size + solveResult[2]/(size/2)
    # END OF CORRECT FITNESS
    return -fitness


options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9, 'k': 2, 'p': 1}


def f(x):
    n_particles = x.shape[0]
    j = [fitness_func(x[i]) for i in range(n_particles)]
    return numpy.array(j)


optimizer = ps.discrete.BinaryPSO(n_particles=20, dimensions=size**2,
                                  options=options)
cost, pos = optimizer.optimize(f, iters=1000, verbose=True)
cost_history = optimizer.cost_history
plot_cost_history(cost_history)
plt.show()

renderImage(pos)
