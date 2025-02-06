"""
37. Count Prime Numbers

Write a function solve that counts the number of prime numbers less than n. a
"""


def solve(n):
    res = []
    if n <= 1:
        return len(res)
    for i in range(2, n):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False

        if isPrime:
            res.append(i)
    return len(res)


print(solve(30))
