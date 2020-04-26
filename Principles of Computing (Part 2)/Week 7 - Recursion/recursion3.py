"""
Write a function is_member(my_list, elem) that returns True if elem is a member of my_list and False otherwise.
For example, is_member(['c', 'a', 't'], 'a') should return True.
Do not use any of Python's built-in list methods or an operator like in.
"""

def is_member(my_list, elem):
    """
    Take list my_list and determines whether elem is in my_list
    Returns True or False
    """
    if len(my_list) == 0:
        return False
    else:
        if my_list[0] == elem:
            return True
        else:
            return is_member(my_list[1:], elem)


def test_is_member():
    """
    Some test cases for is_member
    """
    print("Computed:", is_member([], 1), "Expected: False")
    print("Computed:", is_member([1], 1), "Expected: True")
    print("Computed:", is_member(['c', 'a', 't'], 't'), "Expected: True")
    print("Computed:", is_member(['c', 'a', 't'], 'd'), "Expected: False")


test_is_member()
