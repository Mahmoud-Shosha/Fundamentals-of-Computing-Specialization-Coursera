"""
Example comparisons of growth rates
"""

import matplotlib.pyplot as plt


def f(n):
    """
    A test function, of degree 3
    """
    return 0.1 * n ** 3 + 20 * n


def g(n):
    """
    A test function, of degree 3, 2, 4
    """
    return n ** 3
    # return 20 * n ** 2
    # return .1 * n ** 4


def make_plot(fun1, fun2, plot_length):
    """
    Create a plot relating the growth of fun1 vs. fun2
    """
    y_coords = []
    for index in range(10, plot_length):
        y_coords.append(fun1(index) / float(fun2(index)))
    # plot the list of points
    plt.figure(figsize=[20, 20])
    plt.plot(range(10, plot_length), y_coords, 'o-')
    plt.show()
    # simpleplot.plot_lines("Growth rate comparison", 300, 300, "n", "f(n)/g(n)", [answer])


# create an example plot
make_plot(f, g, 100)
