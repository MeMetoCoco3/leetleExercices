"""
55. Jump Game

Write a function solve that determines if you can reach the last index in an
array. Each element represents the maximum jump length at that position.
"""


def solve(nums):
    if len(nums) < 2:
        return True
    current_position = 1
    step = nums[current_position]
    for _ in nums[1:]:
        if len(nums) <= current_position:
            return False
        if len(nums) == current_position + 1:
            return True

        current_position += step
        step = nums[current_position]
    return False


print(solve([3, 2, 1, 0, 4]))
