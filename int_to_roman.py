"""
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution:
    # @return a string
    def intToRoman(self, num):
        symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]   # if need sorted dictionary, use two arrays like this

        res = ''
        res = self.helper(num, symbols, values, res)   # BUG prone!!! string is immutable, must return something.
        return res

    def helper(self, num, symbols, values, res):
        if num <= 0:
            return res

        if num > values[0]:
            num -= values[0]
            res += symbols[0]
        else:
            start = 0
            end = len(values) - 1
            while start + 1 < end:
                mid = start + (end - start) // 2
                if num == values[mid]:
                    end = mid
                elif num > values[mid]:     # Bug prone, here values is high to low order
                    end = mid
                else:
                    start = mid

            if values[start] <= num:
                num -= values[start]
                res += symbols[start]
            else:
                num -= values[end]
                res += symbols[end]


        return self.helper(num, symbols, values, res)


