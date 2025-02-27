"""
58. Unique Paths

Write a function solve that returns the number of unique paths
if the grid has obstacles (1 means blocked).

"""


def solve(obstacleGrid):
    if not obstacleGrid or obstacleGrid[-1][len(obstacleGrid[0]) - 1] == 1:
        return 0
    cnt = 0
    for i in obstacleGrid:
        if 1 in i:
            continue
        cnt += 1
    return cnt
