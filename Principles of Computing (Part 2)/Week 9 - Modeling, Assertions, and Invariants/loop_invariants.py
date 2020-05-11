"""
An example on loop invariants
"""
import math

def iterative_factorial(num):
    """Calculate factorial iterativly."""
    answer = 1
    index = 0
    assert answer == math.factorial(index)
    while index < num:
        index += 1
        answer *= index
        assert answer == math.factorial(index)
    return answer


print(iterative_factorial(3))
