import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
import numpy as np
import math
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

x_max = np.ones(6)
x_min = np.zeros(6)
my_bounds = (x_min, x_max)
bounds = my_bounds


def endurance(list):
    x = list[0]
    y = list[1]
    z = list[2]
    u = list[3]
    v = list[4]
    w = list[5]
    return -(math.exp(-2*(y-math.sin(x))**2)+math.sin(z*u)+math.cos(v*w))


def f(x):
    n_particles = x.shape[0]
    j = [endurance(x[i]) for i in range(n_particles)]
    return np.array(j)


options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=6,
                                    options=options, bounds=bounds)

optimizer.optimize(f, iters=1000)

cost_history = optimizer.cost_history

plot_cost_history(cost_history)
plt.show()
