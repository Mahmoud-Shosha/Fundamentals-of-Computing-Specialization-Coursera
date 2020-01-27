"""
Given the program template below, implement four functions that manipulate a global variable count as follows.
The function reset() sets the value of count to be zero, the function increment() adds one to count,
the function decrement() subtracts one from count, and the function print_count() that prints the value of
count to the console
"""

# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.


def reset():
    """Reset global count to zero."""

    global count
    count = 0

# Increment global count.


def increment():
    """Incrementr global count by one."""

    global count
    count += 1

# Decrement global count.


def decrement():
    """Decrement global count by one. """

    global count
    count -= 1

# Print global count.


def print_count():
    """Print the global count to zero. """

    global count
    print count


###################################################
# Test
# note that the GLOBAL count is defined inside a function
reset()
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
# 1
# 2
# -2