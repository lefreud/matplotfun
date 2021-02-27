import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from numpy.random import default_rng
from matplotlib.animation import FuncAnimation

matplotlib.use("TkAgg")

NUM_FRAMES = 100
PLOT_SIZE = (0, 10)
NUM_POINTS = 10

random_number_generator = default_rng()
fig, ax = plt.subplots()


scatter_plot = plt.scatter([], [])


def update_animation(frame_number):
    print(f"Computing frame {frame_number}")

    values = random_number_generator.integers(*PLOT_SIZE, size=(NUM_POINTS, 2))

    scatter_plot.set_offsets(values)
    return scatter_plot,


def init_function():
    ax.set_xlim(*PLOT_SIZE)
    ax.set_ylim(*PLOT_SIZE)


animation = FuncAnimation(fig, update_animation, init_func=init_function, frames=NUM_FRAMES, repeat=False)

plt.show()
