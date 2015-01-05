"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return an integer
    def romanToInt(self, s):  # more practice
        symbols = {'M': 1000,
                   'CM': 900,
                   'D': 500,
                   'CD': 400,
                   'C': 100,
                   'XC' : 90,
                   'L' : 50,
                   'XL' : 40,
                   'X' : 10,
                   'IX' : 9,
                   'V' : 5,
                   'IV' : 4,
                   'I' : 1}

        res = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                candidate1 = 0
                candidate2 = 0
                if s[i] in symbols:
                    candidate1 = symbols[s[i]]
                if s[i:i+2] in symbols:
                    candidate2 = symbols[s[i:i+2]]
                if candidate1 > candidate2:
                    res += candidate1
                    i += 1
                else:
                    res += candidate2
                    i += 2

            else:
                if s[i] in symbols:
                    res += symbols[s[i]]
                    i += 1

        return res

