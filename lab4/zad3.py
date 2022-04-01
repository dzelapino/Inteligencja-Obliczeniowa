# Import modules
from pyswarms.utils.plotters.formatters import Designer
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

pos_history_3d = m.compute_history_3d(optimizer.pos_history)

d = Designer(limits=[(-1, 1), (-1, 1), (-0.1, 1)],
             label=['x-axis', 'y-axis', 'z-axis'])

animation3d = plot_surface(pos_history=pos_history_3d,
                           mesher=m, designer=d,
                           mark=(0, 0, 0))

animation3d.save('plot3d.gif', writer='imagemagick', fps=10)
Image(url='plot3d.gif')
