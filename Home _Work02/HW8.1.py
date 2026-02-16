def add_one(some_list):
    nom_str = "".join(str(x) for x in some_list)

    number = int(nom_str)
    number += 1

    result = [int(x) for x in str(number)]

    return result

assert add_one([1, 2, 3, 4])
assert add_one([9, 9, 9])
assert add_one([0])
assert add_one([9])

print("OK")