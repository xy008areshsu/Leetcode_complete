"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""




class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num) < 4:
            return []

        res = []
        num.sort()
        for i in range(len(num) - 3):
            if i != 0 and num[i] == num[i - 1]:
                continue

            for j in range(i + 1, len(num) - 3):
                if j != 0 and num[j] == num[j - 1]:
                    continue

                left = j + 1
                right = len(num) - 1
                while left < right:
                    if num[i] + num[j] + num[left] + num[right] == target:
                        res.append([num[i], num[j], num[left], num[right]])
                        left += 1
                        right -= 1
                        while left < right and num[left] == num[left - 1]:
                            left += 1
                        while left < right and num[right] == num[right + 1]:
                            right -= 1
                    elif num[i] + num[j] + num[left] + num[right] < target:
                        left += 1
                    else:
                        right -= 1

        return res