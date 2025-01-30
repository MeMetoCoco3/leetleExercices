"""
30. Remove Duplicates from Sorted Array

Write a function solve that removes duplicates from a sorted array in-place, and return the new length.
"""


def solve(nums):
    if len(nums) <= 1:
        return 0
    point = 1
    prev = nums[0]
    while point < len(nums):
        if nums[point] == prev:
            del nums[point]
            continue
        prev = nums[point]
        point += 1
    return len(nums)
