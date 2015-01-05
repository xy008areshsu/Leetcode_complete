"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""

class Solution:  # Approach 1: sort + two pointer O(nlogn) time   Approach 2: hash table  O(n) time, O(n) space
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        if len(num) == 0 or len(num) == 1:
            return None

        num_index_tuple = [(val, index) for index, val in enumerate(num)]

        num_index_tuple.sort()

        left = 0
        right = len(num_index_tuple) - 1

        while left < right:
            if num_index_tuple[left][0] + num_index_tuple[right][0] == target:
                return (min(num_index_tuple[left][1], num_index_tuple[right][1]) + 1, max(num_index_tuple[left][1], num_index_tuple[right][1]) + 1)
            elif num_index_tuple[left][0] + num_index_tuple[right][0] > target:
                right -= 1
            else:
                left += 1

        return None


    def twoSum_hash(self, num, target):
        if len(num) == 0 or len(num) == 1:
            raise Exception('No solution')

        hash_m = {}
        for i in range(len(num)):
            if (target - num[i]) in hash_m:
                return (hash_m[target-num[i]] + 1, i + 1)
            hash_m[num[i]] = i

        raise Exception('No solution')

if __name__ == '__main__':
    num = [2, 7, 11, 5]
    sol = Solution()
    print(sol.twoSum_hash(num, 9))


