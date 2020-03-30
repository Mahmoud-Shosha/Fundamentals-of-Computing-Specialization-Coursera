"""
Modify the initial template to draw the firing line used to aim the bubbles. The lower endpint of firing line
(the position where bubbles spawn) should remain unchanged. The position of the upper endpoint should move along
a circle centered at the lower endpoint and with an angle whose value is contained in the global variable
firing_angle. Use the provided function angle_to_vector to turn the value firing_angle into the position for
the upper endpoint of the firing line. Note that angle_to_vector always returns a vector of length one.
Experiment with various value for firing_angle.
"""


# Basic infrastructure for Bubble Shooter

import simplegui
import random
import math

# Global constants
WIDTH = 800
HEIGHT = 600
FIRING_POSITION = [WIDTH // 2, HEIGHT]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.02
BUBBLE_RADIUS = 20
COLOR_LIST = ["Red", "Green", "Blue", "White"]

# global variables
firing_angle = math.pi / 2
firing_angle_vel = 0
bubble_stuck = True


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# class defintion for Bubbles
class Bubble:

    def __init__(self):
        pass

    def update(self):
        pass

    def fire_bubble(self, vel):
        pass

    def is_stuck(self):
        pass

    def collide(self, bubble):
        pass

    def draw(self, canvas):
        pass


# define keyhandlers to control firing_angle
def keydown(key):
    global a_bubble, firing_angle_vel, bubble_stuck
    pass


def keyup(key):
    global firing_angle_vel
    pass


# define draw handler
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck

    # update firing angle

    # draw firing line
    firing_unit_vector = angle_to_vector(firing_angle)
    firing_vector = (firing_unit_vector[0] * FIRING_LINE_LENGTH, firing_unit_vector[1] * FIRING_LINE_LENGTH)
    firing_endpoint = (firing_vector[0] + FIRING_POSITION[0], FIRING_POSITION[1] - firing_vector[1])
    canvas.draw_line(FIRING_POSITION, firing_endpoint, 4, 'white')


    # update a_bubble and check for sticking

    # draw a bubble and stuck bubbles


# create frame and register handlers
frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# create initial buble and start frame
frame.start()