"""
Example of creating a plot using simpleplot

Input is a list of point lists (one per function)
Each point list is a list of points of the form
[(x0, y0), (x1, y1, ..., (xn, yn)]
"""

import matplotlib.pyplot as plt


# create three sample functions

def double(num):
    """
    Example of linear function
    """
    return 2 * num


def square(num):
    """
    Example of quadratic function
    """
    return num ** 2


def exp(num):
    """
    Example of exponential function
    """
    return 2 ** num


def create_plots(begin, end, stride):
    """
    Plot the function double, square, and exp
    from beginning to end using the provided stride

    The x-coordinates of the plotted points start
    at begin, terminate at end and are spaced by
    distance stride
    """

    # generate x coordinates for plot points
    x_coords = []
    current_x = begin
    while current_x < end:
        x_coords.append(current_x)
        current_x += stride

    # compute list of (x, y) coordinates for each function
    double_plot = [double(x_val) for x_val in x_coords]
    square_plot = [square(x_val) for x_val in x_coords]
    exp_plot = [exp(x_val) for x_val in x_coords]

    # plot the list of points
    plt.figure(figsize=[20, 20])
    plt.plot(x_coords, double_plot, 'o-')
    plt.plot(x_coords, square_plot, 'o-')
    plt.plot(x_coords, exp_plot, 'o-')
    plt.legend(['double', 'square', 'exp'])

    plt.show()

create_plots(0, 10, .5)
