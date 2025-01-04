def solve(nums):
    sum1 = sum(nums)
    sum2 = sum(list(range(min(nums), max(nums) + 1)))
    res = sum2 - sum1
    if res == 0:
        return max(nums) + 1
    return res


#  XOR
def solve1(nums):
    result = 0
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result ^ len(nums)


# Math Based
def solve2(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


print(solve([0, 1]))
print(solve([0, 1, 2, 3, 5]))
