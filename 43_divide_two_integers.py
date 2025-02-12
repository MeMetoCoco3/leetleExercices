"""
43. Divide Two Integers

Write a function solve that divides two integers without using multiplication, division, and mod operator. Return the quotient as an int after dividing. Assume 32-bit signed integers.

"""


# This looks horrible but im really tired!!
def solve(dividend, divisor):
    if divisor == 0:
        return 0
    divM = dividend < 0
    divsM = divisor < 0
    sign = divM != divsM

    cnt = 0
    base = abs(divisor)
    div = abs(divisor)

    while abs(dividend) >= div:
        cnt += 1
        div += base
    if sign:
        return -cnt
    return cnt


print(solve(7, -3))
