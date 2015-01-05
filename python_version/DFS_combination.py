"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if k > n:
            return []

        res = []
        list_aux = []
        pos = 1
        self.helper(n, k, res, list_aux, pos)

        return res

    def helper(self, n, k, res, list_aux, pos):
        if len(list_aux) == k:
            res.append(list_aux[:])
            return

        for i in range(pos, n + 1):
            list_aux.append(i)
            self.helper(n, k, res, list_aux, i + 1)
            list_aux.pop()
