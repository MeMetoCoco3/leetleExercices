"""
16. Longest Consecutive Sequence

Write a function solve that finds the length of the longest consecutive sequence in an unsorted list.
"""


def solve(input):
    input = set(input)
    max_streak = 0
    current = 0
    for i in input:
        current += 1
        while i + 1 in input:
            current += 1
            i += 1
        max_streak = max(max_streak, current)
        current = 0
    return max_streak


print(solve([100, 4, 200, 1, 3, 2]))
print(solve([0, 3, 7, 2, 5, 8, 4, 6, 1]))
print(solve([]))
print(solve([0]))
