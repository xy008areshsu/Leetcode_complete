"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
"""
import copy

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        res = []
        list_aux = []
        self.helper(s, res, list_aux)

        return res

    def helper(self, s, res, list_aux):
        if len(s) == 0:
            res.append(list_aux[:])
            return

        for i in range(len(s)):
            if self.is_palindrome(s[: i + 1]):
                list_aux.append(s[: i + 1])
                self.helper(s[i + 1 : ], res, list_aux)
                list_aux.pop()

    def is_palindrome(self, s):
        if len(s) == 1:
            return True

        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
