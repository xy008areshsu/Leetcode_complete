"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
"""

# idea: initialization max_area = 0
# step 1: preprocess, use an aux matrix ones[][] so that ones[i][j] is the cumulative number of 1s on row i, e.g. matrix = [ [0, 0, 1, 0, 1, 1, 1] ], ones[0] = [0, 0, 1, 0, 1, 2, 3]
# step 2: for each row in matrix, if ones[i][j] != 0, then h = 1,w = ones[i][j],  tmp_area = w * h; and go up, if ones[i - 1][j] != 0, w = min(w, ones[i - 1][j]), h += 1, tmp_area = max(tmp_area, w * h)
#         after traverse of row i, update max_area = max(max_area, tmp_area)

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer

    # leetcode python has problem for this one, c++ will pass, python will have LTE with input matrix of []!!!!!!
    def maximalRectangle(self, matrix):  #http://yucoding.blogspot.com/2013/01/incomplete-leetcode-question-47-maximal.html
        #step 1, preprocess

        res = 0
        if matrix == []:
            return 0

        ones = len(matrix[0]) * [0]
        ones = len(matrix) * [ones]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    if j == 0:
                        ones[i][j] = 1
                    else:
                        ones[i][j] = ones[i][j - 1] + 1

        # step 2, traverse
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if ones[i][j] != 0:
                    h = i - 1
                    mini = ones[i][j]
                    tmp_area = ones[i][j]
                    while h >= 0:
                        if ones[h][j] == 0:
                            break
                        else:
                            if ones[h][j] < mini:
                                mini = ones[h][j]
                            if mini * (i - h + 1) > tmp_area:
                                tmp_area = mini * (i - h + 1)
                        h -= 1

                    if tmp_area > res:
                        res = tmp_area

        return res