"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        rowIndex += 1
        if rowIndex == 0:
            return []
        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1, 1]

        last_level = [1, 1]
        for i in range(2, rowIndex):

            this_level = [1]
            for j in range(1, i ):
                this_level.append(last_level[j - 1] + last_level[j])

            this_level.append(1)

            last_level = this_level

        return this_level


if __name__ == '__main__':
    sol = Solution()
    print(sol.getRow(3))
