"""
Counting the number of iterations in various mystery functions
"""

import matplotlib.pyplot as plt
import math

# Plot options
STANDARD = True
LOGLOG = False

# global counter that records the number of iterations for inner loops
counter = 0

###############################################
# three mystery functions
def mystery1(input_val):
    """
    Function whose loops update global counter
    5x ==> Linear
    """
    global counter
    for index in range(input_val):
        for dummy_index in range(5):
            counter += 1

def mystery2(input_val):
    """
    Function whose loops update global counter
    Quadratic
    """
    global counter
    for index in range(input_val):
        for dummy_index in range(index // 2, index):
            counter += 1

def mystery3(input_val):
    """
    Function whose loops update global counter
    A very slowly growing exponential function
    """
    global counter
    for index in range(input_val):
        for dummy_index in range(int(1.1 ** index)):
            counter += 1

def build_plot(plot_size, plot_function, plot_type = STANDARD):
    """
    Build plot of the number of increments in mystery function
    """
    global counter
    plot_x = []
    plot_y = []
    for input_val in range(2, plot_size):
        counter = 0
        plot_function(input_val)
        if plot_type == STANDARD:
            plot_x.append(input_val)
            plot_y.append(counter)
        else:
            plot_x.append(math.log(input_val))
            plot_y.append(math.log(counter))
    return (plot_x, plot_y)



###############################################
# plottting code
plot_type = LOGLOG
plot_size = 40

# Pass name of mystery function in as a parameter
plot1 = build_plot(plot_size, mystery1, plot_type)
plot2 = build_plot(plot_size, mystery2, plot_type)
plot3 = build_plot(plot_size, mystery3, plot_type)

plt.figure(figsize=[20, 20])
plt.plot(plot1[0], plot1[1], 'o-')
plt.plot(plot2[0], plot2[1], 'o-')
plt.plot(plot3[0], plot3[1], 'o-')

plt.legend(['mystery1', 'mystery2', 'mystery3'])
plt.show()
