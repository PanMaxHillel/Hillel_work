lst1 = [1,2,3,4,5]

if len(lst1) == 0:
    result = [[],[]]

elif len(lst1) % 2 == 0:
    lst2 = len(lst1) // 2
    result = [lst1[:lst2],lst1[lst2:]]
else:
    lst3 = len(lst1) // 2 + 1
    result = [lst1[:lst3], lst1[lst3:]]

print(result)