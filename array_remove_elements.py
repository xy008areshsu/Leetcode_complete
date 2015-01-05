"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):  # more practice
        if len(A) == 0:
            return 0

        left = 0
        right = len(A) - 1

        while left <= right:
            if A[left] == elem:
                A[left], A[right] = A[right], A[left]
                right -= 1
            else:
                left += 1

        return left


