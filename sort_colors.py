"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
"""

# one pass algorithm is the same as partition with two pivots!!!!!!!

class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        count = {}
        for i in A:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for i in range(len(A)):
            if 0 in count and count[0] > 0:
                A[i] = 0
                count[0] -= 1
            elif 1 in count and count[1] > 0:
                A[i] = 1
                count[1] -= 1
            elif 2 in count:
                A[i] = 2
                count[2] -= 1
