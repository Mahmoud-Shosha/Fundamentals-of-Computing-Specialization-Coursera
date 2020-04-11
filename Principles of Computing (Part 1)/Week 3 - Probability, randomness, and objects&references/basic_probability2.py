"""
Test whether random.randrage simulates a fair die
"""

import matplotlib.pyplot as plt

from basic_probability1 import roll_die


TRIAL_STRIDE = 10


def plot_fairness(side, num_sides, max_trials):
    """
    Plot the mathematical probability for an outcome vs.
    computed estimate
    """
    plot_x = []
    plot_y = []
    for num_trials in range(TRIAL_STRIDE, max_trials, TRIAL_STRIDE):
        side_count = 0
        for _ in range(num_trials):
            if roll_die(num_sides) == side:
                side_count += 1
        mathematical = 1.0 / num_sides
        computed = float(side_count) / num_trials
        plot_x.append(num_trials)
        plot_y.append(mathematical - computed)
    plt.plot(plot_x, plot_y)
    plt.show()


# check the fairness of the die
plot_fairness(1, 6, 1000)
