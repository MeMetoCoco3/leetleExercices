"""
14. Reverse Words

Write a function solve that reverses the words in a string. Words are separated by spaces.
"""


def solve(split_word):
    split_word = split_word.split(" ")
    breakpoint()
    start = 0
    end = len(split_word) - 1
    while start < end:
        split_word[start], split_word[end] = split_word[end], split_word[start]
        end -= 1
        start += 1
    return " ".join(split_word)


# Didnt read the problem D:
def reverse(w):
    split_word = list(w)

    start = 0
    end = len(split_word) - 1
    while start < end:
        split_word[start], split_word[end] = split_word[end], split_word[start]
        end -= 1
        start += 1
    return "".join(split_word)


print(solve("Hola me llamo vidal que tal"))
