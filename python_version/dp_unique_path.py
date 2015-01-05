"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        unique_paths_number = {}
        unique_paths_number[(0, 0)] = 1
        unique_paths_number.update({(0, i) : 1 for i in range(n)})
        unique_paths_number.update({(i, 0) : 1 for i in range(m)})
        return self.solve(unique_paths_number, m - 1, n - 1)

    def solve(self, unique_paths_number, m, n):
        if m == 0 or n == 0:
            unique_paths_number[(m, n)] = 1
            return 1

        if (m - 1, n) in unique_paths_number:
            unique_paths_number_m_1_n = unique_paths_number[(m-1, n)]
        else:
            unique_paths_number_m_1_n = self.solve(unique_paths_number, m - 1, n)

        if (m, n - 1) in unique_paths_number:
            unique_paths_number_m_n_1 = unique_paths_number[(m, n - 1)]
        else:
            unique_paths_number_m_n_1 = self.solve(unique_paths_number, m , n - 1)

        unique_paths_number_m_n = unique_paths_number_m_1_n + unique_paths_number_m_n_1

        unique_paths_number[(m, n)] = unique_paths_number_m_n

        return unique_paths_number_m_n
