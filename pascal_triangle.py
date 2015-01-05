"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1,1]]
        for i in range(2, numRows):

            this_level = [1]
            for j in range(1, i ):
                this_level.append(res[-1][j - 1] + res[-1][j])

            this_level.append(1)

            res.append(this_level)

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(6))
