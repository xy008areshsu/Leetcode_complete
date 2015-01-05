"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        if len(S) == 0:
            return [[]]

        S.sort()
        res = set()
        list_aux = []
        pos = 0
        self.helper(S, res, list_aux, pos)

        return [[n for n in t] for t in res]

    def helper(self, S, res, list_aux, pos):
        t = tuple(list_aux)
        res.add(t)

        for i in range(pos, len(S)):
            list_aux.append(S[i])
            self.helper(S, res, list_aux, i + 1)
            list_aux.pop()

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetsWithDup([0]))