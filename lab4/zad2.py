# Import modules
from pyswarms.utils.plotters.formatters import Mesher
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image

# Import PySwarms
import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import (
    plot_cost_history, plot_contour, plot_surface)

options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
optimizer = ps.single.GlobalBestPSO(
    n_particles=10, dimensions=2, options=options)

cost, pos = optimizer.optimize(fx.sphere, iters=25)

m = Mesher(func=fx.sphere)
animation = plot_contour(pos_history=optimizer.pos_history,
                         mesher=m,
                         mark=(0, 0))

animation.save('plot0.gif', writer='imagemagick', fps=10)
Image(url='plot0.gif')
