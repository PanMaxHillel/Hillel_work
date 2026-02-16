def correct_sentence(sentence: str) -> str:
    sentence = sentence.capitalize()
    if not sentence.endswith('.'):
        sentence = sentence + '.'

    return sentence

assert correct_sentence("greetings, friends")
assert correct_sentence("hello")
assert correct_sentence("Greetings. Friends")
assert correct_sentence("Greetings, friends.")
assert correct_sentence("greetings, friends.")

print("OK")