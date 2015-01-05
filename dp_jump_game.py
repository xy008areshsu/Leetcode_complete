"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

Hide Tags
"""

# function: f[i] if it is possible to jump to i
# update:  for j in range(i), if f[j] is True, check if A[j] >= i - j, if so, then f[i] is True
# inti: f[0] True,
# final solution: f[len(A) - 1]

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        can_jump = len(A) * [False]
        can_jump[0] = True

        for i in range(len(A)):
            for j in range(i):
                if can_jump[j] and j + A[j] >= i:
                    can_jump[i]= True;
                    break

        return can_jump[len(A) - 1]
