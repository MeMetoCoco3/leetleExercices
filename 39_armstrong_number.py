"""
39. Armstrong Number

Write a function solve that checks if an integer is an Armstrong number (a.k.a Narcissistic number).
"""


def solve(num):
    curr = num
    count = 0
    while curr > 0:
        count += pow(curr % 10, len(str(num)))
        curr = curr // 10

    return count == num


print(solve(152))
