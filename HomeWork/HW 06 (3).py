user_num = int(input("Введите число: "))

numb_1 = abs(user_num)

while numb_1 > 9:
    product = 1
    for digit in str(numb_1):
        product *= int(digit)
    numb_1 = product

print("Результат:", numb_1)