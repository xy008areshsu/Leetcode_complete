"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# idea:
# for k in range(1, n + 1), k is the root node, and recursively generate left part and right part, and combine

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:   # MOre Practice
    # @return a list of tree node
    def generateTrees(self, n):
        return self.helper(1, n + 1)


    def helper(self, start, end):
        if start >= end:
            return [None]  # careful!
        if start == end + 1:
            return [TreeNode(start)]

        res = []
        for i in range(start, end):
            left_res = self.helper(start, i)
            right_res = self.helper(i + 1, end)
            for l_root in left_res:
                for r_root in right_res:
                    root = TreeNode(i)
                    root.left = l_root
                    root.right = r_root
                    res.append(root)

        return res