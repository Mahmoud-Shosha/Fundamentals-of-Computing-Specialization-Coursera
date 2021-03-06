"""
Complete the program template so that the program displays "Space bar down"
 on the canvas while the space bar is held down and "Space bar up"
 while the space bar is up.
 You will need to add code to both the keydown and keyup handlers.
"""


# Space bar status

import simplegui

message = "Space bar up"

# Handlers for keydown and keyup


def keydown(key):
    global message

    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar down"


def keyup(key):
    global message

    if key == simplegui.KEY_MAP["space"]:
        message = "Space bar up"


# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [25, 112], 42, "Red")


# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
