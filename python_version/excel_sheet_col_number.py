"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        h_map = {s : i for (s, i) in zip(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), [i for i in range(1, 27)])}
        degree = len(s) - 1
        res = 0
        for c in s:
            if c not in h_map:
                return None
            res += h_map[c] * (26 ** degree)  # base 26
            degree -= 1

        return res
