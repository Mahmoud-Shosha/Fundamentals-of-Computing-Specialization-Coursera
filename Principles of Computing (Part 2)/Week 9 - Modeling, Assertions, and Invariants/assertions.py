"""
Assertions in python.
"""


# def avg(marks):
#     """Compute the average of numbers in a list."""
#     assert len(marks) != 0, "List is empty." # The message is optional
#     return sum(marks)/len(marks)
#
# MARK2 = [55, 88, 78, 90, 79]
# print("Average of mark2:", avg(MARK2))
#
# MARK1 = []
# print("Average of mark1:", avg(MARK1))


def avg2(marks):
    """Compute the average of numbers in a list."""
    if not len(marks) != 0:
        raise AssertionError("List is empty.") # The message is optional
    return sum(marks)/len(marks)

MARK2 = [55, 88, 78, 90, 79]
print("Average of mark2:", avg2(MARK2))

MARK1 = []
print("Average of mark1:", avg2(MARK1))
