"""
Write a function number_of_threes(num) that returns the number of times the digit 3 appears in
the decimal representation of the non-negative integer num.
For example number_of_threes(34534) should return 2.
"""

def number_of_threes(num):
    """
    Takes a non-negative integer num and compute the
    number of threes in its decimal form
    Returns an integer
    """
    if num == 0:
        return 0
    if num % 10 == 3:
        return 1 + number_of_threes(num//10)
    else:
        return number_of_threes(num//10)


def test_number_of_threes():
    """
    Some test cases for number_of_threes
    """
    print("Computed:", number_of_threes(0), "Expected: 0")
    print("Computed:", number_of_threes(5), "Expected: 0")
    print("Computed:", number_of_threes(3), "Expected: 1")
    print("Computed:", number_of_threes(33), "Expected: 2")
    print("Computed:", number_of_threes(34534), "Expected: 2")


test_number_of_threes()
