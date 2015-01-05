"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

# idea:
# for j in range(len(triangle[-1]) f[i][j] = min path sum from first row to bottom row at col j, then we just need to find the min f[-1][j] for row i and return it.
# update: for each f[i][j] in row i, if j == 0, then f[i][j] = f[i - 1][j] + triangle[i][j]; if j == len(trianlge(row_i)), then f[i][j] = f[i - 1][j - 1] + triangle[i][j]; else  f[i][j] = min(f[i - 1][j - 1], f[i-1][j]) + triangle[i][j]
# init: f[0][0] = triangle[0][0]
# final solution: min(f[-1][j]) for all j

import time
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 1:
            return triangle[0][0]

        f = [[triangle[0][0]]]

        for i in range(1, len(triangle)):
            level = []
            for j in range(len(triangle[i])):
                if j == 0:
                    level.append(f[i - 1][j] + triangle[i][j])
                elif j == len(triangle[i]) - 1:
                    level.append(f[i - 1][j - 1] + triangle[i][j])
                else:
                    level.append(min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j])
            f.append(level)

        return min(f[-1])


