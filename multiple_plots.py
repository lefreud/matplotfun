import matplotlib.pyplot as plt
import numpy as np


def create_quadratic_plot(axes):
    x_data = list(range(10))
    y_data = [x**2 for x in x_data]
    axes.plot(x_data, y_data, label='quadratic')
    axes.set_xlabel("x")
    axes.set_ylabel("y")


def create_linear_plot(axes):
    x_data = list(range(10))
    y_data = [x for x in x_data]
    axes.plot(x_data, y_data, label='linear')
    axes.set_xlabel("x")
    axes.set_ylabel("y")


if __name__ == '__main__':
    fig, ax = plt.subplots()
    create_quadratic_plot(ax)
    create_linear_plot(ax)
    ax.legend()
    plt.show()
