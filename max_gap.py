"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

Credits:
Special thanks to @porker2008 for adding this problem and creating all test cases.
"""


class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):  # more practice
        if len(num) < 2:
            return 0

        gap = 0
        num = self.radix_sort(num)
        for i in range(1, len(num)):
            gap = max(gap, num[i] - num[i - 1])

        return gap


    def radix_sort(self, num):
        max_num = max(num)
        len_max_num = len(str(max_num))
        for i in range(len_max_num):
            num = self.counting_sort(num, i)

        return num

    def counting_sort(self, num, digit):  # base 10, so the range is 0 to 9
        L = [[] for i in range(10)]
        if digit == 0:
            den = 1
        else:
            den = 10 ** digit

        for i in range(len(num)):
            key_i = num[i] // den    # need to get the number located in digit, e.g. 123, digit = 0, then it is 3, digit = 1, then it is 2
            key_i = key_i % 10
            L[key_i].append(num[i])

        res = []
        for l in L:
            res += l

        return res