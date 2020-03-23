"""
Write a function string_list_join(string_list) that takes a list of strings as input and returns a single string
that is the concatenation of the strings in the list.
We recommend using a for loop to implement this function.
"""


# String list joining problem

###################################################
# Student should enter code below

def string_list_join(string_list):
    new_string = ''
    for string in string_list:
        new_string += string
    return new_string


###################################################
# Test data

print string_list_join([])
print string_list_join(["pig", "dog"])
print string_list_join(["spam", " and ", "eggs"])
print string_list_join(["a", "b", "c", "d"])


###################################################
# Output

#
#pigdog
#spam and eggs
#abcd