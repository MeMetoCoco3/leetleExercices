"""
67. Multiply Strings

Write a function solve that multiplies two non-negative integers represented as strings.
"""


def solve(num1, num2):
    if num1.isnumeric() and num2.isnumeric():
        return int(num1) * int(num2)
    else:
        return ""
