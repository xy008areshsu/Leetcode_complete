"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""

# idea: different from permutation_1, in permutation_1 just a simple if num[i] not in list_aux, but here it has duplicates
# first sort it
# Use visited to track if num[i] has been used, avoid the case of putting itself again
# if num[i] == num[i-1] and visited[i-1] == 0, means num[i] and num[i-1] have been used, e.g. [1, 1] has been used, now [1, 1] cannot be used again


import time
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):   # more practice
        if num is None or len(num) == 0:
            return []

        num.sort()
        res = []
        list_aux = []
        visited = len(num) * [False]
        self.helper(num, res, list_aux, visited)

        return res

    def helper(self, num, res, list_aux, visited):
        if len(list_aux) == len(num):
            res.append(list_aux[:])
            return

        for i in range(len(num)):
            if visited[i] or (i != 0 and visited[i - 1] == False and num[i] == num[i - 1]):
                continue

            visited[i] = True
            list_aux.append(num[i])
            self.helper(num, res, list_aux, visited)
            visited[i] = False
            list_aux.pop()