inpt_user = int(input("Введите число: "))

us_dni, remainder = divmod(inpt_user, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

if 11 <= us_dni % 100 <= 14:
    day_word = "днів"
elif us_dni % 10 == 1:
    day_word = "день"
elif 2 <= us_dni % 10 <= 4:
    day_word = "дні"
else:
    day_word = "днів"

hours_str = str(hours).zfill(2)
minutes_str = str(minutes).zfill(2)
seconds_str = str(seconds).zfill(2)

user_prnt = f"{us_dni} {day_word} {hours_str}:{minutes_str}:{seconds_str}"

print(user_prnt)