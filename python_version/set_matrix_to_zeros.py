"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        flag_row = len(matrix) * [False]
        flag_col = len(matrix[0]) * [False]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    flag_row[i] = True
                    flag_col[j] = True


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if flag_row[i] or flag_col[j]:
                    matrix[i][j] = 0

