"""
Construct list of binary numbers of given length
Creates natural binary numbers and Gray codes
"""


def make_binary(length):
    """
    Function that generates ordered list of binary numbers in
    ascending order
    """
    if length == 0:
        return [""]

    all_but_first = make_binary(length - 1)

    answer = []
    for bits in all_but_first:
        answer.append("0" + bits)
    for bits in all_but_first:
        answer.append("1" + bits)
    return answer

def binary_length(length):
    """
    Recurrence for the number of binary numbers of a given length
    """
    if length == 0:
        return 1
    else:
        return 2 * binary_length(length-1)


def run_examples():
    """
    print out example of Gray code representations
    """
    for length in range(5):
        print("Binary numbers of length", length)
        print(make_binary(length))
        print("counts: ", binary_length(length))
        print()




run_examples()
