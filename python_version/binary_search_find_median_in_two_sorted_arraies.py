"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        if (len(A) + len(B)) % 2 == 0:
            return (self.get_kth(A, B, (len(A) + len(B)) / 2) + self.get_kth(A, B, (len(A) + len(B)) / 2 + 1)) / 2.0

        else:
            return self.get_kth(A, B, (len(A) + len(B)) / 2 + 1)

    def get_kth(self, A, B, k):
        if len(A) <= 0:
            return B[k-1]
        if len(B) <= 0:
            return A[k - 1]
        if k <= 1:
            return min(A[0], B[0])
        if len(A) / 2 + len(B) / 2 + 1 >= k:   # drop half of either A or B, take an example to verify the followings. e.g., len(A) = 8, len(B) = 10, k = 9
                                               # then: 4 + 5 + 1 = 10, if k == 9, and B[len(B) / 2] >= A[len(A) / 2], which means, B[5] >= A[4], the first 5 elements in B plus first 3 elements in A already has 9 elements, so the kth element cannot be in the second half of B.
            if B[len(B) / 2] >= A[len(A) / 2]:
                return self.get_kth(A, B[:len(B)/2], k)
            else:
                return self.get_kth(A[:len(A)/2], B, k)
        else:
            if B[len(B) / 2] >= A[len(A) / 2]:
                return self.get_kth(A[len(A) / 2 + 1: ], B, k - (len(A) / 2 + 1))
            else:
                return self.get_kth(A, B[len(B) / 2 + 1: ], k - (len(B) / 2 + 1))