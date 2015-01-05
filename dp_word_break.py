"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

# idea:
# function: f[i] if it can be break for first i+1 elements of s
# update: if s[: i + 1] is in dict, then f[i] is True; else, for j in range(i), if f[j] is True and s[j + 1 : i + 1] is in dict, then is True
# init: f[0] is True if s[0] in dict, else False
# final solution: f[len(s) - 1]

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        f = len(s) * [False]
        f[0] = True if s[0] in dict else False

        for i in range(1, len(s)):
            if s[:i + 1] in dict:
                f[i] = True
            else:
                for j in range(i):
                    if f[j] and s[j+1: i + 1] in dict:
                        f[i] = True
                        break

        return f[-1]