"""59. Counting Inversions

Write a function solve that counts the number of inversions in an array.
An inversion is a pair of elements that are out of order.
"""


def solve(nums):
    cnt = 0
    for idx, i in enumerate(nums):
        for j in nums[idx:]:
            if i > j:
                cnt += 1

    return cnt
