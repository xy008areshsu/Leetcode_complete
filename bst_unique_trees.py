"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0 or n == 1:
            return 1

        sum = 0

        for k in range(1, n + 1):
            left = self.numTrees(k - 1)
            right = self.numTrees(n - k)
            sum += sum + left * right

        return sum