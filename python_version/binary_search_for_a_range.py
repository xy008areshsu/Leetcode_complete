"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if len(A) == 0:
            return [-1, -1]

        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            start_index = start
        elif A[end] == target:
            start_index = end
        else:
            start_index = -1

        if start_index != -1:
            start = start_index
            end = len(A) - 1
            while start + 1 < end:
                mid = start + (end - start) // 2
                if A[mid] == target:
                    start = mid
                elif A[mid] > target:
                    end = mid
                else:
                    start = mid

            if A[end] == target:
                end_index = end
            else:
                end_index = start

            return [start_index, end_index]

        return [-1, -1]