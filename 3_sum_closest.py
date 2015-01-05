"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        if len(num) < 3:
            return 0

        num.sort()
        closest = float('inf')
        res = 0
        for i in range(len(num) - 2):
            if i != 0 and num[i] == num[i - 1]:
                continue

            left = i + 1
            right = len(num) - 1
            while left < right:
                _sum = num[i] + num[left] + num[right]
                if _sum == target:
                    return target
                else:
                    if abs(_sum - target) < closest:
                        closest = abs(_sum - target)
                        res = _sum
                    if _sum > target:
                        right -= 1
                    else:
                        left += 1

        return res

