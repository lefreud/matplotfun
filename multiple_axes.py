import matplotlib.pyplot as plt
import numpy as np


def create_quadratic_plot(axes):
    x_data = list(range(10))
    y_data = [x**2 for x in x_data]
    axes.plot(x_data, y_data)
    axes.set_title("quadratic")
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.set_ylim(bottom=0, top=100)


def create_linear_plot(axes):
    x_data = list(range(10))
    y_data = [x for x in x_data]
    axes.plot(x_data, y_data)
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.set_ylim(bottom=0, top=100)


if __name__ == '__main__':
    fig, (ax1, ax2) = plt.subplots(2, 1)
    create_quadratic_plot(ax1)
    create_linear_plot(ax2)
    plt.show()
