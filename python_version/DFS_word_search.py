"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""



class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):  # more practice
        if len(word) == 0:
            return False

        if len(board) == 0:
            return False

        for i in range(len(board)):
            board[i] = list(board[i])

        head_idx = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    head_idx.append((i, j))

        if len(head_idx) == 0:
            return False

        for idx in head_idx:
            str_aux = word[0]
            parent = {idx : None}
            if self.helper(board, word, idx, str_aux, parent):
                return True

        return False

    def helper(self, board, word, idx, str_aux, parent):
        if str_aux == word:
            return True

        for neighbor in self.neighbors(idx, board):
            if neighbor not in parent:
                if board[neighbor[0]][neighbor[1]] == word[len(str_aux)]:
                    parent[neighbor] = idx
                    str_aux += board[neighbor[0]][neighbor[1]]
                    if self.helper(board, word, neighbor, str_aux, parent):
                        return True
                    parent.pop(neighbor)   # careful!!!, don't forget this!!!   since it can go through other idx with the same character to construct the word
                    str_aux = str_aux[:-1]  # careful!!!, don't forget this!!!

        return False

    def neighbors(self, node_idx, board):
        res = []
        if node_idx[0] - 1 >= 0:
            res.append((node_idx[0] - 1, node_idx[1]))   # left neighbor

        if node_idx[0] + 1 < len(board):
            res.append((node_idx[0] + 1, node_idx[1]))   # right neighbor

        if node_idx[1] - 1 >= 0:
            res.append((node_idx[0], node_idx[1] - 1))   # neighbor above

        if node_idx[1] + 1 < len(board[0]):
            res.append((node_idx[0], node_idx[1] + 1))   # neighbor below

        return res

