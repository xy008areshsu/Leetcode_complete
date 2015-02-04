"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        num = sorted([str(x) for x in num], cmp = self.compare)
        num.reverse()
        res = ''.join(num).lstrip('0')
        if res == '':
            res = '0'
        return res

    def compare(self, a, b):
        if a+b > b + a:
            return 1
        else:
            return -1






if __name__ == '__main__':
    num = [20, 1]
    num2 = [3, 30, 34, 5, 9]
    num3 = [121, 12]
    sol = Solution()
    print(sol.largestNumber(num2))
