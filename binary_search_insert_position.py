"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A) == 0:
            return 0

        if target > A[-1]:
            return len(A)

        if target <= A[0]:
            return 0

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            elif target > A[mid]:
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        if A[end] == target:
            return end
        return end

