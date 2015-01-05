"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Hide Tags
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):  # more practice
        if len(A) == 0:
            return -1

        if len(A) == 1:
            if target == A[0]:
                return 0
            else:
                return -1

        start = 0
        end = len(A) - 1
        while start <= end:  # Careful!!, >= instead of >
            mid = start + (end - start) // 2
            if A[mid] == target:
                return mid
            else:
                if A[mid] >= A[start]:  # Careful!!, >= instead of >
                    if target >= A[start] and target <= A[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if target >= A[mid] and target <= A[end]:
                        start = mid + 1
                    else:
                        end = mid - 1

        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.search([3, 1], 1))
