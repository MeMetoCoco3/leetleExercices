"""
41. 3Sum Closest

Write a function solve that finds the sum of three integers in an array that is closest to a target number.
Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""


def solve(n, t):
    n.sort()
    mid = len(n) - 1
    for i, val in enumerate(n):
        if val > t:
            mid = i
            break
    possible_solutions = []

    f = mid - 2
    if f < 0:
        f = 0
        mid = 3

    while mid < len(n):
        if mid + 1 == len(n):
            possible_solutions.append(sum(n[-3:]))
        else:
            possible_solutions.append(sum(n[f: mid + 1]))
        f += 1
        mid += 1
    return min(possible_solutions, key=lambda x: abs(x - t))


def solve2(n, t):
    n.sort()
    mid = len(n) - 1
    for i, val in enumerate(n):
        if val > t:
            mid = i
            break
    possible_solutions = float("inf")

    f = mid - 2
    if f < 0:
        f = 0
        mid = 3

    while mid < len(n):
        current_sum = float("inf")
        if mid + 1 == len(n):
            current_sum = sum(n[-3:])
        else:
            current_sum = sum(n[f: mid + 1])

        if current_sum < possible_solutions:
            possible_solutions = current_sum
        f += 1
        mid += 1
    return possible_solutions


print(solve2([-1, 2, 1, -4], 1))
print(solve2([1, 1, 1, 1], 0))
