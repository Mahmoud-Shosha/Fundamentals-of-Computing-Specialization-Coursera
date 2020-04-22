"""
Higher-order functions
"""

def double(value):
    """
    return the double of value
    """
    return 2 * value


def square(value):
    """
    return the square of value
    """
    return value ** 2


def twice(func, value):
    """
    Call func twice, passing it value as parameter
    """
    return func(func(value))


print(twice(double, 3))
print(twice(square, 3))
