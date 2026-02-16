def is_palindrome(txt):
    txt = txt.lower()

    clean_txt = ""
    for char in txt:
        if char.isalnum():
            clean_txt += char

    reversed_txt = clean_txt[::-1]

    if clean_txt == reversed_txt:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') is True
assert is_palindrome('0P') is False
assert is_palindrome('a.') is True
assert is_palindrome('aurora') is False

print(is_palindrome('A man, a plan, a canal: Panama'))