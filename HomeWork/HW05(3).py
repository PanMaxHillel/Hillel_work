import string

us_post = input ("Введите имя поста: ")

clear_post = ""
for ch in us_post:
    if ch not in string.punctuation:
        clear_post += ch

words_01 = clear_post.title()
hashtag1 = "#" + words_01.replace(" ", "")

if len(hashtag1) > 140:
    hashtag1 = hashtag1[:140]

print(hashtag1)