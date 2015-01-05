"""
Given a list of numbers, return all possible permutations.

Example
For nums [1,2,3], the permutaions are:

[

    [1,2,3],

    [1,3,2],

    [2,1,3],

    [2,3,1],

    [3,1,2],

    [3,2,1]

]

Challenge Expand
Do it without recursion
"""

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        list = []
        result = []
        return self.helper(nums, result, list)

    def helper(self,nums, result, list):
        if len(nums) == len(list):
            result.append(list[:])  # BUG PRONE, use [:] for a deep copy here!!!
            return result

        for n in nums:
            if n not in list:
                list.append(n)
                self.helper(nums, result, list)
                list.pop()

        return result


