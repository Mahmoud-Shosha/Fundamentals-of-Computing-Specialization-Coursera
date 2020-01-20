"""
Powerball is lottery game in which 6 numbers are drawn at random. Players can purchase a lottery ticket with
a specific number combination and, if the number on the ticket matches the numbers generated in a random drawing,
the player wins a massive jackpot.
Write a Python function powerball that takes no arguments and prints the message
"Today's numbers are %, %, %, %, and %. The Powerball number is %.".
the first five numbers should be random integers in the range [1,60), i.e., at least 1, but less than 60.
In reality, these five numbers must all be distinct, but for this problem, we will allow duplicates.
The Powerball number is a random integer in the range [1,36), i.e., at least 1 but less than 36.
Use the random module and the function random.randrange to generate the appropriate random numbers
Note that this function should print the desired message, rather than returning it as a string.
"""

# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.

import random


def powerball():
    """Prints Powerball lottery numbers."""

    # Generating five numbers in the range [1, 60)
    number1 = random.randrange(1, 60)
    number2 = random.randrange(1, 60)
    number3 = random.randrange(1, 60)
    number4 = random.randrange(1, 60)
    number5 = random.randrange(1, 60)

    # Generating the powerball number in the range [1,36)
    powerbasll_number = random.randrange(1, 36)

    # Printing the lottery numbers
    print ("Today's numbers are " + str(number1) + ", " + str(number2) + ", " +
           str(number3) + ", " + str(number4) + ", and " + str(number5) +
           ". The Powerball number is " + str(powerbasll_number) + ".")


###################################################
# Tests
# Student should not change this code.

powerball()
powerball()
powerball()
