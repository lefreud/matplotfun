import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from numpy.random import default_rng

from os import environ

matplotlib.use("TkAgg")
random_number_generator = default_rng()
values = random_number_generator.integers(low=0, high=10, size=(2, 10))

x_points = values[0, :]
y_points = values[1, :]

fig, ax = plt.subplots()
ax.plot(x_points, y_points, marker='o')
plt.show()

print(x_points)
print(y_points)

