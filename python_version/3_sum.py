"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)

"""
# Lintcode all passed, but leetcode time limited exceeded

import time
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):   # more practice
        if len(num) < 3:
            return []

        num.sort()
        res = []
        for i in range(len(num) - 2):
            if i != 0 and num[i] == num[i - 1]:
                continue

            left = i + 1
            right = len(num) - 1
            while left < right:
                if num[i] + num[left] + num[right] == 0:
                    res.append([num[i], num[left], num[right]])
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left - 1]:
                        left += 1
                    while left < right and num[right] == num[right + 1]:
                        right -= 1
                elif num[i] + num[left] + num[right] > 0:
                    right -= 1

                else:
                    left += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4]))

