"""15. Matrix Rotation

Write a function solve that rotates an n x n matrix 90 degrees clockwise in-place"""


def solve(matrix):
    n = len(matrix)
    solved = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            solved[j][n - 1 - i] = matrix[i][j]
    return solved


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solved = solve(matrix)

for i in solved:
    print(i)


for i in matrix:
    print(i)
