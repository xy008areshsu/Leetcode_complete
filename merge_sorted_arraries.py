"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note:
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

Hide Tags
"""

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        length = m + n - 1
        if len(A) == 0:
            return B
        if len(B) == 0:
            return A

        index = length
        i = m - 1
        j = n - 1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[index] = A[i]
                i -= 1
            else:
                A[index] = B[j]
                j -= 1
            index -= 1

        while j >= 0:
            A[index] = B[j]
            j -= 1
            index -= 1
