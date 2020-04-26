"""
Write a function list_reverse(my_list) that takes a list and returns a new list whose elements appear in reversed order.
For example, list_reverse([2, 3, 1]) should return [1, 3, 2].
Do not use the reverse() method for lists.
"""


def list_reverse(my_list):
    """
    Takes a list my_list and returns new list
    whose elements are in reverse order
    Returns a list
    """
    if len(my_list) == 0:
        return []
    else:
        new_list = [my_list[-1]] + list_reverse(my_list[:-1])
        return new_list




def test_list_reverse():
    """
    Some test cases for list_reverse
    """
    print("Computed:", list_reverse([]), "Expected: []")
    print("Computed:", list_reverse([1]), "Expected: [1]")
    print("Computed:", list_reverse([1, 2, 3]), "Expected: [3, 2, 1]")
    print("Computed:", list_reverse([2, 3, 1]), "Expected: [1, 3, 2]")


test_list_reverse()