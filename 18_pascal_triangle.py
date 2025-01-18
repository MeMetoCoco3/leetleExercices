"""
18. Pascal's Triangle

Write a function solve that generates the first n rows of Pascal's Triangle.
"""


def get_size(n):
    return [[1] * i for i in range(1, n + 1)]


def give_value(arr):
    for i_idx, i_val in enumerate(arr):
        if len(i_val) < 3:
            continue
        for j_idx, _ in list(enumerate(arr[i_idx]))[1:-1]:
            arr[i_idx][j_idx] = arr[i_idx - 1][j_idx] + arr[i_idx - 1][j_idx - 1]
    return arr


def solve(n):
    return give_value(get_size(n))


for i in solve(9):
    print(i)
