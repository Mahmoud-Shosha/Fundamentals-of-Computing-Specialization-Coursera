"""
Challenge: Write a program that draws a polyline (an open polygon) based on a sequence of mouse clicks.
The first click should create a point. Subsequent clicks should add a new segment to the polyline.
You should include a 'Clear' button that deletes the polyline and restarts the drawing process.
"""

# Polyline drawing problem

###################################################
# Student should enter code below

import simplegui
import math

polyline = []
LINE_WIDTH = 4
LINE_COLOR = "red"


# define mouseclick handler
def click(pos):
    polyline.append(pos)


# button to clear canvas
def clear():
    global polyline
    polyline = []


# define draw
def draw(canvas):
    if len(polyline) > 0:
        canvas.draw_circle(polyline[0], LINE_WIDTH // 2, 0.000001, LINE_COLOR, LINE_COLOR)
        canvas.draw_polyline(polyline, LINE_WIDTH, LINE_COLOR)



# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()

