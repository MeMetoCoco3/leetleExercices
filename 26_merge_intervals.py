"""
26. Merge Intervals

Write a function solve that merges overlapping intervals and returns the merged list. Intervals are represented as lists of two integers: start and end.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""


def solve(input):
    if len(input) <= 1:
        return input
    input = sorted(input, key=lambda x: x[0])
    point = 0
    while point < len(input) - 1:
        print(input)
        if input[point][1] >= input[point + 1][0]:
            if input[point][0] <= input[point + 1][1] <= input[point][1]:
                pass
            else:
                input[point] = [input[point][0], input[point + 1][1]]
            input.pop(point + 1)
            continue
        point += 1
    return input


print(solve([[1, 3], [2, 6], [15, 18], [5, 10]]))

print(solve([[1, 4], [2, 3]]))
