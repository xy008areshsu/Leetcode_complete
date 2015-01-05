"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates = list(set(candidates))
        candidates.sort()

        res = []
        list_aux = []
        pos = 0
        self.helper(candidates, target, res, list_aux, pos)

        return res

    def helper(self, candidates, target, res, list_aux, pos):
        if target == 0:
            res.append(list_aux[:])
            return

        if target < 0:
            return

        for i in range(pos, len(candidates)):
            if candidates[i] > target:
                return
            list_aux.append(candidates[i])
            self.helper(candidates, target - candidates[i], res, list_aux, i)
            list_aux.pop()


