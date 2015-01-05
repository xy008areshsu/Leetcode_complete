"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):   # Do this iteratively, TODO!!!!!!
        c = 1
        return self.helper(digits, 0, len(digits) - 1, c)

    def helper(self, digits, start, end, c):
        if start > end:
            if c == 1:
                digits.insert(0, c)
            return digits

        if digits[end] + c > 9:
            digits[end] = 0
            c = 1
            return self.helper(digits, start, end - 1, c)
        else:
            digits[end] += c
            c = 0
            return digits

