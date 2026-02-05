import string
import keyword

name = input("Enter: ")

result = True

if not name:
    result = False

elif name.count("_") > 1:
    result = False

elif name[0].isdigit():
    result = False

elif name in keyword.kwlist:
    result = False

else:
    for name2 in name:
        if name2.isupper():
            result = False
            break
        if name2 in string.punctuation and name2 != "_":
            result = False
            break
        if name2 == " ":
            result = False
            break

print(result)