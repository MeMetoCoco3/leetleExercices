"""
27. Power of Two

Write a function solve that checks if an integer is a power of two.
"""


def solve(n):
    if n == 1:
        return True
    curr = 2
    while curr <= n:
        if curr == n:
            return True
        curr = curr * 2
    return False


def solve2(n):
    return n > 0 and (n & n - 1) == 0


print(solve2(32))
print(solve2(22))
print(solve2(0))
print(solve2(8))
