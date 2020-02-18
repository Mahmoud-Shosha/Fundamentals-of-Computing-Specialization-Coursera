"""
Given the list a in the template, make a new reference b to a.
Update the first entry in b to be zero. What happened to
the first entry in a? Explain your answer (in a comment).
"""


# List reference problem

###################################################
# Student should enter code below

a = [5, 3, 1, -1, -3, 5]
b = a
b[0] = 0
print a


###################################################
# Explanation
# The assignment b = a created a second reference to a.
# Setting b[0] = 0 also mutated the list that both
# a and b reference.  As a result, a[0] == 0.
