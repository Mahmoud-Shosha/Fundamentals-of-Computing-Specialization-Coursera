"""
Given the program template below, implement four buttons that manipulate a global variable count as follows.
The function reset() sets the value of count to be zero, the function increment() adds one to count,
the function decrement() subtracts one from count, and the function print_count() prints the value of count
to the console.
"""

# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simplegui

# Define event handlers for four buttons


def reset():
    """Reset the global count to zero. """

    global count
    count = 0


def increment():
    """Increment the global count by one. """

    global count
    count += 1


def decrement():
    """Decrement the global count by one. """

    global count
    count -= 1


def print_count():
    """Print the global count on the console. """

    global count
    print count

# Create frame and assign callbacks to event handlers

frame = simplegui.create_frame('Manipulate global count variable', 400, 400)
frame.add_button('reset', reset, 100)
frame.add_button('Increment', increment, 100)
frame.add_button('Decrement', decrement, 100)
frame.add_button('Print count', print_count, 100)


# Start the frame animation

frame.start()

###################################################
# Test

# Note that the GLOBAL count is defined inside a function
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
# Expected output from test

# 1
# 2
# -2
