"""
60. Kth Largest Element

Write a function solve that finds the kth largest element in an unsorted array.
"""


def solve(nums, k):
    if not nums:
        return 0
    nums = sorted(nums, reverse=True)

    return max(nums[k - 1 :], default=0)


print(solve([3, 2, 1, 5, 6, 4], 2))
