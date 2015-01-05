"""
A peak element is an element that is greater than its neighbors.



For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
"""

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        if len(num) == 0:
            return None

        if len(num) == 1:
            return 0

        if len(num) == 2:
            if num[0] > num[1]:
                return 0
            else:
                return 1

        start = 0
        end = len(num) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if num[mid] > num[mid - 1] and num[mid] > num[mid + 1]:
                return mid
            elif num[mid] > num[mid - 1]:
                start = mid
            else:
                end = mid

        if num[start] > num[end]:
            return start
        else:
            return end



if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3]))