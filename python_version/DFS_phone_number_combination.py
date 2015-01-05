"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
"""



class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):   # More practice
        res = []
        str_aux = ''
        map = {'2': 'abc', '3':'def', '4':'ghi', '5' : 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}
        self.helper(digits, res, str_aux, map, 0)

        return res

    def helper(self, digits, res, str_aux, map, pos):
        if len(str_aux) == len(digits):
            res.append(str_aux)
            return

        for i in range(pos, len(digits)):
            candidates = map[digits[i]]
            for c in candidates:
                str_aux += c
                self.helper(digits, res, str_aux, map, i + 1)
                str_aux = str_aux[:-1]