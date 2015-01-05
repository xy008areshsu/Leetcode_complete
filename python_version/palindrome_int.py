"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""

class Solution:
    # @return a boolean
    def isPalindrome(self, x):  # more practice
        if x < 0:
            return False

        if x < 10:
            return True

        d = x
        l = 0
        while d > 0:
            d = d/10
            l += 1


        l_d = x
        r_d = x
        r = 0
        while l >= r:
            r_digit = r_d % 10
            l_digit = l_d / (10 ** (l - 1))
            if l_digit != r_digit:
                return False
            r_d = r_d / 10
            r += 1
            l_d = l_d - (l_d / (10**(l-1))) * (10 ** (l - 1))
            l -= 1

        return True

