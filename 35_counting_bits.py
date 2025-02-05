"""
35. Counting Bits

Write a function solve that returns an array of the number of 1-bits (Hamming weight) for each number from 0 to n.
"""


# Had to check >:(
def solve(n):
    result = [0] * (n + 1)
    breakpoint()
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)

    return result


print(solve(4))
