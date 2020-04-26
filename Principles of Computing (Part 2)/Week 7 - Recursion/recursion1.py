# Recursion

def sum_up_to(n):
    if n == 1:
        # base case
        return 1
    else:
        # recursive case
        return n + sum_up_to(n - 1)

print(sum_up_to(1))
print(sum_up_to(2))
print(sum_up_to(10))
print(sum_up_to(55))

print(sum(range(56)))
