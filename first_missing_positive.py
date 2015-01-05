# coding=utf-8
"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

# 把出现的数值放到与下标一致的位置，再判断什么位置最先出现不连续的数值，就是答案了。 e.g., A[i] = 6, A[i] should be put in 6 - 1 = 5's location


class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):  # more practice
        if len(A) == 0:
            return 1

        i = 0
        while i < len(A):
            if A[i] > 0 and A[i] < len(A):
                if A[i] != A[A[i] - 1]:
                    temp = A[i]
                    A[i] = A[temp - 1]
                    A[temp - 1] = temp
                    i -= 1
            i += 1

        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1

        return len(A) + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstMissingPositive([0]))