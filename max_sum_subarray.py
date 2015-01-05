"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.


click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        max_so_far = A[0]
        max_ending_here = A[0]

        for i in range(1, len(A)):
            max_ending_here = max(max_ending_here + A[i], A[i])  #look at element after A[i], it would be greater if later elements will add a greater number between A[i] and max_end_here + A[i]
            max_so_far = max(max_ending_here, max_so_far)

        return max_so_far
