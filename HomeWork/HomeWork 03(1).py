first_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

first_list1 = first_list.count(0)

for a in range(first_list1):
    first_list.remove(0)
    first_list.append(0)

print(first_list)
