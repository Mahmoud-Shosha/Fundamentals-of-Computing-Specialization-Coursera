"""
In the previous problem, we accessed the one piece of data in the Tile object my_tile via the expression my_tile.number
in the provided testing code. More generally, given an object my_object, Python can access the contents of the field
field_name via the expression my_object.field_name. In the Python community, accessing the content of an object
using its field names is common practice. In this class, we will follow the practice of accessing the contents
of objects using methods known as getters and setters. While not required by Python, this practice encourages the user
of the class to manipulates class objects solely via class methods. The advantage of following this practice is that
the implementer of the class definition (often someone other than the user of the class) may restructure
the organization of the data fields associated with the object while avoiding the need to rewrite code that uses
the class.

For this problem, your task is to implement a method get_number that returns the number associated with a tile.
As usual, the first parameter for this method will be self. Then, call this method on the Tile object my_tile and
assign this value to the variable tile_number. Following the convention of other object-oriented programming languages,
Python's syntax for calling methods on class objects is object_name.method_name(....). In evaluating this call,
object_name is bound to the first parameter self in the definition of method_name. Note that we have already seen this
syntax when calling list methods in Python. For example, the statement my_list.append(5) appends the number 5 to
the end of the list my_list
"""


# Define a getter method for the Tile class

#################################################
# Student adds code where appropriate

# definition of a Tile class
class Tile:

    # definition of intializer
    def __init__(self, num):
        self.number = num

    # definition of getter for number
    def get_number(self):
        return self.number


# create a Tile called my_tile with number 3
my_tile = Tile(3)

# get the number of my_tile and assign to tile_number
# Note "tile_number = my_tile.number" works, but is incorrect
tile_number = my_tile.get_number()

###################################################
# Testing code

print my_tile
print tile_number

####################################################
# Output of testing code

# <__main__.Tile object>
# 3