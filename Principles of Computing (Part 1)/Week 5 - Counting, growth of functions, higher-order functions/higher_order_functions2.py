"""
Higher-order functions
"""

def double(value):
    """
    return the double of value
    """
    return 2 * value


data = [1, 3, 6, 9, 10]

# Using list comprehensive
new_data = [double(item) for item in data]
print(new_data)

# Using higher order functions
new_data1 = map(double, data)
print(new_data1)
print(list(new_data1))
new_data1 = map(double, data)
print(set(new_data1))
new_data1 = map(double, data)
print(tuple(new_data1))
