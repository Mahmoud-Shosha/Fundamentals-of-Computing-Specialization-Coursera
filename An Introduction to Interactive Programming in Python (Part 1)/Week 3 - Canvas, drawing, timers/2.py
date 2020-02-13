"""
Write a function format_time that takes an integer number of seconds
in range(0, 3600) and converts it into string that states
the number of minutes and seconds. Remember to use the operations // and %
(Note that this example requires no interactive code.)
"""


# Define a function that returns formatted minutes and seconds

###################################################
# Time formatting function
# Student should enter function on the next lines.

def format_time(seconds):
    """State the number of minutes and seconds in the given seconds"""
    minutes = seconds // 60
    seconds = seconds % 60
    return str(minutes) + " minutes and " + str(seconds) + " seconds"

###################################################
# Tests


print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
# 0 minutes and 23 seconds
# 20 minutes and 37 seconds
# 0 minutes and 0 seconds
# 31 minutes and 0 seconds
