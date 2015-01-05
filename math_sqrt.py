"""
mplement int sqrt(int x).

Compute and return the square root of x.
"""

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):   # method 1 use binary search, sqrt(x) cannot be larger than x / 2 + 1,  best suit if result is integer
        i = 0
        j = x / 2 + 1

        while i <= j:
            mid = i + (j - i) / 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                i = mid + 1
            else:
                j = mid - 1

        if j < 0:
            return 0
        else:
            return j

    def sqrt2(self, x):  # method 2 use Newton's method, can use to solve result that is not integer
        pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.sqrt(1))
