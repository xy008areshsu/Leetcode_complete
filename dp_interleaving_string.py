"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""


# function: f[i][j] = first i elements of s1 and first j elements of s2 can match first i + j elements of s3
# update: f[i][j] is True if:   f[i-1][j] is True and s3[i - 1 + j] == s1[i - 1]   or     f[i][j-1] is True and s3[i + j - 1] == s2[j - 1]
# init:  f[0][0] is True,      when i = 0, f[0][j] is True if f[0][j-1] is True and s3[j - 1] == s2[j - 1]
#                              when j = 0, ... the same
# final solution: f[len(s1)][len(s2)]

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):  # more practice
        if len(s1) == 0:
            return s2 == s3

        if len(s2) == 0:
            return s1 == s3

        if len(s1) + len(s2) != len(s3):
            return False

        f = [[False for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]  #  Bug prone.  I initially used the following to initialize: f = (len(s2) + 1) * [False], f = (len(s1) + 1) * [f[:]],  this is not a deep copy, WILL HAVE ERRORS!!!!!

        f[0][0] = True

        for j in range(1, len(s2) + 1):
            if f[0][j - 1] and s3[j - 1] == s2[j - 1]:
                f[0][j] = True

        for i in range(1, len(s1) + 1):
            if f[i - 1][0] and s3[i - 1] == s1[i - 1]:
                f[i][0] = True

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if (f[i-1][j] and s3[i + j - 1] == s1[i - 1]) or (f[i][j - 1] and s3[ i + j - 1] == s2[j - 1]):
                    f[i][j] = True

        return f[len(s1)][len(s2)]


if __name__ == '__main__':
    sol = Solution()
    s1 = 'ab'
    s2 = 'bc'
    s3 = 'bbac'
    print(sol.isInterleave(s1, s2, s3))