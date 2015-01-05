"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        unique_path_num = {}
        unique_path_num[(0, 0)] = 0 if obstacleGrid[0][0] == 1 else 1
        block = len(obstacleGrid)
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                block = i
                break
        unique_path_num.update({(i, 0) : (1 if i < block else 0) for i in range(len(obstacleGrid))})


        block = len(obstacleGrid[0])
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                block = i
                break
        unique_path_num.update({(0, i) : (1 if i < block else 0) for i in range(len(obstacleGrid[0]))})

        return self.solve(obstacleGrid, unique_path_num, len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)

    def solve(self, obstacleGrid, unique_path_num, m, n):
        if m == 0 or n == 0:
            return unique_path_num[(m,n)]


        if obstacleGrid[m][n] == 1:
            unique_path_num[(m, n)] = 0
            return 0

        if (m - 1, n) in unique_path_num:
            unique_paths_number_m_1_n = unique_path_num[(m-1, n)]
        else:
            unique_paths_number_m_1_n = self.solve(obstacleGrid, unique_path_num, m - 1, n)

        if (m, n - 1) in unique_path_num:
            unique_paths_number_m_n_1 = unique_path_num[(m, n - 1)]
        else:
            unique_paths_number_m_n_1 = self.solve(obstacleGrid, unique_path_num, m , n - 1)

        unique_paths_number_m_n = unique_paths_number_m_1_n + unique_paths_number_m_n_1

        unique_path_num[(m, n)] = unique_paths_number_m_n

        return unique_paths_number_m_n


if __name__ == '__main__':
    obs = [[1,0]]
    obs1 = [[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],[0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1],[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0],[1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1],[1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1],[0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1],[1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0]]

    sol = Solution()

    print(sol.uniquePathsWithObstacles(obs))
    print(sol.uniquePathsWithObstacles(obs1))