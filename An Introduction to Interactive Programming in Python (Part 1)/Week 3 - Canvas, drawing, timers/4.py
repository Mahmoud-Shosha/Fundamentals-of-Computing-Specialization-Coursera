"""
Given the solution from the following problem,
we again want a counter printed to the console.
Add three buttons that start, stop and reset the counter, respectively.
"""


# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui

counter = 0


# Timer handler
def tick():
    global counter
    print counter
    counter += 1


# Start event handler
def start_handler():
    timer.start()


# Stop event handler
def stop_handler():
    timer.stop()


# Reset event handler
def reset_handler():
    global counter
    counter = 0

# Event handlers for buttons


# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)
frame.add_button("Start", start_handler, 80)
frame.add_button("Stop", stop_handler, 80)
frame.add_button("Reset", reset_handler, 80)
