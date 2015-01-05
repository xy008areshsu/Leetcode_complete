"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        res = 0

        for n in A:
            res = res ^ n

        return res

    def using_hash_table(self, A):  # applies to any kind of single number, with other elements appear any number of times
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