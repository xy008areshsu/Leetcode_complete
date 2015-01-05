"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):                   # More practice
        for layer in range(len(matrix) / 2):
            first = layer
            last = len(matrix) - 1 - layer
            for i in range(first, last):
                offset = i - first

                top = matrix[first][i]   # save top

                matrix[first][i] = matrix[last - offset][first]    # left move to top


                matrix[last - offset][first] = matrix[last][last - offset]  # bottom move to left

                matrix[last][last - offset] = matrix[i][last]    # right move to bottom

                matrix[i][last] = top       # top move to right


        return matrix