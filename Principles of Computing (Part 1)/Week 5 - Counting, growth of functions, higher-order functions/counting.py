"""
Counting the number of steps during execution
of code fragments
"""

# straight line code: # of step steps bounded by size of code
print("test0")
print("test0")
print("test0")

# conditionals: # of steps is bound by size of code
if True:
    print("test0")
else:
    print("test0")

# loops: # of steps depends on loop parameters
for index in range(10):
    print("test0")


# functions: number of steps depends on input parameters
def test1(input_val):
    """
    Linear function for counting
    """
    n = 0
    for index in range(input_val):
        print("test1")
        n += 1
    print(n)

# test1(10)


def test2(input_val):
    """
    Quadratic function for counting
    """
    n = 0
    for index1 in range(input_val):
        for index2 in range(index1 + 1):
            print("test2")
            n += 1
    print(n)

#test2(5)


def test3(input_val):
    """
    Exponential function for counting
    """
    n = 0
    for index1 in range(input_val):
        for index2 in range(2 ** index1):
            print("test3")
            n += 1
    print(n)

test3(3)
