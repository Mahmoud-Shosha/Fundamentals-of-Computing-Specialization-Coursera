"""
Write a function add_vector(v, w) that takes two 2D vectors v and w
(represented as lists) and returns a new 2D vector (represented as a list)
that is the sum of the two vectors
 Remember that vector addition is performed independently on
 each corresponding element of the lists.
 Hint: returning v + w does not work.
"""


# Vector addition function

###################################################
# Student should enter code below

def add_vector(v, w):
    """Returns a sum of two 2D vectors."""
    new_list = [0, 0]
    new_list[0] = v[0] + w[0]
    new_list[1] = v[1] + w[1]
    return new_list

###################################################
# Test


print add_vector([4, 3], [0, 0])
print add_vector([1, 2], [3, 4])
print add_vector([2, 3], [-6, -3])


###################################################
# Output

# 4, 3]
# [4, 6]
# [-4, 0]
