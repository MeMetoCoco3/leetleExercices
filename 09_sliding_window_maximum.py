"""9. Sliding Window Maximum

Write a function solve that returns the maximum number in each window of size k sliding from left to right in a list. Your function should return a list of ints."""


def solve(nums, k):
    respose = []
    for i in range(len(nums) - k + 1):
        respose.append(max(nums[i : i + k]))

    return respose


print(solve([1, 3, -1, -3, 5, 3, 6, 7], k=3))
