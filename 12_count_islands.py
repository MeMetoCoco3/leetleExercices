"""12. Count Islands

Write a function solve that counts the number of islands in a 2D grid.
An island is surrounded by water (0s) and is formed by connecting adjacent
lands (1s) horizontally or vertically."""


def solve(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    islands = 0
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def dsf(x, y):
        grid[x][y] = 0
        for direction in directions:
            nx = direction[0] + x
            ny = direction[1] + y
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                dsf(nx, ny)

    for r_idx, row in enumerate(grid):
        for col_idx, _ in enumerate(row):
            if grid[r_idx][col_idx] == 1:
                islands += 1
                dsf(r_idx, col_idx)

    return islands


input = [[1, 1, 0], [0, 1, 0], [1, 0, 1]]
print(solve(input))
