"""
62. Spiral Matrix

Write a function solve that returns all elements of an m x n matrix
in spiral order.
"""


def solve(arr):
    if not arr or not arr[0]:
        return []
    right = len(arr[0]) - 1
    bottom = len(arr) - 1
    left = top = 0
    res = []

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            res.append(arr[top][i])
        top += 1
        for i in range(top, bottom + 1):
            res.append(arr[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(arr[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(arr[i][left])
            left += 1
    return res


print(solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
