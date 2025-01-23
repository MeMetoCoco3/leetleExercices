"""
23. Validate Palindromic Number

Write a function solve that checks whether an integer is a palindrome without converting it to a string.
"""


def solve(input):
    number = []

    if not input:
        return True
    elif input < 0:
        return False
    while input > 0:
        new_val = input % 10
        input = input // 10
        number.append(new_val)
    if len(number) % 2 == 0:
        fp = number[: len(number) // 2]
        lp = number[len(number) // 2 :][::-1]

        return fp == lp
    else:
        fp = number[: len(number) // 2]
        lp = number[(len(number) // 2) + 1 :][::-1]

        return fp == lp


print(solve(-121))
