"""10. First Missing Positive

Write a function solve that finds the first missing positive integer given an unsorted list.
That is, the smallest positive integer not in the list.
"""


def solve(nums):
    nums.sort()
    for i, val in enumerate(nums[: len(nums) - 2]):
        dif = nums[i + 1] - val
        ret = val + 1
        if dif > 1 and ret > 0:
            return val + 1

    return nums[-1] + 1


print(solve([7, 8, 9, 11, 12]))
