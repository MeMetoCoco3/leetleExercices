"""
21. Factorial

Write a function solve that returns the factorial of a given integer n. Return 1 if n is 0.
"""


def solve(n):
    if n <= 1:
        return 1
    return n * solve(n - 1)


print(solve(7))
