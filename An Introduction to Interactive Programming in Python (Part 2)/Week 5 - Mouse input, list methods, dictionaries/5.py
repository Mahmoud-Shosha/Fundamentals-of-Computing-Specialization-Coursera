"""
Load this image of an asteroid, and draw the image centered at the last mouse click.
Prior to any mouse clicks, the image should be drawn in the middle of the canvas. The image size is 95x93 pixels.
"""

# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
IMAGE_WIDTH = 95
IMAGE_HEIGHT = 93
ball = [WIDTH//2, HEIGHT//2]


# load test image
image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")


# mouseclick handler
def click(pos):
    global ball
    ball = pos


# draw handler
def draw(canvas):
    canvas.draw_image(image, [IMAGE_WIDTH//2, IMAGE_HEIGHT//2], [IMAGE_WIDTH, IMAGE_HEIGHT],
                      ball, [IMAGE_WIDTH, IMAGE_HEIGHT])


# create frame and register draw handler
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)


# start frame
frame.start()

