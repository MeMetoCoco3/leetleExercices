def solve(nums):
    for i, v in enumerate(nums):
        rest = nums[:i] + nums[i + 1 :]
        if v in rest:
            continue
        return v
