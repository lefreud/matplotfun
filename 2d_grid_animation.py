import matplotlib.pyplot as plt
import matplotlib
from numpy.random import default_rng
from matplotlib.animation import FuncAnimation
import numpy as np

matplotlib.use("TkAgg")

N = 10
grid = np.array([])


def create_grid():
    global grid
    rng = default_rng()
    grid = rng.integers(0, 2, size=(N, N))


def update_animation(frame_number):
    grid[frame_number // N, frame_number % N] += 1
    plt.imshow(grid)


if __name__ == '__main__':
    create_grid()
    fig, ax = plt.subplots()

    animation = FuncAnimation(fig, update_animation, frames=(N**2), repeat=False, interval=(1000*1/30))
    animation.save('animation.mp4', fps=30)
    plt.show()
