"""
    48. Add Binary

Write a function solve that adds two binary strings and returns their sum as a binary string.
"""


def solve(a, b):
    x = btod(a)
    y = btod(b)
    return dtob(x + y)


def btod(n: str) -> int:
    if len(n) == 0:
        return 0
    cnt = 0
    for pot, i in enumerate(n[::-1]):
        cnt += pow(2, int(pot)) * int(i)
    return cnt


def dtob(n: int) -> str:
    if n == 0:
        return "0"
    cnt = ""
    while n > 0:
        quo = n // 2
        rem = n % 2
        cnt += str(rem)
        n = quo

    return cnt[::-1]


print(btod("010110101"))
print(dtob(181))
