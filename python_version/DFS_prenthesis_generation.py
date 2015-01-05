"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""
"""
Analysis:
The classic question from the Cracking the Code Interview. DFS is enough. Note that it is wrong when the number of ')' is more than '(' in the current string. e.g. ()()).

"""


class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):   # Memorize !!!!!!!!!!!!!!
        if n == 0:
            return []
        if n == 1:
            return ['()']

        res = []
        l = 0
        r = 0
        str_aux = ''
        self.helper(n, res, l, r, str_aux)

        return res

    def helper(self, n, res, l, r, str_aux):
        if l == n and r == n:
            res.append(str_aux)
            return

        if l > n:
            return

        self.helper(n, res, l + 1, r, str_aux + '(')
        if l > r:
            self.helper(n, res, l, r + 1, str_aux + ')')

