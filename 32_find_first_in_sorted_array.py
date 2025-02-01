"""
32. Find First and Last Position of Element in Sorted Array

Write a function solve that finds the starting and ending position of a target value in a sorted array. If the target is not found, return [-1,-1]. Ideally, your solution should run in O(logn) time.
"""


def solve(nums, target):
    left = 0
    right = len(nums) - 1

    if not nums:
        return [-1, -1]

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            if mid + 1 == len(nums):
                if nums[mid - 1] == target:
                    if mid - 1 == -1:
                        return [0, 0]
                    return [mid - 1, mid]
                else:
                    return sorted([mid, mid])
            else:
                other = mid + 1 if nums[mid + 1] == target else mid - 1
                if nums[other] == target:
                    return sorted([mid, other])
                else:
                    return sorted([mid, mid])
        if target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return [-1, -1]


# print(solve([5, 7, 7, 8, 8, 10], 8))
# print(solve([5, 7, 7, 8, 8, 10], 6))
print(solve([1], 1))
# print(solve([], 1))
# print(solve([1, 2, 3, 4, 5], 3))
# print(solve([1, 2, 3, 4, 5], 6))
