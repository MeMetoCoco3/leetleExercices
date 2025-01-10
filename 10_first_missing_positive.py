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


def solve2(nums):
    nums = [x for x in nums if x > 0]
    cnt = sum(nums)
    cnt2 = sum(range(min(nums), max(nums) + 1))
    return cnt2 - cnt


print(solve2([3, 4, -1, 1]))
