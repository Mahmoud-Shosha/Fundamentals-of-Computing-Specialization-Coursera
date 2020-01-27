"""
Write event handlers print_hello() and print_goodbye() for the two buttons with labels "Hello" and "Goodbye"
defined in the program template below. Pressing these buttons should print the messages
"Hello" and "Goodbye", respectively, in the console.
"""


# Add "Hello" and "Goodbye" buttons

###################################################
# Student should add code where relevant to the following.

import simplegui


# Handlers for buttons
def print_hello():
    """Print 'Hello' to the console. """

    print 'Hello'



def print_goodbye():
    """Print 'Goodbye' to the console. """

    print 'Goodbye'


# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)
frame.add_button("Hello", print_hello)
frame.add_button("Goodbye", print_goodbye)


# Start the frame animation
frame.start()


###################################################
# Test

print_hello()
print_hello()
print_goodbye()
print_hello()
print_goodbye()

###################################################
# Expected output from test

#Hello
#Hello
#Goodbye
#Hello
#Goodbye


