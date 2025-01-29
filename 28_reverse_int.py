"""
28. Reverse Integer

Write a function solve that reverses the digits of an integer. If the reversed integer overflows, return 0.
"""


def solve(n):
    INT_MAX = 2**32 - 1
    reversed_num = 0
    sign = 1 if n > 0 else -1
    n = abs(n)
    while n > 0:
        next_num = n % 10
        n = n // 10
        reversed_num = reversed_num * 10 + next_num
        if reversed_num > (INT_MAX - next_num) // 10:
            return 0

    return int(reversed_num) * sign


print(solve(-1534))
