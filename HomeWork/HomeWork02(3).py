lst1 = [1,2,3,4]

if len(lst1) <= 1:
    print(lst1)
else:
    lst2 = lst1.pop()
    lst1.insert(0, lst2)

print(lst1)