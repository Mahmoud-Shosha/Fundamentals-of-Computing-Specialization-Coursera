"""
At this point, our Tile class is still not so useful. Your next task is to add a field called exposed to
a Tile class definition and implement three methods that manipulate this field. Logically, this field will be True when
the tile's number is exposed to the player and False when the tile's number is hidden from the player. To add this
field to a Tile object, you will need to add another parameter exp to the __init__ method and initialize the exposed
field with this value. Once you have done this, implement three methods described below that manipulate this field.
You will use all of these methods when we re-implement Memory.

* is_exposed which takes a tile and returns the value of the exposed field,
* expose_tile which takes a tile and sets the value of its exposed field to be True, and
* hide_tile which take a tile and set the value of its exposed field to be False.
Note how this design of the Tile class logically binds together the data associated with a tile into a single object.
In our previous implementation of Memory, the data associated with a single tile was stored in two separate lists.
This design required us to keep track of where the data for the same object was in both lists. For Memory, this task
wasn't so hard. However, as the complexity of your programs increase, grouping all of the data corresponding to
a single logical entity together is a powerful way to reduce the complexity of your program
"""


# Add an exposed field to a Tile object with three methods

#################################################
# Student adds code where appropriate

# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num, exp):
        self.number = num
        self.exposed = exp

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


# create a Tile called my_tile with number 3 that is exposed
my_tile = Tile(3, True)

###################################################
# Testing code

print my_tile
print my_tile.is_exposed()
my_tile.hide_tile()
print my_tile.is_exposed()
my_tile.expose_tile()
print my_tile.is_exposed()

####################################################
# Output of testing code

# <__main__.Tile object>
# True
# False
# True
