import random

frst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num1 = [random.randint(1, 100) for i in range(random.randint(3, 10))]

print(num1)

frst2 = [num1[0], num1[2], num1[-2]]

print(frst2)