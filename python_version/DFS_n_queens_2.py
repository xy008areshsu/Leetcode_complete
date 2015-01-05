"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

import copy
import time

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        res = []
        board = []
        for i in range(n):
            board.append(n * ['.'])

        self.solver(res, board, 0)
        if len(res) > 0:
            for i in range(len(res)):
                for j in range(len(res[i])):
                    res[i][j] = ''.join(res[i][j])
        return len(res)

    def solver(self, res, board, i):
        if i >= len(board):
            res.append(copy.deepcopy(board))

        for j in range(len(board[0])):
            if self.is_valid(i, j, board):
                board[i][j] = 'Q'
                self.solver(res, board, i + 1)
                board[i][j] = '.'

    def is_valid(self, i, j, board):
        for k in range(i):
            if board[k][j] == 'Q':  # same col
                return False
            queen_k_index = board[k].index('Q')
            if i - k == abs(j - queen_k_index):  # diagonal
                return False

        return True
