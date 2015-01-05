"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution:
    # @return a string
    def convert(self, s, nRows):   # more practice
        board = []
        for i in range(nRows):
            board.append([])

        i = 0
        direction = 0  # 0 means down, 1 means up

        for c in s:
            board[i].append(c)
            if direction == 0 and i == nRows - 1:
                direction = 1
                i -= 1
            elif direction == 0 and i < nRows - 1:
                i += 1
            elif direction == 1 and i == 0:
                i += 1
                direction = 0
            elif direction == 1 and i > 0:
                i -= 1

        res = ''
        for str_list in board:
            res += ''.join(str_list)

        return res