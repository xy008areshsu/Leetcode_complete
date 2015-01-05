"""
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

    * Integers in each row are sorted from left to right.

    * The first integer of each row is greater than the last integer of the previous row.

Example
Consider the following matrix:

[

    [1, 3, 5, 7],

    [10, 11, 16, 20],

    [23, 30, 34, 50]

]

Given target = 3, return true.

Challenge Expand
O(log(n) + log(m)) time

Tags Expand

"""

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if target > matrix[-1][-1] or target < matrix[0][0] or len(matrix) == 0:
            return False

        row = 0
        start = 0
        end = len(matrix) - 1
        if target > matrix[-1][0]:
            row = end
        else:
            while start + 1< end:
                mid = start + (end - start) // 2
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] > target:
                    end = mid
                else:
                    start = mid

            if matrix[start][0] == target or matrix[end][0] == target:
                return True

            if target > matrix[start][0] and target < matrix[end][0]:
                row = start
            else:
                row = end

        start = 0
        end = len(matrix[row]) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid
            else:
                start = mid

        if matrix[row][start] == target or matrix[row][end] == target:
            return True

        return False

