"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []

        res = []
        direction = 0    # 0: right; 1: down;  2: left;  3: up
        val = 1
        self.spiral_flood(matrix, 0, 0, direction, res)

        return res

    def spiral_flood(self, mat, i, j, direction, res):
        res.append(mat[i][j])
        mat[i][j] = None
        if (j + 1 >= len(mat[0]) or mat[i][j + 1] == None) and (i + 1 >= len(mat) or mat[i + 1][j] == None) and (j - 1 < 0 or mat[i][j - 1] == None) and (i - 1 < 0 or mat[i - 1][j] == None):
            return

        if direction == 0:  # if previous direction is right
            if j + 1 >= len(mat[0]) or mat[i][j + 1] == None:
                direction = 1   # change it to down
                self.spiral_flood(mat, i + 1, j, direction, res)
            else:               # otherwise still head right
                self.spiral_flood(mat, i, j + 1, direction, res)
        elif direction == 1:    # down
            if i + 1 >= len(mat) or mat[i + 1][j] == None:
                direction = 2
                self.spiral_flood(mat, i, j - 1, direction, res)
            else:
                self.spiral_flood(mat, i + 1, j, direction, res)
        elif direction == 2:    # left
            if j - 1 < 0 or mat[i][j - 1] == None:
                direction = 3
                self.spiral_flood(mat, i - 1, j, direction, res)
            else:
                self.spiral_flood(mat, i, j - 1, direction, res)
        elif direction == 3:    # up
            if i - 1 < 0 or mat[i - 1][j] == None:
                direction = 0
                self.spiral_flood(mat, i, j + 1, direction, res)
            else:
                self.spiral_flood(mat, i - 1, j, direction, res)

if __name__ == '__main__':
    mat = [[2,5],[8,4],[0,-1]]
    sol = Solution()
    print(sol.spiralOrder(mat))



