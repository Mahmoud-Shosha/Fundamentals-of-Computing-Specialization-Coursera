"""
A module to learn python modules
"""
# Import the math module (look in the Docs for help)
import math

# Import example module
import examples_module as example

# Constants
print("===Math constants===")

print(math.pi)
print(math.e)

# Functions
print()
print("===Math functions===")

print(math.sqrt(25))
print(math.trunc(14.83483))
print(math.sin(math.pi / 2.0))

# Dir
print()
print("===Dir===")

print(dir(math))
print(dir(example))

print(example.MESSAGE)

print(math.__name__)
print(example.__name__)
