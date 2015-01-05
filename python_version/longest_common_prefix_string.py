"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):  # More practice
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]

        for i in range(1, len(strs)):
            if strs[i] == '':
                return ''
            prefix = prefix[: min(len(strs[i]), len(prefix))]
            for j in range(len(prefix)):
                if strs[i][j] != prefix[j]:
                    prefix = prefix[: j]
                    break

        return prefix