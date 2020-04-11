"""
Conducting multiple trials using random.randrange()
"""


import random


def roll_die(num_sides):
    """
    Simulate a trail corresponding to the roll of die
    with specified number of sides
    """
    result = random.randrange(0, num_sides) + 1
    return result


def roll_test(num_sides, num_rolls):
    """
    Roll a die with num_sides num_rolls number of times
    """
    print("Roll " + str(num_sides) + "-sided die " + str(num_rolls) + " times")
    for _ in range(num_rolls):
        roll = roll_die(num_sides)
        print("Roll was", roll)

roll_test(6, 10)
