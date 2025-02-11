"""
42. Longest Substring Without Repeating Characters

Write a function solve that finds the length of the longest substring without
repeating characters.
"""


def solve(s):
    max_len = curr = start = 0
    mp = {}

    for i, val in enumerate(s):
        if val in mp and mp[val] >= start:
            start = mp[val] + 1
            curr = i - start + 1
        else:
            curr += 1

        mp[val] = i
        max_len = max(max_len, curr)
    return max_len


print(solve("abcabcbb"))  # 3
print(solve("pwwkew"))  # 3
print(solve("dvdf"))  # 3
