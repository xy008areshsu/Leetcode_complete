"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

# idea:
# maintain: max_ending_here, min_ending_here,  max_so_far
# Exactly the same as max_sum_subarray, except that max_ending_here now might be one of the three: max(A[i], min_ending_here * A[i], max_ending_here * A[i]), since two negative number will give a positive number
# and min_ending_here = min(A[i], min_ending_here * A[i], max_ending_here * A[i]),
# update: max_so_far = max(max_so_far, max_ending_here)

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):  # http://blog.csdn.net/linhuanmars/article/details/39537283
        if len(A) == 0:
            return None

        if len(A) == 1:
            return A[0]

        max_so_far = A[0]
        max_local = A[0]
        min_local = A[0]

        for i in range(1, len(A)):
            max_temp = max_local
            max_local = max(max_local * A[i], A[i], A[i] * min_local)
            min_local = min(max_temp * A[i], A[i], A[i] * min_local)
            max_so_far = max(max_so_far, max_local)

        return max_so_far

