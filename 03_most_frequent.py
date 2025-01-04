def solve(nums):
    freq = {}
    for i in nums:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1

    max_count = 0
    max_num = None
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            max_num = num

    return max_num
