# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, edgecolor='none',s=40,c=y_values)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])
plt.show()
plt.savefig('square.png',bbox_inches='tight')