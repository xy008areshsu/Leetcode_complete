"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

# idea:
# function: f[i][j] = minimum sum of all numbers from top left to (i, j)
# update:for i in range(1, len(grid)):
#            f[i][0] = f[i - 1][0] + grid[i][0]
#
#         for j in range(1, len(grid[0])):
#            f[0][j] = f[0][j - 1] + grid[0][j]
#
#         for i in range(1, len(grid)):
#            for j in range(1, len(grid[0])):
#               f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]
# init: f[0][0] = grid[0][0]
# final solution: f[len(grid) - 1][len(grid[0]) - 1]

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        f = []
        for i in range(len(grid)):
            f.append(len(grid[0]) * [float('inf')])

        f[0][0] = grid[0][0]

        for i in range(1, len(grid)):
            f[i][0] = f[i - 1][0] + grid[i][0]

        for j in range(1, len(grid[0])):
            f[0][j] = f[0][j - 1] + grid[0][j]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                f[i][j] = min(f[i - 1][j], f[i][j - 1]) + grid[i][j]

        return f[len(grid) - 1][len(grid[0]) - 1]