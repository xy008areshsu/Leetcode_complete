"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n == 0:
            return []

        mat = [n * [0] for i in range(n)]

        direction = 0    # 0: right; 1: down;  2: left;  3: up
        val = 1
        self.spiral_flood(mat, n, 0, 0, direction, val)

        return mat

    def spiral_flood(self, mat, n, i, j, direction, val):
        mat[i][j] = val
        if val == n ** 2:
            return

        if direction == 0:  # if previous direction is right
            if j + 1 >= len(mat[0]) or mat[i][j + 1] != 0:
                direction = 1   # change it to down
                self.spiral_flood(mat, n, i + 1, j, direction, val + 1)
            else:               # otherwise still head right
                self.spiral_flood(mat, n, i, j + 1, direction, val + 1)
        elif direction == 1:    # down
            if i + 1 >= len(mat) or mat[i + 1][j] != 0:
                direction = 2
                self.spiral_flood(mat, n, i, j - 1, direction, val + 1)
            else:
                self.spiral_flood(mat, n, i + 1, j, direction, val + 1)
        elif direction == 2:    # left
            if j - 1 < 0 or mat[i][j - 1] != 0:
                direction = 3
                self.spiral_flood(mat, n, i - 1, j, direction, val + 1)
            else:
                self.spiral_flood(mat, n, i, j - 1, direction, val + 1)
        else:    # up
            if i - 1 < 0 or mat[i - 1][j] != 0:
                direction = 0
                self.spiral_flood(mat, n, i, j + 1, direction, val + 1)
            else:
                self.spiral_flood(mat, n, i - 1, j, direction, val + 1)





if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(4))
