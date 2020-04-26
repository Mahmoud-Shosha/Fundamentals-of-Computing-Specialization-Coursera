"""
Three implementations of binary search
"""

import random


def iter_binary_search(ordered_list, lower, upper, item):
    """
    Iterative version of binary search
    Test whether item is in ordered_list[lower:upper]
    """

    while lower <= upper:
        mid = (lower + upper) // 2
        if ordered_list[mid] == item:
            return True
        else:
            if item < ordered_list[mid]:
                upper = mid - 1
            else:
                lower = mid + 1
    return False


def rec1_binary_search(ordered_list, item):
    """
    Recursively check whether item lies in non-empty ordered_list
    """
    if len(ordered_list) == 0:
        return False
    mid = len(ordered_list) // 2
    if ordered_list[mid] == item:
        return True
    else:
        if item < ordered_list[mid]:
            return rec1_binary_search(ordered_list[: mid-1], item)
        else:
            return rec1_binary_search(ordered_list[mid+1:], item)



def rec2_binary_search(ordered_list, lower, upper, item):
    """
    Recursive version of binary search with bounds
    Test whether item is in ordered_list[lower:upper]
    """
    if lower > upper:
        return False
    mid = (lower + upper) // 2
    if ordered_list[mid] == item:
        return True
    else:
        if item < ordered_list[mid]:
            return rec2_binary_search(ordered_list, lower, mid-1, item)
        else:
            return rec2_binary_search(ordered_list, mid+1, upper, item)


# Test on sorted list of numbers
sorted_list = [5, 6, 12, 17, 30, 64, 64, 67, 75, 79, 88, 91, 101, 106, 134, 135, 158, 168, 178, 199, 200, 202, 212, 230,
               231, 234, 244, 253, 273, 291, 326, 327, 344, 345, 348, 361, 378, 385, 394, 400, 406, 416, 419, 439, 443,
               450, 455, 477, 482, 491, 499, 511, 512, 516, 522, 542, 544, 583, 586, 590, 592, 598, 612, 624, 634, 634,
               658, 667, 672, 689, 724, 737, 750, 765, 793, 803, 812, 814, 835, 836, 838, 849, 851, 861, 862, 867, 875,
               876, 882, 894, 904, 906, 908, 942, 960, 965, 984, 986, 990, 993]

print("Order list is", sorted_list)
print()
print("Searched for 135", "Computed:", iter_binary_search(sorted_list, 0, len(sorted_list)-1, 135), "Expected: True")
print("Searched for 125", "Comptued:", iter_binary_search(sorted_list, 0, len(sorted_list)-1, 125), "Expected: False")
print()
print("Searched for 135", "Computed:", rec1_binary_search(sorted_list, 135), "Expected: True")
print("Searched for 125", "Comptued:", rec1_binary_search(sorted_list, 125), "Expected: False")
print()
print("Searched for 135", "Computed:", rec2_binary_search(sorted_list, 0, len(sorted_list)-1, 135), "Expected: True")
print("Searched for 125", "Comptued:", rec2_binary_search(sorted_list, 0, len(sorted_list)-1, 125), "Expected: False")

def test(func):
    """
    Return True if function works correctly
    """
    not_exist = [4, 7, 994, 992, 513, 0, -88, 99999]
    result1 = True
    result2 = False
    for key in sorted_list:
        result1 = result1 and func(sorted_list, 0, len(sorted_list)-1, key)
    for key in not_exist:
        result2 = result2 or func(sorted_list, 0, len(sorted_list)-1, key)
    return result1 and not result2

print()
print()
print("__Testing__")
print(test(iter_binary_search))
print(test(rec2_binary_search))