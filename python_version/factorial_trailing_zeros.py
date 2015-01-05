"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""

class Solution:
    # @return an integer
    def trailingZeroes(self, n):  # very simple, see http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/
        count = 0
        i = 5
        while n // i >= 1:
            count += n // i
            i *= 5

        return count

if __name__ == '__main__':
    sol =  Solution()
    print(sol.trailingZeroes(5))