"""8. Two Sum

Write a function solve that finds two numbers in a list that add up to a target value. Return a list with their indices in order. If the target cannot be made, return an empty list."""


def solve(nums, target):
    a = i = 0
    while a < len(nums):
        if nums[a] + nums[i] == target and a != i:
            return [a, i]
        if i == len(nums) - 1:
            a += 1
            i = 0
        i += 1
    return []


print(solve([2, 7, 11, 15], 9))
print(solve([3, 2, 4], 6))
