"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""

#idea: for each location i in s until to the location of len(s) - 1, expand two candidates of palindromes, one from center of i, the other one from center of i and i + 1
#, take the longest as the new updated one

class Solution:
    # @return a string
    def longestPalindrome(self, s):   # more practice
        if len(s) == 1:
            return s

        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        longest = ''
        for i in range(len(s) - 1):
            palindrom1 = self.expand(s, i, i)
            palindrom2 = self.expand(s, i, i+1)
            if len(palindrom1) > len(longest):
                longest = palindrom1
            if len(palindrom2) > len(longest):
                longest = palindrom2

        return longest

    def expand(self, s, c1, c2):
        if s[c1] != s[c2]:
            return ''

        left = c1
        right = c2
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break

        return s[left + 1 : right]

