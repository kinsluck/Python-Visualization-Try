# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from randomwalk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
                s=15, cmap=plt.cm.Blues, edgecolors='none')
    plt.show()
    keep_running = input('Make anther walk?(y/n):')
    if keep_running == 'n':
        break
