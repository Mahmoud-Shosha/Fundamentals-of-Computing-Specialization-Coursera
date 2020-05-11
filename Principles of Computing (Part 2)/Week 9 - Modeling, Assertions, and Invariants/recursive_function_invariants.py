"""
An example on recursive function invariants
"""
import math

def recursive_factorial(num):
    """Calculate factorial recursivly."""
    if num == 0:
        answer = 1
        assert answer == math.factorial(num)
        return answer

    rec_part = recursive_factorial(num - 1)
    answer = num * rec_part
    assert answer == math.factorial(num)
    return answer


print(recursive_factorial(3))
