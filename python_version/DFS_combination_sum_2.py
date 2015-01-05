"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        if len(candidates) == 0:
            return []

        candidates.sort()
        res = set()
        list_aux = []
        self.helper(candidates, target, list_aux, res, 0)

        return [list(t) for t in res]


    def helper(self, candidates, target, list_aux, res, pos):
        if target == 0:
            res.add(tuple(list_aux[:]))
            return
        if target < 0:
            return

        for i in range(pos, len(candidates)):
            if target < candidates[i]:
                break
            list_aux.append(candidates[i])
            self.helper(candidates, target - candidates[i], list_aux, res, i + 1)
            list_aux.pop()
