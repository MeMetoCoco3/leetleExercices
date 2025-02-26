"""
56. Rotate Array (Cyclic)

Write a function solve that rotates an array to the right by k steps. Ideally,
you should be able to rotate the array in-place, but be sure to still return
your solution.
"""


def solve(nums, k):
    new_array = [0 for _ in nums]
    for idx, i in enumerate(nums):
        pos = (idx + k) % len(nums)
        new_array[pos] = i
    return new_array


def solve2(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[n - k] + nums[: n - k]
    return nums


print(solve([1, 2, 3, 4, 5, 6, 7], 3))
