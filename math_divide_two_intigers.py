"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

Hide Tags
"""

# memorize it!!!!!!!!!!!!!!

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):   # more practice
        sign = 1
        if dividend < 0:
            sign *= -1

        if divisor < 0:
            sign *= -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        if abs(dividend) < abs(divisor) or dividend == 0:
            return 0

        if dividend == divisor:
            return 1 * sign

        count = 1

        while dividend >= (divisor << 1):
            divisor <<= 1
            count <<= 1

        res = 0

        while dividend > 0 and divisor >= 1:
            if dividend >= divisor:
                dividend -= divisor
                res += count

            divisor >>= 1
            count >>= 1

        res *= sign
        if res > 2147483647:
            res = 2147483647   # to deal with leetcode's MAX_INT, acutally in python MAX_INT can be much larger than 2147483647

        return res
