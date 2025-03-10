"""
    66. Hamming Distance

Write a function solve that computes the Hamming distance between two integers
(number of differing bits).

"""


def bitLen(num):
    length = 0
    while num:
        num >>= 1
        length += 1
    return length


def solve(num1, num2):
    xor = num1 ^ num2
    cnt = 0
    while xor:
        cnt += xor & 1
        xor >>= 1
    return cnt


print(solve(1, 4))
