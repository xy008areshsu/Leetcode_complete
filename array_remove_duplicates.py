"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Hide Tags Array Two Pointers

"""

#idea: two pointers
# first = 0, second = 1
# scan the array A, until second hit the end.
# every time, use second to find the first element that is NOT equal to first, swap second and first + 1. Then increment both first and second
# return first + 1

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):   # More practice
        if len(A) == 0 or len(A) == 1:
            return len(A)

        first = 0
        second = 1
        while second < len(A):
            while second < len(A) and A[second] == A[first]:
                second += 1

            if second < len(A):
                A[first + 1], A[second] = A[second], A[first + 1]
                first += 1
                second += 1

        return first + 1
