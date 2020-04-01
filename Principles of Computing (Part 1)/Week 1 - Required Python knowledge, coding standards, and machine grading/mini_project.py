"""
Merge function for 2048 game.
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """

    new_list = trail_zeros(line)
    new_list = adjacent_merge(new_list)
    new_list = trail_zeros(new_list)

    return new_list


def trail_zeros(line):
    """
    Put non-zero values at the beginning of the list,
    and zeros at the end of the list
    """

    # Create an empty list with the same size as line list
    new_line = [0 for dummy_num in line]

    # new_line_index points to the next index to be filled in the
    # new_line list
    new_line_index = 0

    for num in line:
        if num != 0:
            new_line[new_line_index] = num
            new_line_index += 1

    return new_line


def adjacent_merge(line):
    """
    Merge two equal adjacent numbers in a list,
    the first one becomes the double and the second become zero
    """

    index = 1
    new_line = list(line)
    while index < len(line):
        if new_line[index-1] == new_line[index]:
            new_line[index-1] = new_line[index-1] * 2
            new_line[index] = 0
            index += 2
        else:
            index += 1

    return new_line
