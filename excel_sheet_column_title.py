"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
"""

class Solution:
    # @return a string
    def convertToTitle(self, num):        # more practice
        titles = '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while num > 0:
            rem = num % 26
            num = num / 26
            if rem == 0:   #  to deal with the case of remainder is 0, e.g. 26, 52...
                rem = 26
                num -= 1
            res = titles[rem] + res

        return res