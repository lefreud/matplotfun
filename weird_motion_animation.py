import matplotlib.pyplot as plt
import matplotlib
from numpy.random import default_rng
from matplotlib.animation import FuncAnimation

matplotlib.use("TkAgg")

NUM_FRAMES = 10
PLOT_SIZE = (0, 10)

random_number_generator = default_rng()
fig, ax = plt.subplots()

values = random_number_generator.integers(*PLOT_SIZE, size=(2, NUM_FRAMES))

x_points = values[0, :]
y_points = values[1, :]

ln, = plt.plot([], [], marker='o')


def update_animation(frame_number):
    print(f"Computing frame {frame_number}")
    ln.set_data(x_points[:frame_number], y_points[:frame_number])
    return ln,


def init_function():
    ax.set_xlim(*PLOT_SIZE)
    ax.set_ylim(*PLOT_SIZE)


animation = FuncAnimation(fig, update_animation, init_func=init_function, frames=NUM_FRAMES, repeat=False)

plt.show()
