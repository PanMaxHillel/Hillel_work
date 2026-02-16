def second_index (text, some_str):
    first = text.find(some_str)

    if first == -1:
        return None

    second = text.find(some_str, first + 1)

    if second == -1:
        return None

    return second

assert second_index("sims", "s")
assert second_index("find the river", "e")
assert second_index("hi", "h") is None
assert second_index("Hello, hello", "lo")

print("OK")