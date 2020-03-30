"""
In the previous problem, we used the method is_exposed to determine whether a tile's number was exposed. Sometimes,
especially during debugging, it is useful to know the value of all of the object data fields. As the first few exercises
showed, trying to print a Tile object in Python yields a message of the form ", end color red">"<__main__.Tile object>"
This message indicates the object is a tile, but doesn't provide any helpful information about the data stored in
the object. In Python, we can define a special string method named __str__ that Python will automatically call when
printing an object or converting the object into a string. Based on the values of the object's fields, the body of the
__str__ method should construct and return a string that indicates the state of the object.

For this problem, implement a string method for the Tile class that return a string of the form
"Number is 3, exposed is True". Remember that you will need to use the str operation to convert the data in
an object into a string.
"""


# Add a __str__ class to the Tile class

#################################################
# Student adds code where appropriate

# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, val, exp):
        self.number = val
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

    # string method for tiles
    def __str__(self):
        return "Number is " + str(self.number) + ", exposed is " + str(self.exposed)


# create a Tile called my_tile with number 3 that is exposed
my_tile = Tile(3, True)

###################################################
# Testing code

print my_tile
my_tile.hide_tile()
print my_tile
my_tile.expose_tile()
print my_tile

####################################################
# Output of testing code

# number is 3, exposed is True
# number is 3, exposed is False
# number is 3, exposed is True
