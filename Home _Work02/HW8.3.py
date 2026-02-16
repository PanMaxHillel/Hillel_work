def find_unique_value(list):
    for number in list:
        if list.count(number) == 1:
            return number

assert find_unique_value([1, 2, 1, 1])
assert find_unique_value([2, 3, 3, 3, 5, 5])
assert find_unique_value([5, 5, 5, 2, 2, 0.5])

print("OK")