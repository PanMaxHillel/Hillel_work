def common_elements():
    lst_3 = [i for i in range(100) if i % 3 == 0]

    lst_5 = [i for i in range(100) if i % 5 == 0]

    set_3 = set(lst_3)
    set_5 = set(lst_5)

    common = set_3 & set_5

    return common

assert common_elements()

print("OK")
