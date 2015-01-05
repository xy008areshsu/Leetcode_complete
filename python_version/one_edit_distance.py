"""
Given two strings S and T, determine if they are both one edit distance apart.
"""

# two cases are True ,   ASSUME len(s) <= len(t).  IF len(t) > len(s), call the function with s and t swapped!!!!!!
# 1. if length are the same, then only one character can be different, replace
# 2. if length is 1 difference, then one character should be inserted or deleted
# keep a counter i, first scan over s and t, find the i value that s[i] and t[i] first being different
# if i is not len of s, then if len(s) == len(t), check if s[i+1:] == t[i+1:]; if len(s) != len(t), check if s[i:] == t[i+1:]
# if i is len of s, if len(t) - len(s) == 1: True, else False
#

class Solution:
    # @param s, a string
    # @param t, a string
    # @return a boolean
    def isOneEditDistance(self, s, t):   # More practice
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        i = 0
        while i < len(s):
            if s[i] == t[i]:
                i += 1
            else:
                break

        if i == len(s):
            return len(t) == len(s) + 1
        else:
            if len(t) == len(s):
                return s[i+1:] == t[i+1:]
            else:
                return s[i:] == t[i+1:]
