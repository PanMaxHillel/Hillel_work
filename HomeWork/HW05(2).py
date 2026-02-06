print("Калькулятор")
while True:
    user_input1= int(input("Ведите первое число:"))
    user_input2 = input("Значение (+,-,/,*):")
    user_input3 = int(input("Ведите второе число:"))

    if user_input2 == "+":
        print(user_input1 + user_input3)

    elif user_input2 == "-":
        print(user_input1 - user_input3)

    elif user_input2 == "*":
        print(user_input1 * user_input3)

    elif user_input2 == "/":
        if user_input3 != 0:
            print(user_input1 / user_input3)
        else:
            print("Ошибка")

    else:
        print("Нет данных")

    user_input4 = input("Продолжим: ").lower()

    if user_input4 == "y" or user_input4 == "yes":
        continue
    else:
        print("Остоновка")
        break