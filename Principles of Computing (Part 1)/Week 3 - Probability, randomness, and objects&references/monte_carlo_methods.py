"""
Monte Carlo simulation to compute the expectation that
you will get three-of-a-kind when rolling 5 dice.
"""


import random
import matplotlib.pyplot as plt


def compute_trial():
    """
    Trial: roll five six-sided dice
    """
    return [random.randrange(1, 7) for dummy in range(5)]


def check_event(dice):
    """
    Event: rolled three-of-a-kind
    """
    for die in set(dice):
        if dice.count(die) == 3:
            return True
    return False


def simulation_step():
    """
    One step of the Monte Carlo simulation.
    """
    result = compute_trial()
    event = check_event(result)
    return event


def monte_carlo(ntrials):
    """
    Basic Monte Carlo simulation.
    """
    events = 0
    for dummy in range(ntrials):
        event = simulation_step()
        if event:
            events += 1

    # Return expectation of the event
    return float(events) / float(ntrials)


def run():
    """
    Run Monte Carlo simulations with different numbers
    of trials to estimate the expectation that you will
    get 3-of-a-kind when rolling 5 dice.

    Actual probability of 3-of-a-kind: .1929
    """
    trial_sizes = [10, 100, 1000, 10000, 100000]
    estimates = []
    for ntrials in trial_sizes:
        estimates.append(monte_carlo(ntrials))
    for i in range(5):
        print(trial_sizes[i], ":", estimates[i])

    # plt.figure(figsize=[20, 20])
    plt.bar([1, 2, 3, 4, 5], estimates)
    plt.xticks([1, 2, 3, 4, 5], ['10', '100', '1000', '10000', '100000'])
    plt.show()


run()
