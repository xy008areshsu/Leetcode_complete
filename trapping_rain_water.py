"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):               # More practice
        if len(A) == 0 or len(A) == 1:
            return 0

        # scan left to right
        sk = [A[0]]
        max_l = [0]
        max_l_cur = 0
        for i in range(1, len(A)):
            if A[i] >= A[max_l_cur]:
                max_l.append(i)
                max_l_cur = i
            else:
                max_l.append(max_l_cur)

        # scan right to left
        max_r = [len(A) - 1]
        max_r_cur = len(A) - 1
        for i in range(len(A) - 2, -1, -1):
            if A[i] >= A[max_r_cur]:
                max_r.append(i)
                max_r_cur = i
            else:
                max_r.append(max_r_cur)

        max_r.reverse()    # BUG PRONE, need this step

        # combine
        area = 0
        for i in range(len(A)):
            if max_l[i] != i and max_r[i] != i:
                area += abs(min(A[max_l[i]], A[max_r[i]]) - A[i])

        return area