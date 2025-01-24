"""
24. Minimum Rotated Sorted Array

Write a function solve that finds the minimum element in a rotated sorted array.
"""


def solve(nums):
    return min(nums)


def solve2(nums):
    if not nums:
        return []
    min = nums[0]
    for i in nums:
        if i < min:
            return i
    return min


# Binary search
def solve3(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


print(solve3([4, 5, 1, 2, 3]))
print(solve3([1]))
