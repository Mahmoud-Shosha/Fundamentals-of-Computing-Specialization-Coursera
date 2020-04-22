"""
Higher-order functions
"""

def is_even(value):
    """
    return wheher a value is even
    """
    if value % 2:
        return False
    else:
        return True


data = [1, 3, 6, 9, 10]


even_data = filter(is_even, data)
print(list(even_data))
