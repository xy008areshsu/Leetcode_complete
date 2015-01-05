"""
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""


# function: f[i][j] number of distinct subsequence of first i characters of S S[: i + 1] in first j characters in T T[: j + 1]
# update: f[i][j],  f[i][j] must be at least f[i - 1][j]; then if S[i] == T[j], then f[i][j] += f[i-1][j-1]
# init:  f[i][0] = 0
# final solution: f[len(S)][len(T)]

class Solution:
    # @return an integer
    def numDistinct(self, S, T):  # more practice
        nums = []

        for i in range(len(S) + 1):
            nums.append((len(T) + 1) * [0])

        for i in range(len(S) + 1):
            nums[i][0] = 1

        for i in range(1, len(S) + 1):
            for j in range(1, len(T) + 1):
                nums[i][j] = nums[i - 1][j]
                if S[i - 1] == T[j - 1]:
                    nums[i][j] += nums[i - 1][j - 1]

        return nums[len(S)][len(T)]
