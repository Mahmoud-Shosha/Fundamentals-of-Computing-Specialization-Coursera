"""
Study Permutations and Combinations
where Repetition of outcomes is NOT allowed
"""

import math

# Lottery, 59 balls, draw 6, order is important

print(math.factorial(59) / math.factorial(59-6))

num_perms = 1
for index in range(59, 59-6, -1):
    num_perms *= index

print(num_perms)