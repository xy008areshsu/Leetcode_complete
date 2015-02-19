"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
"""

# idea:
# same as array_remove_duplicates. except that initialization needs to check if first two are the same.
# also except that during for loop, run two checks every time, since it allows two duplicates at most

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):   # More practice
        if len(A) == 0 or len(A) == 1 or len(A) == 2:
            return len(A)

        if A[0] == A[1]:
            first = 1
            second = 2
        else:
            first = 0
            second = 1


        while second < len(A):
            while second < len(A) and A[first] == A[second]:
                second += 1

            if second < len(A):
                A[second], A[first + 1] = A[first + 1], A[second]
                first += 1
                second += 1
                if second < len(A) and A[first] == A[second]:
                    A[second], A[first + 1] = A[first + 1], A[second]
                    first += 1
                    second += 1

        return first + 1



if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 2, 2, 3, 3, 3]))