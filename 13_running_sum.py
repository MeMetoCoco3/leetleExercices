"""
13. Running Sum
Write a function solve that returns the running sum of a list. The running sum is the sum of all elements up to each index
"""


def solve(nums):
    return [x + sum(nums[:i]) for i, x in enumerate(nums)]


def solve2(nums):
    from itertools import accumulate

    return list(accumulate(nums))


print(solve([1, 2, 3, 4]))
print(solve2([1, 2, 3, 4]))
