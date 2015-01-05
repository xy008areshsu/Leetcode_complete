"""
Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        hash_m = {}

        for n in A:
            if n in hash_m:
                hash_m[n] += 1
            else:
                hash_m[n] = 1

        for n in A:
            if hash_m[n] == 1:
                return n

        return None