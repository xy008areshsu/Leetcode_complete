"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):  # more practice
        if len(num) == 0:
            return None

        if len(num) == 1:
            return num[0]

        if len(num) == 2:
            return min(num[0], num[1])

        res = num[0]
        start = 0
        end = len(num) - 1
        return self.helper(num, start, end, res)

    def helper(self, num, start, end, res):
        if start > end:
            return res

        mid = start + (end - start) // 2
        if num[mid] < num[end]:
            res = min(res, num[mid])
            return self.helper(num, start, mid - 1, res)
        else:
            res = min(res, num[start])
            return self.helper(num, mid + 1, end, res)

    def method_2(self, num):
        if len(num) == 0:
            return None
        if len(num) == 1:
            return num[0]
        if len(num) == 2:
            return min(num[0], num[1])

        pivot = -1
        start = 0
        end = len(num) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if num[mid] < num[mid - 1] and num[mid] < num[mid + 1]:
                pivot = mid
                break
            elif num[mid] > num[start]:  # careful!
                start = mid
            else:
                end = mid

        if pivot == -1:
            if num[start] > num[end]:
                pivot = end

        if pivot == -1:
            pivot = 0

        return num[pivot]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMin([2, 3, 1]))