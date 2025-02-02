"""
33. Number of Steps to Reduce to Zero

Write a function solve that returns the number of steps to reduce a non-negative integer to zero. If it's even, divide by 2; if it's odd, subtract 1.
"""


def solve(num):
    c = 0
    while num != 0:
        num = num / 2 if num % 2 == 0 else num - 1
        c += 1
    return c


print(solve(14))
