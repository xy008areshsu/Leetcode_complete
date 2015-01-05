"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        h_set = set()
        for n in num:
            h_set.add(n)

        count = 0
        for n in num:
            new_count = 1
            i = 1
            while n + i in h_set:
                new_count += 1
                h_set.remove(n+i)
                i += 1
            i = 1
            while n - i in h_set:
                new_count += 1
                h_set.remove(n - i)
                i += 1
            count = max(count, new_count)

        return count