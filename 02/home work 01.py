#Задание №1 "Квадрат числа"
print("Квадрат числа")

user_input = int (input("Введите число:"))

print(user_input ** 2)

#Задание №2 "Среднее трех чисел"
print("Среднее трех чисел")

user_input_1 = int( input("Введите первую цифру:"))
user_input_2 = int( input("Введите вторую цифру:"))
user_input_3 = int( input("Введите третью цифру:"))

print( (user_input_1 + user_input_2 + user_input_3) // 3 )

#Задание №3 "Перевод минут в часы"
print("Перевод минут в часы")

USER_INPUT_1 = int (input("Введите минуты:"))

print( int(USER_INPUT_1 / 60), end=" часа ")
print( int((USER_INPUT_1 % 60)), end= " минут ")
print("")

#Задание №4 "Калькуляция скидки"
print("Калькуляция скидки")

user_input_1 = int( input("Введите цену:"))
user_input_2 = int( input("Введите размер скидки (без %):"))

print("Сумма со скидкой:", float(user_input_1 - (user_input_1 * user_input_2) / 100))

#Задание №5 "Последняя цифра числа"
print("Последняя цифра числа")

user_cifra_1 = int( input("Введите число:"))

print("Последняя цифра", user_cifra_1 % 10)

#Задание №6 "Периметр прямоугольника"
print("Периметр прямоугольника")

user_dlina_1 = int( input("Введите длину:"))
user_shirina_2 = int( input("Введите ширину:"))

print("Периметр прямоугольника равен:", int( 2* (user_dlina_1 + user_shirina_2)))

#Задание №7 "Вывод чисел в столбец"

print("Вывод чисел в столбец")

user_cifra = int( input("Введите число, которое нужно разбить в стобик: "))

meaning_1 = user_cifra // 1000
meaning_2 = (user_cifra // 100) % 10
meaning_3= (user_cifra // 10) % 10
meaning_4= user_cifra % 10

print("Первая цифра: ", meaning_1)
print("Вторая цифра:",meaning_2)
print("Третья цифра:",meaning_3)
print("Четвертая цифра:",meaning_4)

