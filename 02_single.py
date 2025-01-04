"""
Write a function solve that finds the number that appears only once in a list where all other numbers appear twice.

Example:
Input: [4,1,2,1,2]
Output: 4
"""


def solve(nums):
    for i, v in enumerate(nums):
        rest = nums[:i] + nums[i + 1 :]
        if v in rest:
            continue
        return v
