"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

# Pay attention to the difference between set and permutation

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        if len(S) == 0:
            return [[]]

        res = []
        list_aux = []
        pos = 0
        S.sort()
        self.helper(S, res, list_aux, pos)

        return res

    def helper(self, S, res, list_aux, pos):
        res.append(list_aux[:])

        for i in range(pos, len(S)):
            list_aux.append(S[i])
            self.helper(S, res, list_aux, i + 1)
            list_aux.pop()