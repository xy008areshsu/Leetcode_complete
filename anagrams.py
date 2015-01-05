"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""


class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        ana = {}
        for s in strs:
            s_list = list(s)
            s_list.sort()
            s_aux =''.join(s_list)
            if s_aux not in ana:
                ana[s_aux] = [s]
            else:
                ana[s_aux].append(s)

        res = []
        for key, val in ana.items():
            if len(val) >= 2:
                res += val

        return res