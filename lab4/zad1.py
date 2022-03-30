import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}

optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2,
                                    options=options)

stats = optimizer.optimize(fx.sphere, iters=100)

cost_history = optimizer.cost_history

plot_cost_history(cost_history)
print(cost_history)
plt.show()
