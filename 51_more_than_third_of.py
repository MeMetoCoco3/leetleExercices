"""
51. Majority Element II (n/3)

Write a function solve that finds all elements that appear more than n/3 times in an array.
"""


def solve(nums):
    mp = {}
    for i in nums:
        if mp.get(i):
            mp[i] += 1
            continue
        mp[i] = 1
    con = len(nums) / 3
    return [x[0] for x in mp.items() if x[1] > con]


print(solve([3, 2, 3]))
