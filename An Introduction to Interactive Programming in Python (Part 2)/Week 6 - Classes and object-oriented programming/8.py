"""
To complete our implementation of the Tile class, we must determine whether a tile has been clicked. In our week five
implementation of Memory, this computation was done in the draw handler. For our object-oriented version, we will
implement a method is_selected for the Tile class that returns True if a tile contains a specified point. To determine
if a tile has been clicked, the mouse handler will then simply call is_selected using the position of the mouse. Again,
this design moves the determination of whether a point lies on a tile out of the mouse handler into the Tile class,
reducing the complexity of the mouse handler.

For the final problem, your task is to implement the is_selected method. This method take a point pos as a parameter
and return True if the point lies inside the tile. If your implementation of this method is correct, our provided
template will allow you to flip over two cards whose numbers are hidden.
"""

# Add an selection method for Tile class

#################################################
# Student adds code where appropriate

import simplegui

# define globals
TILE_WIDTH = 50
TILE_HEIGHT = 100


# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num, exp, loc):
        self.number = num
        self.exposed = exp
        self.location = loc

    # definition of getter for number
    def get_number(self):
        return self.number

    # check whether tile is exposed
    def is_exposed(self):
        return self.exposed

    # expose the tile
    def expose_tile(self):
        self.exposed = True

    # hide the tile
    def hide_tile(self):
        self.exposed = False

    # string method for tiles
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)

        # draw method for tiles

    def draw_tile(self, canvas):
        loc = self.location
        if self.exposed:
            text_location = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.number), text_location, TILE_WIDTH, "White")
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, loc[1] - TILE_HEIGHT],
                            [loc[0], loc[1] - TILE_HEIGHT])
            canvas.draw_polygon(tile_corners, 1, "Red", "Green")

    # selection method for tiles
    def is_selected(self, pos):
        loc = self.location
        return (pos[0] > loc[0]) and (pos[0] < loc[0] + TILE_WIDTH)


# define event handlers
def mouseclick(pos):
    if tile1.is_selected(pos):
        tile1.hide_tile()
    if tile2.is_selected(pos):
        tile2.expose_tile()


# draw handler
def draw(canvas):
    tile1.draw_tile(canvas)
    tile2.draw_tile(canvas)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

# create two tiles
tile1 = Tile(3, True, [0, TILE_HEIGHT])
tile2 = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])

# get things rolling
frame.start()

###################################################
# Clicking on tile should flip them once
