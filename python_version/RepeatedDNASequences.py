"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        res = set()
        h_map = {}
        for i in range(len(s) - 9):
            s_aux = s[i : i + 10]
            if s_aux not in h_map:
                h_map[s_aux] = 1
            else:
                h_map[s_aux] += 1
                res.add(s_aux)

        return list(res)

    def method2(self, s):
        res = []
        h_map = {}

        if len(s) < 10:
            return res

        for i in range(len(s) - 9):
            s_aux = s[i : i + 10]
            if s_aux not in h_map:
                h_map[s_aux] = 1
            else:
                if h_map[s_aux] == 1:
                    res.append(s_aux)
                h_map[s_aux] += 1

        return res
