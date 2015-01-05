"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

# Detailed explanation see 9c chapter 5 1:34:00

# function: f[i][j] = minimum number of steps required to convert first i characters of word1 to first j numbers of characters of word2
# update:  f[i][j]: if word1[i] == word2[j], then f[i][j] = f[i-1][j-1]; else: we need one edit to convert from word1[i] to word2[j], so
#  f[i][j] = min(f[i-1][j] + cost(delete), f[i][j-1] + cost(insert), f[i-1][j-1] + cost(replace))
# init: f[0][j] = j,  convert a empty string to word2[:j+1] needs j steps of insertion
# final solution: f[len(word1)][len(word2)]

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        f = []  # f[i][j] means how many steps are required to make the first i chars of word1 to be equal to the first j chars of word2
        for i in range(len(word1) + 1):
            f.append([])
            for j in range(len(word2) + 1):
                if j == 0:
                    f[i].append(i)
                elif i == 0:
                    f[i].append(j)
                else:
                    f[i].append(None)

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i != 0 and j != 0:
                    if word1[i - 1] == word2[j - 1]:
                        f[i][j] = f[i - 1][j - 1]
                    else:
                        f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1


        return f[len(word1)][len(word2)]
