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

imshow_object = None

def update_animation(frame_number):
    global imshow_object, grid
    grid[frame_number // N, frame_number % N] += 1
    # plt.imshow(grid)
    imshow_object.set_array(grid)


if __name__ == '__main__':
    create_grid()
    fig, ax = plt.subplots()

    imshow_object = plt.imshow(grid, vmin=0, vmax=4)

    animation = FuncAnimation(fig, update_animation, frames=(N**2), repeat=False)
    animation.save('animation3.mp4', fps=30)
    # plt.show()
