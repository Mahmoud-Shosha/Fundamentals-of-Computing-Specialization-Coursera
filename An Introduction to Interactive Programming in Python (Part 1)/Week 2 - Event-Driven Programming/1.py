"""
Given the program template below, write a Python function print_goodbye() that defines a local variable
message whose value is "Goodbye" and prints the value of this local variable to the console.
Note that the existing global variable message retains its original value "Hello" after the call to
print_goodbye() completes.
"""


# Printing "Goodbye" with a local message variable

###################################################
# Student should enter function on the next lines.

def print_goodbye():
    """Print 'Goodbye' to the console."""

    message = "Goodbye"
    print message

###################################################
# Tests

message = "Hello"
print message
print_goodbye()
print message

message = "Ciao"
print message
print_goodbye()
print message


###################################################
# Output

#Hello
#Goodbye
#Hello
#Ciao
#Goodbye
#Ciao