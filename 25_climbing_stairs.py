"""
25. Climbing Stairs

Write a function solve that calculates how many distinct ways you can climb a staircase of n steps, taking 1 or 2 steps at a time.
"""


def solve(n):
    if n <= 2:
        return n

    a, b = 1, 2

    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


print(solve(6))
