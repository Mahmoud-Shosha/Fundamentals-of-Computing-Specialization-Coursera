"""
Given the program template below, modify the program to create a CodeSkulptor frame that
opens a 200x100 pixel frame with the title "My second frame". Remember to use the Docs to determine
the correct syntax for the necessary SimpleGUI calls.
"""


# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

import simplegui

message = "My second frame!"

# Handler for mouse click
def click():
    print message

# create the frame
frame = simplegui.create_frame(message, 200, 100)

# Assign callbacks to event handlers
frame.add_button("Click me", click)

# Start the frame animation
frame.start()

