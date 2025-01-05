"""6. Maximum Subarray
15:21

Write a function solve that finds the contiguous subarray with the largest sum in a list."""


def solve(nums):
    max_current = max_global = nums[0]

    for current_num in nums[1:]:
        max_current = max(current_num, max_current + current_num)
        max_global = max(max_global, max_current)

    return max_global


j = solve([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(j)
