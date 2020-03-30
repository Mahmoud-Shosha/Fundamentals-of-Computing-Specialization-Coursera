"""
At this point, our Tile class has captured much of the behavior of tiles in Memory. However, the problem of how to draw
tiles still remains. One possibility would be to maintain a list of Tile objects and draw them using a for-loop where
the location of the tile varies as function of the loop's iteration as done in our suggestion implementation of Memory
for week five. This choice, while not terrible, implicitly models the location of a tile by its position in a list.
Instead, we suggest that the we store the location of the tile as part of the data associated with a Tile object.
This choice groups all of the relevant properties of a tile into one object. Following the convention of draw_text,
the tile's location will be specified by the lower left corner of the tile with the width and height of the tile being
specified by the global constants TILE_WIDTH and TILE_HEIGHT, respectively.

With this design, we can implement a draw_tile method for the Tile class that draws the specified tile object at its
corresponding location. This draw_tile method will use SimpleGUI's draw_text or draw_polygon methods to draw the tile.
Since both of these methods require the canvas which itself is passed to the draw handler, we must call the draw_tile
method inside the draw handler and pass the current canvas as a parameter to draw_tile. This design moves most of the
complexity of drawing a tile out of the draw handler into the Tile class and makes the logic of the draw handler
much more transparent.

For this problem, your task is to add the location of the tile to the Tile class and implement a draw_tile method for
the Tile class. The tile should display the tile's number as text at the tile's location if the tile's number is
exposed. Otherwise, it should draw the unexposed tile at the its location as a green polygon. If your implementation of
the draw_tile method is correct, our implementation of the draw handler should display a pair of tiles on the canvas,
one whose number is exposed and one whose number is not.
"""

# Add an draw method for Tile class

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
            text_loc = [loc[0] + 0.2 * TILE_WIDTH, loc[1] - 0.3 * TILE_HEIGHT]
            canvas.draw_text(str(self.get_number()), text_loc, TILE_WIDTH, 'white')
        else:
            tile_corners = (loc, [loc[0] + TILE_WIDTH, loc[1]], [loc[0] + TILE_WIDTH, 0], [loc[0], 0])
            canvas.draw_polygon(tile_corners, 2, 'gray', 'green')


# draw handler
def draw(canvas):
    tile1.draw_tile(canvas)
    tile2.draw_tile(canvas)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 2 * TILE_WIDTH, TILE_HEIGHT)
frame.set_draw_handler(draw)

# create two tiles.make sure to update initializer
tile1 = Tile(3, True, [0, TILE_HEIGHT])
tile2 = Tile(5, False, [TILE_WIDTH, TILE_HEIGHT])

# get things rolling
frame.start()

###################################################
# Resulting frame should display a tile with number 3 (left)
# and a tile with a green back (right)
